document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    // After Submitting the form...
    form.onsubmit = function() {
        const empty = "";
        const image = document.querySelector("#image-upload-field").value;
        const school = document.querySelector("#school").value;
        const intro = document.querySelector("#intro").value;

        if ( image === empty || school === empty || intro === empty ) {
            document.querySelector(".message").innerHTML = "Please fill the details."
            return false;
        }
    };
});