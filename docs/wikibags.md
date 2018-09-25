# Wikipedia Bag-of-Words parser
// Written on **September 24th, 2018**

Wikipedia [Bag of words](https://en.wikipedia.org/wiki/Bag-of-words_model) as a service.

Suppose we're interested in analyzing wikipedia's article on [bag of words](https://en.wikipedia.org/wiki/Bag-of-words_model).

## Response Format
Use curl or requests to hit [https://data.pengra.io/wikibags/Bag-of-words_model/](https://data.pengra.io/wikibags/Bag-of-words_model/). 
Responses will always be in JSON in the following format:

```json
// Redirects to https://data.pengra.io/wikibags/14003441/
{
    "updated_at": "2018-09-24T19:43:15.419147-07:00",
    "page": "bag-of-words_model",
    "wiki_id": 14003441,
    "title": "Bag-of-words model",
    "header_bag_size": 17,
    "bag_size": 1191,
    "header_bag": { "word": somecount, ... },
    "bag": { ... }
}
```

All requests using `page` will be redirected to its `wiki_id` equivalent.

## Data Source:
[Wikipedia API](https://en.wikipedia.org/w/api.php?action=parse&pageid=&format=json) provides the initial data, and then it is cached permanently.
