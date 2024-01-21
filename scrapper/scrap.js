function saveAllEmailsToFolder() {
    // Get all threads in the Inbox
    var threads = GmailApp.getInboxThreads();
  
    // Get the folder where you want to save the text files
    var folder = DriveApp.getFolderById('1fRLD0DvC7rBMV95mcVW-5zAXqAQXPkq-');
  
    // Iterate through each thread and save the emails as text files
    for (var i = 0; i < threads.length; i++) {
      var messages = threads[i].getMessages();
      for (var j = 0; j < messages.length; j++) {
        var subject = messages[j].getSubject();
        var body = removeHtmlTags(messages[j].getBody());
  
        // Check if a file with the same name already exists
        var existingFiles = folder.getFilesByName(subject + '.txt');
        if (!existingFiles.hasNext()) {
          // File doesn't exist, create a new one
          folder.createFile(subject + '.txt', body);
        }
      }
    }
  }
  
  // Function to remove HTML tags from a string
  function removeHtmlTags(html) {
    var plainText = html.replace(/<[^>]*>/g, '');
    return plainText;
  }