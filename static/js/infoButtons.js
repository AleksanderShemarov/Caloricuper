document.addEventListener("DOMContentLoaded", function () {
    let buttonBlock = document.querySelectorAll("div.button");
    for (let button of buttonBlock) {
        button.addEventListener("mousemove", () => {
            button.classList.add("focus");
            button.classList.add("focus.a");
        });
        button.addEventListener("mouseout", () => {
            button.classList.remove("focus");
            button.classList.remove("focus.a");
        });
    }
});
