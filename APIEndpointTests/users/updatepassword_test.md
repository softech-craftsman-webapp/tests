##UpdatePassword



##Url
{https://auth.hiringo.tech/users/{id}/update-password}



#Request
Request Headers1:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-password HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTg6MzM6MzEuNTI3Njg1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYzI3NzdiYmY4YjdjZmVlZDdkOTM5ZGMyMDRkMmQ3OWIyNTBjNThiMjEwN2U3ODk0MGIwOTA0NTc2NjA3ZjIzNiJ9fSwiZXhwIjoxNjM2NzUxMDc1LCJpYXQiOjE2MzY3NTAxNzUsIm5iZiI6MTYzNjc1MDE3NH0.tV3RR4ky1cbp58HaSHR9hk9fMdd25gAt4x88UCGJW9AASjNDkAGh3eOR6zZMpF3Yc38ZlU5ytiUVv9BXseczGA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: af5c945e-59aa-4f62-86e4-07a1d9834cbb
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 63}



Request Body1:{{
"old_password": "qwaezsxd12",
"password": "qwaezsxd123"
}
 }




Request Headers2:{PUT /users/%7Bid%7D/update-password HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTg6MzM6MzEuNTI3Njg1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYzI3NzdiYmY4YjdjZmVlZDdkOTM5ZGMyMDRkMmQ3OWIyNTBjNThiMjEwN2U3ODk0MGIwOTA0NTc2NjA3ZjIzNiJ9fSwiZXhwIjoxNjM2NzUxMDc1LCJpYXQiOjE2MzY3NTAxNzUsIm5iZiI6MTYzNjc1MDE3NH0.tV3RR4ky1cbp58HaSHR9hk9fMdd25gAt4x88UCGJW9AASjNDkAGh3eOR6zZMpF3Yc38ZlU5ytiUVv9BXseczGA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 63cca6d9-7c61-449a-a5ec-b56674a06147
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 63}


Request Body2:{{
"old_password": "qwaezsxd12",
"password": "qwaezsxd123"
}}




Request Headers3:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-password1111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiOTdiZTQxZjNkMGI4ODdjNDc0YTJiNzBhYTMwNWVhOTU3ODA2NDljZDQyOTg0ZGYwMDRlMTIzNmNhMmE5MWQ3ZCJ9fSwiZXhwIjoxNjM2NzUyMDgzLCJpYXQiOjE2MzY3NTExODMsIm5iZiI6MTYzNjc1MTE4Mn0.lWk0quhjFtLVB0zj8KMD3TI6H2zVJscbe343uhH-tNc8PS_1DyNyrjqLadSvivVQecyUugmUm-GhZc-xXXYM0g
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 569bbf34-a128-466b-a54b-a7a3e44dffb2
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 63}



Request Body3:{{
"old_password": "qwaezsxd12",
"password": "qwaezsxd123"
}}




Request Headers4:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-password HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiOTdiZTQxZjNkMGI4ODdjNDc0YTJiNzBhYTMwNWVhOTU3ODA2NDljZDQyOTg0ZGYwMDRlMTIzNmNhMmE5MWQ3ZCJ9fSwiZXhwIjoxNjM2NzUyMDgzLCJpYXQiOjE2MzY3NTExODMsIm5iZiI6MTYzNjc1MTE4Mn0.lWk0quhjFtLVB0zj8KMD3TI6H2zVJscbe343uhH-tNc8PS_1DyNyrjqLadSvivVQecyUugmUm-GhZc-xXXYM0g
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: fa6a3b0b-500c-4cb4-a4df-2543e50e3a76
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 6}



Request Body4:{{
}}





Request Headers5:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-password HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiOTdiZTQxZjNkMGI4ODdjNDc0YTJiNzBhYTMwNWVhOTU3ODA2NDljZDQyOTg0ZGYwMDRlMTIzNmNhMmE5MWQ3ZCJ9fSwiZXhwIjoxNjM2NzUyMDgzLCJpYXQiOjE2MzY3NTExODMsIm5iZiI6MTYzNjc1MTE4Mn0.lWk0quhjFtLVB0zj8KMD3TI6H2zVJscbe343uhH-tNc8PS_1DyNyrjqLadSvivVQecyUugmUm-GhZc-xXXYM0g
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 3e6cb306-fcff-4fcd-8b08-5852b17d3ab8
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 63}



Request Body5:{{
"old_password": "qwaezsxd12",
"password": "qwaezsxd123"
}}



##Response

Response1:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 20:52:31 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=K0wPwaTgKEpi6EiLr7p%2F1N1vhmO27RLO8LEBtGTQYtUduIfTazP%2BaFwrct4eIU%2BSsi6aEddU42B%2FukTizr8O5reRKCxeVA8ACmlhV7TB03uFjYH%2BzYJ5bj8BknKzbbB0CQw5yQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad2a4fb9f9268fd-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60"}}}





Response2:{HTTP/1.1 403 Forbidden
Date: Fri, 12 Nov 2021 20:57:12 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=ISuHbN2BgixUjlmwsFlCQoyvw%2Fk8iq6K7KukjkaEnXW19QsbBpOZSz7Dn2yMIJs9jD5gHV9XHjS%2F12ELrOiTGzMw7QHAl2ESxYDGP5c9hHY2vWKom0pAv0VK8VbsU7hwREodWw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad2abdaec8868fd-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}





Response3:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 21:06:39 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=jJIggb%2Fpo%2BrLLdvqVpMnEzxYAQOaAQMf4654oTIc0O3YTwQe%2FspiU4q5zaHVythebyc2n6gYI71PlTkGn%2FG4c2PqdxvY6%2Flb%2FkD4GjMb8UgT7j66bi71XOTxERXTrVHogmCTrQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad2b9b5cfe1dfc3-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=crypto/ecdsa: verification error","payload":null}
}



Response4:{HTTP/1.1 400 Bad Request
Date: Fri, 12 Nov 2021 21:10:51 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=FplBvrTQGP5jw76djJzh8mBH5XB4Gd2kMCrDFAHR2f%2FYcQ3nM5fNIXYEuRby8vsUDv8AfhYBZ2gfCEi1ofNs9rz4YkYjyFF0ZaOig6AAySEwgbb4KhojCz7HgcNs7GLhdc3xng%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad2bfdaec5edfc3-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Key: 'UpdatePasswordRequest.OldPassword' Error:Field validation for 'OldPassword' failed on the 'required' tag\nKey: 'UpdatePasswordRequest.Password' Error:Field validation for 'Password' failed on the 'required' tag","payload":null}
}



Response5:{HTTP/1.1 500 Internal Server Error
Date: Fri, 12 Nov 2021 21:13:19 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=trN1jG5wMbaY%2F5e49gZlLC2ZLhNdlcL%2B29NNUIrWd1MlEB42SVrPpDtfcOMpi%2B7oes8WgCjiZuOugSZ7uM%2Br3CUNOnaHZDIhQrbLaxHl0bf5VEgG3MVRZu3TWtAe%2Bbhm%2Bh2ppA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad2c3773e87dfc3-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}





##Results
Success
