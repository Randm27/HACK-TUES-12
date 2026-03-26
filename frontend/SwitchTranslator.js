;

const signToText = document.getElementById("sign-to-text");
const textToSign = document.getElementById("text-to-sign");
const switchButton = document.getElementById("switch-button");

switchButton.addEventListener("click", () =>{
    signToText.classList.toggle("mode-active");  
    signToText.classList.toggle("secondary-mode");

    textToSign.classList.toggle("mode-active");
    textToSign.classList.toggle("secondary-mode");
});