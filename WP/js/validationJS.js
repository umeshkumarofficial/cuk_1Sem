
function validate() {

    alert("Validation started!");

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let course = document.getElementById("course").value.trim();

    if (name == "") {
        alert("Please enter your name!");
        return false;
    }

    if (email == "") {
        alert("Please enter your email!");
        return false;
    }

    if (!email.includes("@") || !email.includes(".")) {
        alert("Please enter a valid email!");
        return false;
    }

    if (course == "") {
        alert("Please select a course!");
        return false;
    }

    alert("Registration Successful!");

    location.reload();

    return false;
}
