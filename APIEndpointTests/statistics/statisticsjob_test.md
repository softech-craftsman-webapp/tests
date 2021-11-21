# StatisticsJob



## URL
```
https://main-api.hiringo.tech/statistics/job
```



## Request
```
Request1:{GET /statistics/job HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjAxZDZkZWY4ODJhODFlYzQzMWE4YjIxNmUxZTNhZWFmYzJhMjY0YmY0NTM4MmZjYTBhZGVkZWIzNzgyZTJjNyJ9fSwiZXhwIjoxNjM3MDA0Mjk0LCJpYXQiOjE2MzcwMDMzOTQsIm5iZiI6MTYzNzAwMzM5M30.rz16jKF5D3FnDE0sOlgBcb0Ahqdgo3agdPt9jAzpIw1B93pXJZAF0wHs0pyf3WJiTVlIJ3Hv0gDfDB5AboFTBg
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7c732101-38ee-41e0-96d3-90606c3ea4f3
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```

```
Request2:{GET /statistics/job1111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjAxZDZkZWY4ODJhODFlYzQzMWE4YjIxNmUxZTNhZWFmYzJhMjY0YmY0NTM4MmZjYTBhZGVkZWIzNzgyZTJjNyJ9fSwiZXhwIjoxNjM3MDA0Mjk0LCJpYXQiOjE2MzcwMDMzOTQsIm5iZiI6MTYzNzAwMzM5M30.rz16jKF5D3FnDE0sOlgBcb0Ahqdgo3agdPt9jAzpIw1B93pXJZAF0wHs0pyf3WJiTVlIJ3Hv0gDfDB5AboFTBg
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 37fbc492-8b1e-47b7-8261-3d464b35f367
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```

```
Request3:{GET /statistics/job HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: ad9c8986-348a-4597-a45d-aa1dc7cb90db
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```




## Response
```
Response1:{HTTP/1.1 200 OK
Date: Mon, 15 Nov 2021 19:10:32 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=jgLzEjJH226DdkrI%2FMoj3VHLpmg5e2jP%2Bro%2BYDspqYL%2FGLp68ecCpwqf0ABlhFXiLdWeILqZ1UMS6%2BmLoBz8h%2F4hisbdhaoOLhBYR6DRVKW%2FuVtp8shLQI79u%2FzvK33gjLHPdp5TJC8%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeac7bbab1f5b44-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"total":13,"user_job_count":4,"latest_job":{"id":"2ef792f1-720a-4822-abdd-bcde4804cf60","user_id":"","name":"","description":"","image":"","valid_until":"0001-01-01T00:00:00Z","is_premium":false,"is_equipment_required":false,"category_id":"","transaction_id":"","latitude":0,"longitude":0,"distance":0,"is_contract_signed":false},"time":"0001-01-01 00:00:00"}}
}
```

```
Response2:{HTTP/1.1 404 Not Found
Date: Mon, 15 Nov 2021 19:12:23 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=%2F9hrJiuabgmvu9vU9M5NLtNDKwAIiVBcL%2FnuzljHzErseufkBaVsga2W3zuxhSMnO6W9FMAHMKYboayn0uHQdALqT%2ByprRXFvflV2nbnLqTbLdFYk6SqVnM7NYrbR7l5%2BIuAIOx8Los%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeaca735b1e5b44-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```


```
Response3:{HTTP/1.1 401 Unauthorized
Date: Mon, 15 Nov 2021 19:13:05 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=ybqxogpCWK3ceHehE93zo7SpJb83nZJi1Wk5Ew4wbjeU2f0RTG49eM%2FXa5YszCiiQr53FUsOcOL2wKBaX71BdUgUisXEU35DCsQb8bLh6rI8032Lj6jHKdNEIS08A%2BYWaq9Um0lJznE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeacb77e93f5b44-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```





## Results
Success