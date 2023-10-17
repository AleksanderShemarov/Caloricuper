document.addEventListener("DOMContentLoaded", function () {
    let buttonBlock = document.getElementsByClassName("button");
    // let buttons = buttonBlock.childNodes;
    for (let button of buttonBlock) {
        if (button.type !== undefined) {
            button.addEventListener("mousemove", () => {
                button.classList.add("focus");
            });
            button.addEventListener("mouseout", () => {
                button.classList.remove("focus");
            });
        }
    }
});
