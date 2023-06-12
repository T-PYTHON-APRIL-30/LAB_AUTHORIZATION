console.clear();
"use strict";

/* Note: Dark mode / High Contrast hurts my eye's and causes discomfort, migraines as well as blurred vision. Unfortunetly, due to this, I can't test this mode properly. If anyone plans to use this, this is just a visual example and you should make your own changes. */

//
// For development use only
//
(function() {
   
   var isLight = 1;
   
   var mapContrast = [];
   
   // backgrounds
   document.querySelectorAll(".bg-white").forEach(function(item) {
      mapContrast.push(["bg-white", "bg-dark", item]);
   });
   
   document.querySelectorAll(".bg-dark").forEach(function(item) {
      mapContrast.push(["bg-dark", "bg-white", item]);
   });
   
   document.querySelectorAll(".bg-light").forEach(function(item) {
      mapContrast.push(["bg-light", "bg-black", item]);
   });
   
   // text
   document.querySelectorAll(".text-dark").forEach(function(item) {
      mapContrast.push(["text-dark", "text-white", item]);
   });
   
   document.querySelectorAll(".text-white").forEach(function(item) {
      mapContrast.push(["text-white", "text-dark", item]);
   });
   
   // links
   document.querySelectorAll(".link-dark").forEach(function(item) {
      mapContrast.push(["link-dark", "link-light", item]);
   });
   
   document.querySelectorAll(".link-light").forEach(function(item) {
      mapContrast.push(["link-dark", "link-light", item]);
   });
   
   
   document.querySelector(".app-dl-mode").addEventListener("click", function() {
      isLight = isLight ? 0 : 1;
      
      mapContrast.forEach(function(item) {
         item[2].classList.remove(item[isLight]);
         item[2].classList.add(item[isLight ? 0 : 1]);
      });
   }, false);
   
})();