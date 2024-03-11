

document.addEventListener("DOMContentLoaded", function() {
    // Function to handle button click
    function handleClick() {
        const outputTextElement = document.getElementById("outputText");
        outputTextElement.textContent = "Button clicked!";
    }

    // Adding click event listener to the button
    const clickMeBtn = document.getElementById("clickMeBtn");
    clickMeBtn.addEventListener("click", handleClick);
});
