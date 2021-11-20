##Register



##Url:{https://auth.hiringo.tech/auth/register}



##Request

Request Headers1:{POST /auth/register HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzAyZjRkY2Q2OWVkYWU3MzBhMjYzMDY1NDg0ODZmMDdiYzMxNDBmMzM1ZGNjM2I1YTU3YzI2YTc4YzdjYjk3MSJ9fSwiZXhwIjoxNjM2MjgxNzA4LCJpYXQiOjE2MzYyODA4MDgsIm5iZiI6MTYzNjI4MDgwN30.WNNehwtwzuEocNqHvKTWtn0M-FqkLO1GFbcpNZQgtaZGymM8ChO3I3ySuHZ29ouNAD4FtNPPL0Gn3Ei5EAeMIw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 6a10e087-0fa5-44bd-afd0-85402488ae2f
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 76}


Request Body1:{{
  "email": "xxx17@gmail.com",
  "name": "xx",
  "password": "qwaezsxd12"
}}



Request Headers2:{POST /auth/register HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzAyZjRkY2Q2OWVkYWU3MzBhMjYzMDY1NDg0ODZmMDdiYzMxNDBmMzM1ZGNjM2I1YTU3YzI2YTc4YzdjYjk3MSJ9fSwiZXhwIjoxNjM2MjgxNzA4LCJpYXQiOjE2MzYyODA4MDgsIm5iZiI6MTYzNjI4MDgwN30.WNNehwtwzuEocNqHvKTWtn0M-FqkLO1GFbcpNZQgtaZGymM8ChO3I3ySuHZ29ouNAD4FtNPPL0Gn3Ei5EAeMIw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 8cf2e7a9-2329-4666-be35-ffca4f7b6d77
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 68}



Request Body2:{{
  "email": "xxx17@gmail.com",
  "name": "xx",
  "password": "&&"
}}





##Response

Response1:{
HTTP/1.1 201 Created
Date: Thu, 11 Nov 2021 17:24:05 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=j5TZ6fX8kOxkMxCxr2AaHFCttUbzUN36tW6oNgX26ruip2gvtnVwlNtQdsrfeDJMp3K0HJTiM9uDM1FzZwrlkkFNUauYWbvgd2QEyqgrRUuYHktpc5H%2FW5tKuHUfBstMCMrs9A%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ac9364dba70dffb-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: duplicate key value violates unique constraint \"users_email_key\" (SQLSTATE 23505)","payload":null}}



Response2:{
HTTP/1.1 400 Bad Request
Date: Thu, 11 Nov 2021 17:30:08 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=sFCBovY6e3LqCytIgmwZ27An6EAWlJmDc7R4LruIkkN6liI%2FZM%2BPTCk9VIqvVN64YmxhVLcwoOlO9BZOvXMnM7oPzHUA9pB%2BfGcr0NvdGZvdWsKfVnEoYWe3BxUJnB0fsdgg0w%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ac93f2a0fd8dffb-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Key: 'RegisterRequest.Password' Error:Field validation for 'Password' failed on the 'min' tag","payload":null}}





##Results
Success