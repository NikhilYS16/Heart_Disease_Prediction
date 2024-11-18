async function submitForm() {
    const formData = new FormData(document.getElementById('predictionForm'));
    const data = {};
    formData.forEach((value, key) => data[key] = Number(value));
    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    const result = await response.json();
    document.getElementById('result').innerText = result.message;
}