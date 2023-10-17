document.addEventListener("DOMContentLoaded", function () {
    let info1 = document.getElementById("info_1"),
        messageField = document.querySelector("div.mesField"),
        info2 = document.getElementById("info_2"),
        contactList = document.querySelector("div.contact_list");
    info2.addEventListener("click", function () {
        messageField.style.display = "none";
        messageField.style.visibility = "hidden";
        contactList.style.display = "block";
        contactList.style.visibility = "visible";
    });
    info1.addEventListener("click", function () {
        contactList.style.display = "none";
        contactList.style.visibility = "hidden";
        messageField.style.display = "block";
        messageField.style.visibility = "visible";
    });
});
