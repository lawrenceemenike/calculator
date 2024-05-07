function initializeCalculator() {
    const numInputs = document.querySelectorAll('input[type="text"]');
    numInputs.forEach(input => {
        input.addEventListener('input', validateInput);
    });
}

function validateInput(event) {
    const input = event.target;
    const value = input.value;
    const isNumber = /^-?\d*\.?\d*$/.test(value);
    
    if (!isNumber) {
        input.value = value.replace(/[^-.\d]/g, '');
    }
}