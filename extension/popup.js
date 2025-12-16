document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('new-quote-btn');
    const quoteText = document.getElementById('quote-text');
    const authorText = document.getElementById('quote-author');

    fetchQuote();

    btn.addEventListener('click', function() {
        fetchQuote();
    });

    function fetchQuote() {
        fetch('database/quotes.json')
            .then(response => response.json())
            .then(data => {
                const randomIndex = Math.floor(Math.random() * data.length);
                const randomQuote = data[randomIndex];

                quoteText.innerText = randomQuote.quote;
                authorText.innerText = "— " + randomQuote.author;
            })
            .catch(error => {
                console.error(error);
                quoteText.innerText = "Error loading quotes.";
            });
    }
});