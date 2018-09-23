# Geographic Location by IP
// Written on **September 23rd, 2018**

Pretty self explanatory. Suppose you're interested in the IP address: `127.0.0.1`

## Response Format
Use curl or requests to hit [https://data.pengra.io/geoip/127.0.0.1](https://data.pengra.io/geoip/127.0.0.1). 
Responses will always be in JSON in the following format:

```json
{
    "IP": "127.0.0.1",
    "continent": null,
    "country": null,
    "region_code": null,
    "region_name": null,
    "city": null,
    "zip": null,
    "latitude": null,
    "longitude": null,
    "language": null
}
```

## Data Source:
[Ipstack](https://ipstack.com/) provides the initial data, and then it is cached.
