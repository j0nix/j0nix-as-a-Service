# j0nix-as-a-Service
* What would j0nix have said?
* as a REST API for my collegues to utilize when I change job.
## GET ALL
```
[GET] http://localhost:8080/
[GET] http://localhost:8080/wisdoms
```
## ADD NEW
```
[POST] http://localhost:8080/wisdoms?msg={url-encoded-text}
```
## GET SPECIFIC 
```
[GET] http://localhost:8080/wisdoms/{id}
```
## UPDATE
```
[PUT] http://localhost:8080/wisdoms/{id}?msg={url-encoded-text}
```
# DELETE
```
[DELETE] http://localhost:8080/wisdoms/{id}
```
