# Login


## URL
```
https://auth.hiringo.tech/auth/login
```

## Request
```
Request Headers1:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 8291fad4-75a4-4261-a7bb-15a6a810cf1e
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}

Request Body1:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}
```

```
Request Headers2:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: d9029ea1-1696-4dda-b9bb-d6682053ba2f
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 56
}


Request Body2:{{
"email": "x@gmail.com",
"password": "qwaezsxd12"
}
}
```



## Response
```
Response1:{
Date: Wed, 10 Nov 2021 18:46:46 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=3jv0N1x6OisXvlI5R%2BP%2Ff%2Fr%2F0DwjcqXb3kBsr9stG%2F%2FR0UOrLT%2B18lLzrpSZBXqj4nIEsm1cdu5sZpION5%2FalOa2ul6lzkfxjGcLMFVRNBR%2BsghnM00U6gVwOpPsvC7uX3vIJg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ac1720a58c12c4a-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiN2U3ODlkNGRlYTMwNTc5ZmJiYjI4N2VlM2FlN2VkOTMzODg4NzcxN2Y0NWU4MDkzYzdiNGM3MDM5MmFmMTk5MCJ9fSwiZXhwIjoxNjM2NTcwOTA2LCJpYXQiOjE2MzY1NzAwMDYsIm5iZiI6MTYzNjU3MDAwNX0.bveqbkjbbuW8jrGVVlBThfLgXsFYPLUtHUs5NZU5daxbKkhQTcpQ7dq-Ak47BN1EPxm4LhlmdF-XlvOSe5tS9A","token_expiration":1636570906,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiN2U3ODlkNGRlYTMwNTc5ZmJiYjI4N2VlM2FlN2VkOTMzODg4NzcxN2Y0NWU4MDkzYzdiNGM3MDM5MmFmMTk5MCJ9fSwiZXhwIjoxNjM5MTYyMDA2LCJpYXQiOjE2MzY1NzAwMDYsIm5iZiI6MTYzNjU3MDAwNX0.Yj6mTGF4i1KucfSO1wMjM54ddLCvxMJbBDSUN6biFwZhJWvYq78eVl3MdyKGMUROMp6Er9QGlcTLFjR3oj0tqg"}}}
```




```
Response2:{
HTTP/1.1 400 Bad Request
Date: Thu, 11 Nov 2021 16:22:56 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=JCedRengo%2BhNLCIBuKzplus9U7OFBLcoBycEVBUZrC0HoqLhrW6YgdjmvyHCvj2Lhy960ImmjftXtr3JtXGeLnwO9I333kkkTopA5RfFX4CK2tx8xoqd3cVYvRODMehYhHV6%2Bw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ac8dcba7e85430f-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Email or password is invalid","payload":null}}
```



## Result
Success
