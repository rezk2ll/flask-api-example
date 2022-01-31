# flask-api-example

## how to run

```bash
docker-compose up -d
```

service should be running on http://localhost:5000

## how to use

#### using GET:

send a get request to `/clean/:text` endpoint, example:

```
http://localhost:5000/clean/euh some text with euh 
```

#### using POST:

send a POST request to `/clean` endpoint with a `text` in the request body:

```json
{
  "text": "euh some text with euh"
}
```
