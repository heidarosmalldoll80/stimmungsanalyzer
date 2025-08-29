document.getElementById('analyzeButton').addEventListener('click', function() {
    const text = document.getElementById('inputText').value;
    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Stimmung: ' + data.stimmung;
    });
});
