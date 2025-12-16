document.addEventListener('DOMContentLoaded', function() {
    fetchQuote();

    document.getElementById('new-quote-btn').addEventListener('click', function() {
        fetchQuote();
    });
});

function fetchQuote() {
    fetch('quotes.json')
        .then(response => response.json())
        .then(data => {
            const randomIndex = Math.floor(Math.random() * data.length);
            const randomQuote = data[randomIndex];

            document.getElementById('quote').innerText = `${randomQuote.quote}`;
            document.getElementById('author').innerText = `- ${randomQuote.author}`;
        })
        .catch(error => {
            console.error('Error loading quotes:', error);
            document.getElementById('quote').innerText = "Could not load quotes.";
        });
}