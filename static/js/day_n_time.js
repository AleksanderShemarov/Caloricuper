document.addEventListener("DOMContentLoaded", function () {
    let date = new Date();
    let days = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturnday",
        ],
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ];
    let day = document.getElementById("weekday"),
        clock = document.getElementById("time");
    day.textContent = days[date.getDay()];
    clock.textContent = `${
        date.getHours() > 9 ? date.getHours() : "0" + date.getHours()
    }:${date.getMinutes() > 9 ? date.getMinutes() : "0" + date.getMinutes()}:${
        date.getSeconds() > 9 ? date.getSeconds() : "0" + date.getSeconds()
    }`;
    setInterval(() => {
        let newTime = new Date();
        clock.textContent = `${
            newTime.getHours() > 9
                ? newTime.getHours()
                : "0" + newTime.getHours()
        }:${
            newTime.getMinutes() > 9
                ? newTime.getMinutes()
                : "0" + newTime.getMinutes()
        }:${
            newTime.getSeconds() > 9
                ? newTime.getSeconds()
                : "0" + newTime.getSeconds()
        }`;
    }, 1000);
});
