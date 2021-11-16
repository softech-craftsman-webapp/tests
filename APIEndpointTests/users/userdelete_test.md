url:{https://auth.hiringo.tech/users/{id}}



Request1:{DELETE /users/%7Bid%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMjZlZWE3YWVlM2M5NjM5ZWE0ZWZkZjczN2NlMGRlZmY5ZTY3MzgyM2RmZDMxNTliNjlmNzY1YTU2ZTc4Y2ZkNiJ9fSwiZXhwIjoxNjM2NzYxODk5LCJpYXQiOjE2MzY3NjA5OTksIm5iZiI6MTYzNjc2MDk5OH0.GEMpbnwzuyvl0qu0E0JEguZL1C5QK5zjb22yINHuNulT7d-ZRgORpHcAHL-91AdxFq0plXWFIU1Ed09bHjnrMQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1cad3f4e-1800-486b-a0a2-0f07397327ce
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response1:{HTTP/1.1 403 Forbidden
Date: Fri, 12 Nov 2021 23:50:38 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tUsY9GPCC9u0IBOeMdRgVqlexiI%2B7MmnKLsn854g3gUxaT7jUr6rpxUVnBSXdvVmM9VhUdhulXYPelznaUWtBhcFLyXw%2Bf93XritR7AAoM7ptBlHA4KE3mrAxwhRGX2K95Mupw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad3a9e71d3542e7-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}






Request2:{DELETE /usersss/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMjZlZWE3YWVlM2M5NjM5ZWE0ZWZkZjczN2NlMGRlZmY5ZTY3MzgyM2RmZDMxNTliNjlmNzY1YTU2ZTc4Y2ZkNiJ9fSwiZXhwIjoxNjM2NzYxODk5LCJpYXQiOjE2MzY3NjA5OTksIm5iZiI6MTYzNjc2MDk5OH0.GEMpbnwzuyvl0qu0E0JEguZL1C5QK5zjb22yINHuNulT7d-ZRgORpHcAHL-91AdxFq0plXWFIU1Ed09bHjnrMQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a4725a1a-4294-4519-bafe-b20d022d2a11
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}





Respone2:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 23:52:35 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=l1KVFTksP%2BfiK2ErQnF6faK9KpCZjuroMNI%2B3KUAfuFfeUPtTRwKKvvB3Rce99UEEYq6iLG98praRqJEnPfWAy6tAImbBi7wW3%2Fkj12Cmr60NCs%2BMXeEX%2FMKgGzUcfC6261cPw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad3acc41f4942e7-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=crypto/ecdsa: verification error","payload":null}
}






Request3:{DELETE /users/a606969b-206c-4b30-a6bd-22733d4483d8 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiYTYwNjk2OWItMjA2Yy00YjMwLWE2YmQtMjI3MzNkNDQ4M2Q4IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxN0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDdUMTE6Mzg6MjcuMzY5NDQ2KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMDdUMTE6Mzg6MjcuMzY5NDQ2KzAxOjAwIiwiYXV0aCI6eyJpZCI6IjI2NTFkODJhLTZmNDQtNDEzNC1iN2NkLTUyMThhMDY4NTAxMyIsInRva2VuIjoiOWE0MzZlZGZjYTc0N2M1NWQwZGI0YmQ3YmQ2MWNjZGJmN2E3NTA2Y2MzOTYwOWViN2Y5OGUyNWM3MWM2YWNkZCJ9fSwiZXhwIjoxNjM2ODA5OTI5LCJpYXQiOjE2MzY4MDkwMjksIm5iZiI6MTYzNjgwOTAyOH0.eajiUYfHEXtbgVhtjTEShuSp5aeDuMxh9wPkS3YyZ-Cild5Hgc2d6euYpXadnZ-I-Pl-5PpsgkQzoDYCFsXA_g
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 530d682b-65af-4800-846a-38e52be89a98
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}




Response3:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 13:11:32 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=k7kHmwCAkVWlD7LLwsceh99gHiE1x4loIPKbYDisTrDjRPbnmKsXY%2FWS3JIJREIXEHm2gS0PAGr9cRbt8NFBr%2BuuyeRS3Gd1w5ToVq28e02nsZe1rvEPV1cLgkDJxOIIozimhA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad83f188d450601-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"a606969b-206c-4b30-a6bd-22733d4483d8"}}
}







Request4:{DELETE /users/768653f2-e9cf-48e7-ac5c-7c3350907827 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZDg1OTYwMTcyZDVjMTMwYmRhM2M1Y2M3MWEyMmZkNTk2NzQwOTk1NzkyZjg0YWVjMDY3NjJjMjVhNDg0ZWI4MSJ9fSwiZXhwIjoxNjM2ODE5OTIwLCJpYXQiOjE2MzY4MTkwMjAsIm5iZiI6MTYzNjgxOTAxOX0.7z4H64ULgBbPgjtdmgC8Em37c8na5ge61q81EKKSQIueZtpCBs6lVmXoeO-pzIBup_ibtXU5PwNBJC-4x_WPvw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: c704026d-01e5-4dfd-840a-a6930b2490c0
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}




Response4:{HTTP/1.1 500 Internal Server Error
Date: Sat, 13 Nov 2021 15:58:14 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=AR%2Be88R56spUK53R%2BhMec%2F3qY%2Ba6DF6GCs%2FRr96rdVgvQ8%2BR0pVXS7%2FiKd5a4YP0H4o99QiufgQhtb951UCEZXtPkiQYuOjE1SIR2%2Bky1s1LrmK%2FBlYnggtjWlSYID%2F9LXJrTA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad9334c0f820631-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}