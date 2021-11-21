# StatisticsTransaction



## URL
```
https://main-api.hiringo.tech/statistics/transaction
```



## Request
```
Request1:{GET /statistics/transaction HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZjYwZWZiNjQ3NGM3MjcyYmIzOTBiZDQyMDM4Nzg0MWI3ZjQzZjJkOGIyOWFhOTIwNjBkNGRkNzU2YWIyYmU4ZSJ9fSwiZXhwIjoxNjM3MDA0NjM5LCJpYXQiOjE2MzcwMDM3MzksIm5iZiI6MTYzNzAwMzczOH0.qdR8qQGC1HOM20DxUcBfMTiOLiRLZfxWPjZswzIS-7KMn0mqnSihkPoGJQDWBAM3X4cpkTBRpq_lDWeZEnu0HA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 124b495d-4f7c-4e18-b28f-e1df620f84d1
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


```
Request2:{GET /statistics/transaction1111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZjYwZWZiNjQ3NGM3MjcyYmIzOTBiZDQyMDM4Nzg0MWI3ZjQzZjJkOGIyOWFhOTIwNjBkNGRkNzU2YWIyYmU4ZSJ9fSwiZXhwIjoxNjM3MDA0NjM5LCJpYXQiOjE2MzcwMDM3MzksIm5iZiI6MTYzNzAwMzczOH0.qdR8qQGC1HOM20DxUcBfMTiOLiRLZfxWPjZswzIS-7KMn0mqnSihkPoGJQDWBAM3X4cpkTBRpq_lDWeZEnu0HA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7ce60d7b-06c6-4f29-802a-1cc648171f5f
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


```
Request3:{GET /statistics/transaction HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 06be7217-7348-417f-a174-95c8fe0da9c9
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```





## Response
```
Response1:{HTTP/1.1 200 OK
Date: Mon, 15 Nov 2021 19:16:02 GMT
Content-Type: application/json; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
content-security-policy: default-src 'self' 'unsafe-inline'
strict-transport-security: max-age=3600; includeSubdomains
vary: Accept-Encoding
vary: Origin
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Zm2vObL4rMP1%2B1rktoVLlGvIuzmuPeo6%2Bn%2BazRffWqaj5bOPRB4XqLNrOsSE9%2B1vQtlDjFvfeVlvUhcJdCnA2SnbF28lENOz5ZwelXgbguPZuIT8q9FZwvOz%2BpdNYWsFWO1Mia%2FEyv0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeacfc6e8b65b44-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"total":37,"user_transaction_count":11,"latest_transaction":{"id":"6d22750e-ab5f-482d-a5b0-e24dbec297c4","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":900,"currency":"EUR"},"time":"2021-11-13 21:54:30"}}}
```


```
Response2:{HTTP/1.1 404 Not Found
Date: Mon, 15 Nov 2021 19:17:35 GMT
Content-Type: application/json; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
content-security-policy: default-src 'self' 'unsafe-inline'
strict-transport-security: max-age=3600; includeSubdomains
vary: Accept-Encoding
vary: Origin
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tWV0W%2FhWY6OSziFTZc%2Fz9GAYSfoQmbZn6St0R75eE%2FqlmstcA7fidLKFuqqv%2FW6rAox%2BLk5PAoUFJkKtYGLFOUn98fBxSImERWLhjNB0T2gb3qqJar1CEA5Kbt7K1AQk5Yk%2FUJ72W34%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aead21328495b44-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```


```
Response3:{HTTP/1.1 401 Unauthorized
Date: Mon, 15 Nov 2021 19:18:06 GMT
Content-Type: application/json; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
content-security-policy: default-src 'self' 'unsafe-inline'
strict-transport-security: max-age=3600; includeSubdomains
vary: Accept-Encoding
vary: Origin
x-content-type-options: nosniff
x-frame-options: SAMEORIGIN
x-xss-protection: 1; mode=block
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=nnRSBiaJJEA9H9Ud6jDWwv3RGvmfb90QzchqBoxU3I887eRnPf2p9%2FMN%2FIX7pOBeeloI63Zoj9vAvMQmrsjWjfOSMbInc4q7%2BCgfHE3yOp9%2FGxdiPaQ3UBltAXCFIvuZn4QqrqsZuSk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aead2d3ad6b5b44-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```





## Results
Success