document.addEventListener("DOMContentLoaded", function() {
    let form = document.querySelector("form");

    form.onsubmit = function() {
        const title = document.querySelector("#title");
        const content = document.querySelector("#content");

        if (title.value === "" || content.value === ""){
            const message = document.querySelector(".message").innerHTML = "Incomplete Details."
            return false;
        }
    };
});