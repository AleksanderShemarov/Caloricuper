document.addEventListener("DOMContentLoaded", function () {
    let data = {
        1: [
            "Before You start, fill your data in, such as name, email, password.",
            "/static/images/regist.jpg",
            "Sing Up",
        ],
        2: [
            "Fill your weight and height in to set calories start point.",
            "/static/images/start_point.jpg",
            "Mass Index",
        ],
        3: [
            "That's all! Use the application and check up your body calories.",
            "/static/images/full_ahead.jpg",
            "Let's start!",
        ],
    };
    let prev = document.querySelector("input.arrow-up-1"),
        next = document.querySelector("input.arrow-up-2"),
        number = document.querySelector("div.num"),
        text = document.getElementById("text"),
        image = document.getElementById("pict");
    let counter = 1;
    number.textContent = counter;
    text.textContent = data[counter][0];
    image.setAttribute("src", data[counter][1]);
    image.setAttribute("alt", data[counter][2]);
    prev.addEventListener("click", function () {
        if (number.textContent === "1") counter = 3;
        else counter -= 1;
        number.textContent = counter;
        text.textContent = data[counter][0];
        image.setAttribute("src", data[counter][1]);
        image.setAttribute("alt", data[counter][2]);
    });
    next.addEventListener("click", function () {
        if (number.textContent === "3") counter = 1;
        else counter += 1;
        number.textContent = counter;
        text.textContent = data[counter][0];
        image.setAttribute("src", data[counter][1]);
        image.setAttribute("alt", data[counter][2]);
    });
    // for (let key of Object.keys(data)) {
    //     console.log(key, data[key]);
    // }
});
