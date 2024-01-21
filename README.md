# mAI-Mail
- This project was made using the repo [privateGPT](https://github.com/imartinez/privateGPT?tab=readme-ov-file). 
We have integrated web scrapping for your gmails using a script that you can log into.


 - Credits to [Salvik](https://github.com/Salvik-Krishna),[Ami](https://github.com/AmiBuch),[Mrudani](https://github.com/MrudaniPimpalkhare),[Vignesh](https://github.com/wig-nesh) for working on this.
- Team Chipi Chapa Dubi Daba FTW
![](https://tenor.com/view/chipi-chipi-chipi-chipi-chipi-chapa-chapa-cat-cat-chipi-gif-3982040863797256894)

## References

Our work uses the following software:

- PrivateGPT: 
@software{Martinez_Toro_PrivateGPT_2023,
author = {Martínez Toro, Iván and Gallego Vico, Daniel and Orgaz, Pablo},
license = {Apache-2.0},
month = may,
title = {{PrivateGPT}},
url = {https://github.com/imartinez/privateGPT},
year = {2023}
}
## Use cases and Featuers:
- Can easily understand Acedamic PDFs.
- Added the New TimeTable with Tut, can INSTANTLY answer when and where is your Tut/Class.
- Can read your mails and give you new information about the events that are going on and you can decide on yourself if you want to join or not.
- Can talk in normal LLM mode + Query mode + Search on the Docs. (this is the feature of the original repo)

## How to use it?
  ### First time Setup:
  ```sh
  git clone https://github.com/MostlyKIGuess/mAI-Mail.git && cd mAI-Mail && \
  python3.11 -m venv .venv && source .venv/bin/activate && \
  pip install --upgrade pip poetry && poetry install --with ui,local && ./scripts/setup

  # Launch the privateGPT API server **and** the gradio UI
  poetry run python3.11 -m private_gpt

  # In another terminal, create a new browser window on your private GPT!
  open http://127.0.0.1:8001/
  ```
 ### Normally:
 - Now you don't have to reinstalling everything again but if there are updates and features we will keep updating the documentation so you can watch out for it.
 - But now you don't have to run everything but just do:
 ```sh
  source .venv/bin/activate
  ## and launch 
  poetry run python3.11 -m private_gpt
  ## now open web browser
  open http://127.0.0.1:8001/
 ```
 ### Updating with mails and data ingestion.
 - The UI already provides you to add your pdf, where ;) (~~we keep this a secret but you can put your cpro assignment and ask for advice without needing to ask chatGPT, this model is reasonable enough to code.~~)
 - To remove the data you type 
 ```sh
 make wipe #inside the directory
 ```
- To add the data we have premade scripts inside the ./scrapper for copying the scrapped files after you scrap your emails.
- Then there is already a script called makefileforingestion.sh give it the execution perms and run it to ingest the data inside the model directly from the ./data folder.


### Setting up Credentials.json
To use this web scrapper, you need a `credentials.json` file for authenticating with the Gmail API. Here's how you can get it:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).

2. Click on "Select a project" at the top of the page, then click on "New Project", and create a project.

3. Once the project is created, select it.

4. In the left-hand menu, go to "APIs & Services" > "Library".

5. Search for "Gmail API" and click on it.

6. Click "Enable" to enable the Gmail API for your project.

7. In the left-hand menu, go to "APIs & Services" > "Credentials".

8. Click on "Create Credentials" > "OAuth client ID".

9. If you haven't configured the OAuth consent screen yet, you'll be asked to do so. Fill in the required fields. You can set the "User Type" to "External" for testing purposes.

10. Once the OAuth consent screen is configured, you'll be able to create the OAuth client ID. Set the "Application type" to "Desktop app", give it a name, and click "Create".

11. You'll see a screen with your client ID and client secret. Click "OK".

12. Back in the "Credentials" screen, you'll see your new OAuth 2.0 Client ID. Click on the download icon on the right to download your `credentials.json` file.

13. Move the `credentials.json` file to the ``./scrapper`` directory of this project.

- And WOHOO you are done and set uped.

 ## TMux 
 - You need TMux to run the `final.sh` script which runs every script I have mentioned above that is if you want it to directly run by just one click. :)
 
 - If you are having trouble running this , run the scripts alone to figure out what's wrong, feel very free to create issue I will reply as soon as possible. Also this might be useful :
 https://tmuxcheatsheet.com/


 ## PS
 - My sincere thanks to my teammates and the people who made the privateGPT repo, this is not my work and I do not take credits for it, some changes are made sure but that's all the thanks due to my teammates who have given many ideas and made this beautiful application which I will use (~~for DSA ASSIGNMENT~~)(I do not promote using AI , you will get MOSSED, do not use AI plsss, I code in nvim so this is not an option but I m jus saying uk).

- Thanks to my friends as well. :)