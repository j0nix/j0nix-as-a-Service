# j0nix-as-a-Service
* What would j0nix have said?
* as a REST API for my collegues to utilize when I change job.

# HOWTO
```
python app.py
```
- If database is not present, one is created.
- Dockerfile & kubernetes deployment example included in repository
```
docker build . -t jaas:latest
docker run -d -p 8080:8080 jaas:latest
```

## GET ALL
Get all entry:s in database
```
[GET]   http://<url>:8080/
[GET]   http://<url>:8080/wisdoms
```

## GET RANDOM
Get a random entry from database
```
[GET]   http://<url>:8080/random
```
# CRUD
## CREATE
```
[POST]    http://<url>:8080/wisdoms?msg={url-encoded-text}
```
## READ
```
[GET]     http://<url>:8080/wisdoms/{id}
```
## UPDATE
```
[PUT]     http://<url>:8080/wisdoms/{id}?msg={url-encoded-text}
```
## DELETE
```
[DELETE]  http://<url>:8080/wisdoms/{id}
```
