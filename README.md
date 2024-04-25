# Website Search Feature Documentation

## How to Use the Search Feature

The website now includes a content search feature that allows users to quickly find information across the site. To use the search feature, simply type your query into the search input field located in the header of the website. As you type, search results will dynamically appear below the input field, displaying relevant page titles and snippets of content. Click on a result to navigate to the corresponding page.

## Customizing the Search Settings

The search functionality is powered by Fuse.js, a lightweight fuzzy-search library. The search settings can be customized by editing the `static/js/search.js` file. Here, you can adjust the search parameters such as `threshold` for result relevance, `location` and `distance` for matching accuracy, and `keys` to specify which object properties to search in. For more detailed information on customizing Fuse.js options, refer to the [Fuse.js documentation](https://fusejs.io/).

