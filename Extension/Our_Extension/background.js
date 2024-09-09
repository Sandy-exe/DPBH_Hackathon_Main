// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//   // Send the processed data to the content script
//   console.log(request.tabID);
//   console.log(typeof request.processedReviews);
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  
//     chrome.tabs.sendMessage(tabs[0].id, {
//       processedReviews: request.processedReviews,
//     });
//   });
// });

// background.js
chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.activeTab) {
    console.log("Received message:", request.myReviews);
    console.log("Received Tab:", request.activeTab.id);
    console.log("Received Hightlight:", request.myHighlight);
    let success = false;
    let retries = 0;

    while (!success && retries < 3) {
      try {
        chrome.tabs.query(
          { active: true, currentWindow: true },
          function (tabs) {
            chrome.tabs.sendMessage(request.activeTab.id, {
              myReviews: request.myReviews,
              myHighlight: request.myHighlight,
            });
          }
        );
        success = true; // If the operation succeeds, set success to true
      } catch (error) {
        console.error("Error:", error);
        retries++; // If an error occurs, increment the retry count
      }
    }
    // Process the message here
  }
});

// // In your background script
// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
//   // Query for the active tab in the current window
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//     if (tabs.length > 0) {
//       // Establish a connection to the active tab
//       var port = chrome.tabs.connect(tabs[0].id, {name: "my-connection"});
      
//       // Send the processed data to the content script
//       port.postMessage({processedReviews: request.processedReviews});
      
//       // Listen for a response
//       port.onMessage.addListener(function(response) {
//         console.log(response.myResponse);
//       });
//     } else {
//       console.log('No active tabs found.');
//     }
//   });
// });