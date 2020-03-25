# j0nix-as-a-Service
* What would j0nix have said?
* as a REST API for my collegues to utilize when I change job.
## GET ALL
```
[GET]   http://<url>:8080/
[GET]   http://<url>:8080/wisdoms
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
