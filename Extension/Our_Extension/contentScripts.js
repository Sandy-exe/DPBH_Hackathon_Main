// // List of words to highlight
// var words = ["film"];

// // Loop over each word
// for (var i = 0; i < words.length; i++) {
//   var word = words[i];

//   // Create a regular expression to find the word in the document
//   var regex = new RegExp("\\b" + word + "\\b", "gi");

//   console.log(document.documentElement.outerHTML);
//   // Replace the word with the same word wrapped in a span with a highlight class
//   document.body.innerHTML = document.body.innerHTML.replace(
//     regex,
//     function (match) {
//       return '<span class="highlight">' + match + "</span>";
//     }
//   );
// }

// // Add CSS for the highlight class
// var css = ".highlight { background-color: yellow; }";
// var style = document.createElement("style");

// if (style.styleSheet) {
//   style.styleSheet.cssText = css;
// } else {
//   style.appendChild(document.createTextNode(css));
// }

// document.getElementsByTagName("head")[0].appendChild(style);

function highlightText(word) {
  const body = document.body;
  const regex = new RegExp(`\\b${word}\\b`, "gi");

  function highlightNode(node) {
    const childNodes = node.childNodes;
    for (let i = 0; i < childNodes.length; i++) {
      const child = childNodes[i];
      if (child.nodeType === 3) {
        // Text node
        const matches = [...child.nodeValue.matchAll(regex)];
        console.log(matches);
        if (matches.length > 0) {
          let newHTML = child.nodeValue;
          for (let j = matches.length - 1; j >= 0; j--) {
            const match = matches[j];
            newHTML =
              newHTML.slice(0, match.index) +
              `<mark>${match[0]}</mark>` +
              newHTML.slice(match.index + match[0].length);
          }
          const newElement = document.createElement("span");
          newElement.innerHTML = newHTML;
          node.replaceChild(newElement, child);
        }
      } else if (child.nodeType === 1) {
        // Element node
        highlightNode(child);
      }
    }
  }
  highlightNode(body);
}

function addTagToText(key, word) {

  const body = document.body;
  const regex = new RegExp(`\\b${word}\\b`, "gi");
  console.log(regex);

  function addTagToNode(node) {
    const childNodes = node.childNodes;
    // console.log(childNodes);
    for (let i = 0; i < childNodes.length; i++) {
      const child = childNodes[i];
      if (child.nodeType === 3) {
        // Text node
        const matches = [...child.nodeValue.matchAll(regex)];
        if (matches.length > 0) {
          let newHTML = child.nodeValue;
          for (let j = matches.length - 1; j >= 0; j--) {
            const match = matches[j];
            newHTML =
              newHTML.slice(0, match.index) +
              match[0] +
              `&nbsp;&nbsp;&nbsp;&nbsp;<span class="_3LWZlK _1BLPMq" style="background: red;">${key}</span>` +
              newHTML.slice(match.index + match[0].length);
          }
          const newElement = document.createElement("span");
          newElement.innerHTML = newHTML;
          node.replaceChild(newElement, child);
        }
      } else if (child.nodeType === 1) {
        // Element node
        addTagToNode(child);
      }
    }
  }
  addTagToNode(body);
}

// Summa
// fetch("http://localhost:5000/get-text-to-highlight")
//   .then((response) => response.json())
//   .then((data) => {
//     // const textsToHighlight = data.textsToHighlight; // Assume the server returns a list of texts
//     // textsToHighlight.forEach((text) => {
//     //   highlightText(text);
//     // });
//   });



// chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
// //   // var data = request.processedData; // Assume this is a list of texts
// //   // data.forEach((text) => {
// //   //   highlightText(text);
// //   // });
// //   console.log(request);
//   console.log(request);
//   var processedReviews = request.processedReviews;
//   //highlightText(processedReviews);
//   console.log(processedReviews); // Assume this is a list of texts
//   // processedReviews.forEach((text) => {
//   //   highlightText(text);
//   // });
  
//   //highlightText("samsung");
// });

// var port = chrome.runtime.connect({ name: "my-connection" });

// port.onMessage.addListener(function (request) {
//   // Process the received data
//   console.log(request.processedReviews);

//   // Send a response
//   port.postMessage({ myResponse: "Data received!" });
// });



// content_script.js

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  // Process the received data
  console.log(Object.keys(request.myReviews).length);

  for (let key in request.myReviews) {
    if (request.myReviews.hasOwnProperty(key)) {
      console.log(request.myReviews[key]);
      console.log(request);
      console.log(request.myHighlight);
      if (request.myReviews[key] !== "") {
        addTagToText(request.myReviews[key], key);
      };
    }
  }

  for (let key in request.myHighlight) {
    if (request.myHighlight.hasOwnProperty(key)) {
      console.log(request.myHighlight[key]);
      console.log(request);
      console.log(request.myHighlight);
      if (request.myHighlight[key] !== "") {
        highlightText(request.myHighlight[key]);
      };
    }
  }

  
  // You can send a response here if needed
});