chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
  let url = tabs[0].url;
  fetch("http://localhost:5000/receive-data", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url, tabID: tabs[0].windowId }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        let activeTab = tabs[0];
        console.log(data.processedReviews);
        console.log(data.textsToHighlight);
        console.log(activeTab);
        chrome.runtime.sendMessage({
          myReviews: data.processedReviews,
          activeTab: activeTab,
          myHighlight: data.textsToHighlight,
        });
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

// popup.js
// function checkReviews() {
//   fetch("http://localhost:5000/get-reviews")
//     .then((response) => response.json())
//     .then((data) => {
//       if (data.status !== "no data") {
//         chrome.tabs.query(
//           { active: true, currentWindow: true },
//           function (tabs) {
//             let activeTab = tabs[0];
//             chrome.runtime.sendMessage({
//               myMessage: data.processedReviews,
//               activeTab: activeTab,
//             });
//           }
//         );
//       }
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });
// }
// // Check for new reviews after a delay of 5 seconds
// setTimeout(checkReviews, 5000);

// chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//   let url = tabs[0].url;
//   fetch("http://localhost:5000/receive-data", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ url,'tabID': tabs[0].windowId }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       console.log(data.processedReviews);
//       // Establish a connection to the background script
//       var port = chrome.runtime.connect({name: "my-connection"});
//       // Send the processed data to the background script
//       port.postMessage({ processedReviews: 'Classy product', tabID : data.tabsID });
//       // Listen for a response
//       port.onMessage.addListener(function(response) {
//         console.log(response.myResponse);
//       });
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });
// });
