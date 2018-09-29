# Broward County COMPASS data
// Written on **September 29th, 2018**

This is an API that hosts the dataset of Broward County

## Notable Lab
I wrote a lab about this dataset: [Naturally Occurring Racial Bias in AIs](https://pengra.github.io/labs/compass_analysis)

## Response Format
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

## Data Source:
Freedom of Information Act let me obtain a CSV containing these values. I simply converted it to an API for future use.
