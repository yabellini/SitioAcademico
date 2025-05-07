// Import Fuse.js for fuzzy search functionality
import Fuse from 'fuse.js';

document.addEventListener('DOMContentLoaded', function() {
    // Fetch the search index file
    fetch('/search-index.json')
    .then(response => response.json())
    .then(data => {
        const fuse = new Fuse(data, {
            keys: ['title', 'content'],
            includeScore: true
        });

        // Bind search input
        const searchInput = document.getElementById('search-input');
        const searchResults = document.getElementById('search-results');

        searchInput.addEventListener('input', function() {
            const results = fuse.search(this.value);
            let searchResultsHTML = '';

            // Display search results
            results.forEach(result => {
                searchResultsHTML += `<li><a href="${result.item.url}">${result.item.title}</a></li>`;
            });

            searchResults.innerHTML = searchResultsHTML;
        });
    });
});
