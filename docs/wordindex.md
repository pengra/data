# Wikipedia Based Word Index
// Written on **October 20th, 2018**

This service returns the most popular words mined from [wikibags](https://data.pengra.io/wikibags/).

## Response Format

Use curl or requests to hit [data.pengra.io/wordindex/](https://data.pengra.io/wordindex/). 
Default responses will always be in JSON in in the following format:

```json
// Get a list of most common words
{
    "count": 150005,
    "next": "https://data.pengra.io/wordindex/?page=2",
    "previous": null,
    "results": [
        {
            "word": "down",
            "count": 910,
            "isAlnum": true
        },
        {
            "word": "military",
            "count": 905,
            "isAlnum": true
        },
        {
            "word": "region",
            "count": 897,
            "isAlnum": true
        },
        ...
```

## Stop Word Behavior

By default, anytime a word mined from wikibags makes up more than 0.03% of the total words, or appears on more than 85% of all pages, it's marked as a "stop word".
Default queries will ignore stop words. 
To include stop words in query, append [`?WordDensityMax=1&ArticleDensityMax=1`](https://data.pengra.io/wordindex/?WordDensityMax=1&ArticleDensityMax=1) to query.
You can specify your own definition of stop words by tweaking decimal values.

## Other Filters

If `isAlnum` is set to true, then queryset will exclude all punctuation. 
You can specify word count via `count=<value>` but it's more useful to specify word desnity or article density.
You can also search for a word using `word=<value>`, search will honor `WordDesnityMax` and `ArticleDensityMax`.
