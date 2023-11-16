document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        // Prevent the form from submitting
        event.preventDefault();

        // Validate the form fields
        if (validateForm()) {
            // If the form is valid, submit it
            form.submit();
        }
    });

    function validateForm() {
        let isValid = true;

        // Validate each input field
        const inputFields = form.querySelectorAll('input');
        inputFields.forEach(function (input) {
            if (input.checkValidity() === false) {
                isValid = false;
                alert(`Please enter a valid value for ${input.name}.`);
            }
        });

        return isValid;
    }
});
