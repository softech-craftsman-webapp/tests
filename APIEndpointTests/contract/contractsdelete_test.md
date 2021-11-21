# ContractsDelete



## URL
```
https://main-api.hiringo.tech/contracts/{id}
```

## Request
```
Request1:{DELETE /contracts/a2f7e77b-ca28-474b-8b8d-006b0bf61a42 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiYjJkYzFmMmViNjg3MTI3NmMxMzNlNGI5OGNhMGExMTg0ZGVlMTFlM2I4ZmJkM2E4Zjg0ODhkNzQxYzQyYmM4ZCJ9fSwiZXhwIjoxNjM3MzY0MTc3LCJpYXQiOjE2MzczNjMyNzcsIm5iZiI6MTYzNzM2MzI3Nn0.vXYQhhpLF7uhq1PkLujZUPUrUKLOqWV0REY-gVvWVT-Zx33sBiz2xRdqFffU7bLEzqX9N8u40dlIkcBlTWpfeQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 236b5da5-559b-4e7d-b575-75ca9c5e57da
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
}
```

```
Request2:{DELETE /contracts/aaa HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiYjJkYzFmMmViNjg3MTI3NmMxMzNlNGI5OGNhMGExMTg0ZGVlMTFlM2I4ZmJkM2E4Zjg0ODhkNzQxYzQyYmM4ZCJ9fSwiZXhwIjoxNjM3MzY0MTc3LCJpYXQiOjE2MzczNjMyNzcsIm5iZiI6MTYzNzM2MzI3Nn0.vXYQhhpLF7uhq1PkLujZUPUrUKLOqWV0REY-gVvWVT-Zx33sBiz2xRdqFffU7bLEzqX9N8u40dlIkcBlTWpfeQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 0f7940d3-507f-4473-9c23-20ab01e6d86d
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```

```
Request3:{DELETE /contracts/ HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiYjJkYzFmMmViNjg3MTI3NmMxMzNlNGI5OGNhMGExMTg0ZGVlMTFlM2I4ZmJkM2E4Zjg0ODhkNzQxYzQyYmM4ZCJ9fSwiZXhwIjoxNjM3MzY0MTc3LCJpYXQiOjE2MzczNjMyNzcsIm5iZiI6MTYzNzM2MzI3Nn0.vXYQhhpLF7uhq1PkLujZUPUrUKLOqWV0REY-gVvWVT-Zx33sBiz2xRdqFffU7bLEzqX9N8u40dlIkcBlTWpfeQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: ab689b0e-585e-4ef0-a172-8aa8438557e8
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```
```
Request4:{DELETE /contracts/e5d43103-d707-48f4-bc3b-a5578a93cb58 HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 9cccfbeb-4d9c-4d23-b3a9-da2f3b35cf62
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```




## Response
```
Response1:{HTTP/1.1 200 OK
Date: Fri, 19 Nov 2021 23:10:08 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=n%2BcLPDFggVcEnO2T6iavwmVodOGAh0cL0Nc9fSfkzje%2F2qKBWpM9z8pYy%2BxmDfv7c3Uhnn65cjuQfKiF0BC9PSodUQGgIRJjxTjKLnc8uMyjhbfAg6%2BAcgiBI0jQWn%2F%2FvzwGxKV4eiE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6b0d1c34edd67031-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"a2f7e77b-ca28-474b-8b8d-006b0bf61a42"}}
}
```

```
Response2:{HTTP/1.1 500 Internal Server Error
Date: Fri, 19 Nov 2021 23:15:16 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=8eeLy4i4dR23cAh8X7f5tz%2F%2B1RqarWcJC1E50C%2Bd053JWpoiYgWUey6L2Jqe1zhht0E4lSm4rc2Ufv4nIeklOmFFNOafabCGnKv3nGhwKnbUJAkQrOaIfcJwDl6jIRcX6g%2Bi9SW2cDk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6b0d23bb3d8d7031-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"aaa\" (SQLSTATE 22P02)","payload":null}}
```

```
Response3:{HTTP/1.1 404 Not Found
Date: Fri, 19 Nov 2021 23:17:01 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tVSB5Ijdrlb2fwaMqQkxuGp9WzOTTLfYxQ0V0%2F11NHvGsm5AAXoEc7iVV456UJ14LBgVyfxGt3wTBnnabtbyycsMBHbmCeC3%2Bssk4VRIJjycvNPwugG1878RqPfe2gVgcuHGPWLZ96Y%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6b0d264dbd4a7031-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```

```
Response4:{HTTP/1.1 401 Unauthorized
Date: Fri, 19 Nov 2021 23:19:47 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=l8KxbcA3uLKbXy%2BPa%2BR5IurLHtpd8f2xRmM61tRCluvGO%2Fp7V1HE2EVXvX4aaOGeMsdeCIS9vDtCumHMS1t4z7mYQDB8hOxY8ocWfz8yHfDKprWIqdqnqsBm%2FQk2%2FXj0mebtSIfLj6U%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6b0d2a5b9a9a7031-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}
}
```


## Results
Success