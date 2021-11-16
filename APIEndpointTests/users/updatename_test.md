url:{https://auth.hiringo.tech/users/{id}/update-name}




Request Headers1:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-name HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTY6NDI6MjMuODgwODI1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzk0ODMwOTkwYWY5YjZjMGE2MjE1NTdlZWQxYjM1ZWUyMTM5MDkyNjI4NTg1MjhkMjg5ZTAwMzE2Nzk5Zjg0MiJ9fSwiZXhwIjoxNjM2NzM5MjE2LCJpYXQiOjE2MzY3MzgzMTYsIm5iZiI6MTYzNjczODMxNX0.5r1_Sg0f2urAH3H7XkswSutOqwlrvlcKfO6gkFLtQXPD90I5C933esstvXeApOeSw3UD--22MzaOTsy86f7Zlw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: d988b1a1-ba78-4619-a05a-24917017da49
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 48}



Request Body1:{{
"name": "Rachel",
"password": "qwaezsxd"
}}




Response1:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 17:33:31 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=aB%2B9V9ogHwz59klkkrd7O1HyN5KF%2FwUBX9KSf00DWV50zVGB6UgZsDC7l8Ox6CyKMM0%2BeavVnZDOAgozL3bmSvD9fixKAJ4TAW7gqP1m4aRaQCgG3TkuGJuj8CKQKj7ljiVttQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad1817c2a6c702d-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60"}}}






Request Headers2:{PUT /users/%7B%7D/update-name HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTY6NDI6MjMuODgwODI1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzk0ODMwOTkwYWY5YjZjMGE2MjE1NTdlZWQxYjM1ZWUyMTM5MDkyNjI4NTg1MjhkMjg5ZTAwMzE2Nzk5Zjg0MiJ9fSwiZXhwIjoxNjM2NzM5MjE2LCJpYXQiOjE2MzY3MzgzMTYsIm5iZiI6MTYzNjczODMxNX0.5r1_Sg0f2urAH3H7XkswSutOqwlrvlcKfO6gkFLtQXPD90I5C933esstvXeApOeSw3UD--22MzaOTsy86f7Zlw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a795200e-562a-45b9-ba87-d84d8feef482
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 48}





Request Body2:{{
"name": "Rachel",
"password": "qwaezsxd"
}
}




Response2:{HTTP/1.1 403 Forbidden
Date: Fri, 12 Nov 2021 17:36:34 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=rXCuOeaU7iJ4mk0wpb6Z8Giivvkhll4jYAYPGdC%2FAcaIhbiatRvyp3Y00alueCe5LrvpYwf2JyjzU4IKTsPssNUSH8T%2FyeY80WwcQHn%2Bq%2B3E4Ly5aaIGmYAoR4L5HScnpSxzWA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad185f4fcf9702d-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}






Request Headers3:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-name111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTY6NDI6MjMuODgwODI1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzk0ODMwOTkwYWY5YjZjMGE2MjE1NTdlZWQxYjM1ZWUyMTM5MDkyNjI4NTg1MjhkMjg5ZTAwMzE2Nzk5Zjg0MiJ9fSwiZXhwIjoxNjM2NzM5MjE2LCJpYXQiOjE2MzY3MzgzMTYsIm5iZiI6MTYzNjczODMxNX0.5r1_Sg0f2urAH3H7XkswSutOqwlrvlcKfO6gkFLtQXPD90I5C933esstvXeApOeSw3UD--22MzaOTsy86f7Zlw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 12d78d13-0fb4-4040-a098-ed9056cc8721
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 48}




Request Body3:{{
"name": "Rachel",
"password": "qwaezsxd"
}}




Response3:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 17:44:35 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Sde%2F1tvrIXs%2F26cdkvV9%2FlVUVq%2F9a2yr9chXSjwA0WCyLui54%2BQqq5C5uAKGDIkq7PmSXI%2BjjF%2F%2Bjh2AEk0PUdzdbBcduEdsB5ds7sBvjLlkoyGe7rAwqdiNOqQPXVRfi7R9kw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad191b50e37d6b1-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=crypto/ecdsa: verification error","payload":null}}






Request Headers4:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-name HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTg6MzM6MzEuNTI3Njg1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiM2MyMGIwNDIzYjg5OTU4MWE2ZDM0YjVjOTIzMjVjYTY3NjBiMmY2YWYwNzU2NTMyNjhmYzdlNGI1MGMwODQyMSJ9fSwiZXhwIjoxNjM2NzQwMjkwLCJpYXQiOjE2MzY3MzkzOTAsIm5iZiI6MTYzNjczOTM4OX0.0e74iHm1BWklhOyxqjcuf__Gmgw7Rtq9B4b8FWMCWn4lRNQKYGsTj18OkGGu_meOf8he9ay1bc5lXJpOwBGfxw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 9cb24a52-43cd-4a2a-9d0d-5aa2908c9468
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 6}




Request Body4:{
{
}}




Response4:{HTTP/1.1 400 Bad Request
Date: Fri, 12 Nov 2021 17:50:17 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=L%2BtAAA5twMHFWgHWsV73JkGAb7DXHVQXmQ3BkHMPYb2ChDGHIS0DxMMgQKPPoJcHjf%2FkhwQYkXDLjnSMS%2FQBB3AW9MgiCY0NS0OzhBS%2FjedAtaElXL%2BH%2BzJrX0PeA9aWaiWlzQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad19a0c0d91d6b1-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Key: 'UpdateNameRequest.Name' Error:Field validation for 'Name' failed on the 'required' tag\nKey: 'UpdateNameRequest.Password' Error:Field validation for 'Password' failed on the 'required' tag","payload":null}}





Request Headers5:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-name HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTg6MzM6MzEuNTI3Njg1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiM2MyMGIwNDIzYjg5OTU4MWE2ZDM0YjVjOTIzMjVjYTY3NjBiMmY2YWYwNzU2NTMyNjhmYzdlNGI1MGMwODQyMSJ9fSwiZXhwIjoxNjM2NzQwMjkwLCJpYXQiOjE2MzY3MzkzOTAsIm5iZiI6MTYzNjczOTM4OX0.0e74iHm1BWklhOyxqjcuf__Gmgw7Rtq9B4b8FWMCWn4lRNQKYGsTj18OkGGu_meOf8he9ay1bc5lXJpOwBGfxw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 576360b6-4a7c-4373-b40f-555e5e34a2ee
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 48
}




Request Body5:{{
"name": "Rachel",
"password": "qwaezsxd"
}
}




Response5:{HTTP/1.1 500 Internal Server Error
Date: Fri, 12 Nov 2021 17:57:32 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=bumj6aiSx8IPnUgrB%2FDWNK%2FYMrarWklSwX8DftqM%2F%2F8NK%2FICA%2FKAH5%2FFmZCLPqiM2pHzpdsGrtvTGuNLkNZ4Wg30ErvEVX73JW6qzL1VSXKUIExPwPw%2FsSdxN%2FEqRsTDW6c%2Bhg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad1a4abcf71d6b1-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}
