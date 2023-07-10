document.addEventListener("DOMContentLoaded", function () {
    let buttonBlock = document.querySelector("div.buttons");
    let buttons = buttonBlock.childNodes;
    for (let button of buttons) {
        if (button.value !== undefined) {
            button.addEventListener("mousemove", () => {
                button.classList.add("focus");
            });
            button.addEventListener("mouseout", () => {
                button.classList.remove("focus");
            });
        }
    }
});
