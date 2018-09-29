# Broward County COMPASS data
// Written on **September 29th, 2018**

This is an API that hosts the dataset of Broward County

## Notable Lab
I wrote a lab about this dataset: [Naturally Occurring Racial Bias in AIs](https://pengra.github.io/labs/compass_analysis). The API has changed a lot since this writing.

## Filtering

### By ethnicity
`inmate_ethnicity` will be one of the following values:
- african-american
- asian
- caucasian
- hispanic
- native-american
- other
You can filter the result by ethnicity by appending `?inmate__ethnicity=<ethnicity>`.

### By gender
`inmate_sex` will be one of the following values:
- male
- female
You can filter the result by ethnicity by appending `?inmate__sex=<sex>`

### By score
`violence_score`, `recidivism_score` and `fail_to_appear_score` is a nullable rating from 1-10.
Each score is filterable. For instance, you can filter the result by violence risk by append `?violence_score=<score>`.

### By language
`inmate_language` will be either `english` or `spanish`.
You can filter the result by language by appending `?inmate__language=<language>`

### By type
`type` will either be `new` or `copy`.
You can filter the result by type by appending `?type=<type>`

#### Examples:
- [African American males with a `violence_score` of 10](https://data.pengra.io/compas/?inmate__ethnicity=african-american&inmate__sex=male&violence_score=10)
- [Caucasians males with a `violence_score` of 10](https://data.pengra.io/compas/?inmate__ethnicity=caucasian&inmate__sex=male&violence_score=10)

## Response Data
Each query will return a dictionary with at least 3 of the 4 keys:
- `next` - Results are paginated, so this links to the next page of results
- `previous` - as mentioned, results are paginated, so this links to the previous page of results
- `meta` - This dictionary contains demographic, gender and scoring meta data that summarizes the results
- `results` - An array containing this page's results.

### Results Format
Use curl or requests to hit [https://data.pengra.io/compas/](https://data.pengra.io/compas/). 
The results will be split into pages with 100 items per page. Results will appear in the following format:
```json
"results": [
    {
        "inmate_id": 00001,
        "inmate_sex": "female",
        "inmate_ethnicity": "african-american",
        "inmate_dob": "YYYY-MM-DD",
        "inmate_legal_status": "pretrial",
        "inmate_custody_status": "jail inmate",
        "inmate_marital_status": "single",
        "inmate_language": "english",
        "date": "YYYY-MM-DD",
        "case_id": 00001,
        "assessment_id": 00001,
        "agency_text": "pretrial",
        "supervision_level": 2,
        "supervision_level_text": "medium",
        "violence_score": 3,
        "violence_score_text": "low",
        "recidivism_score": 6,
        "recidivism_score_text": "medium",
        "fail_to_appear_score": 8,
        "fail_to_appear_score_text": "high",
        "type": "new"
    },  
    "... and thousands more ..."
]
```
To grab an individual assessment, use `https://data.pengra.io/compas/<assessment_id>`.

## Data Source:
Freedom of Information Act let me obtain a CSV containing these values. I simply converted it to an API for future use. Some data had to be cleaned before becoming an API endpoint.
