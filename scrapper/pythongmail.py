from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os
import base64

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
 
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                './scrapper/credentials.json', SCOPES) #for final script
                # './credentials.json', SCOPES) #for testing
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

   # Call the Gmail API to fetch threads
    results = service.users().threads().list(userId='me').execute()
    threads = results.get('threads', [])

    # Open a text file for writing
    with open('threads.txt', 'w') as f:
        # Iterate over each thread
        for thread in threads:
            # Fetch the thread details
            tdata = service.users().threads().get(userId='me', id=thread['id']).execute()
            # Get all the messages in the thread
            messages = tdata['messages']

            # Write the thread ID to the file
            f.write(f'Thread ID: {thread["id"]}\n')

            # Iterate over each message
            for msg in messages:
                # Get the message headers
                headers = msg['payload']['headers']
                # Find the subject and date headers
                subject = next(h['value'] for h in headers if h['name'] == 'Subject')
                date = next(h['value'] for h in headers if h['name'] == 'Date')
                # Write the subject and date to the file
                f.write(f'Subject: {subject}\nDate: {date}\n')

                # Get the message body
                if 'parts' in msg['payload']:
                    # The message body is in a part
                    for part in msg['payload']['parts']:
                        if part['mimeType'] == 'text/plain':
                            # Decode the base64 message body
                            text = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                            f.write(f'Content: {text}\n')
                else:
                    # The message body is not in a part
                    text = base64.urlsafe_b64decode(msg['payload']['body']['data']).decode('utf-8')
                    f.write(f'Content: {text}\n')

            # Write a separator between threads
            f.write('-' * 40 + '\n')
    for thread in threads:
        print(f'Thread ID: {thread["id"]}')

if __name__ == '__main__':
    main()