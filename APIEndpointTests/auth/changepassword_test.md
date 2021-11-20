##ChangePassword


##url
{https://auth.hiringo.tech/auth​/change-password​/{token}}
https://auth.hiringo.tech/auth/login


##Request
Login Request Headers:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a5c28a00-1d2b-4dce-b5c2-19d303e6cc92
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}



Login Request Body:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Change Password Request Headers:{POST /auth/change-password/eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNWYzZDU1Nzc2NmEzYmQ1NGE4MzhlODkzNjVkOTdiMzA5Y2RjYmVhM2M4NjQyMjYxZGNkYjI2YzUwYmMyNjg0NSJ9fSwiZXhwIjoxNjM2ODk3MDYxLCJpYXQiOjE2MzY4OTYxNjEsIm5iZiI6MTYzNjg5NjE2MH0.5RSFRDv76o_MyR00T7vR_Hfzt5o1WSe2sV30IzBMPvnTU7ON5iSCNzzaCM6FlMNa6kPWVtUkCjj8fIjio7yw-A?email=xxxx@gmail.com HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 03ce1176-0497-4222-8c3e-035ce53c6832
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 36}



Change Password Request Body:{
{
"password":"qwaezsxd123"
}}



##Response
Login Response:{HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 13:22:41 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=zz6XUCruUbDkKGxjCM0KrvuLIhJUqEOkvGzKpVPJDTbpwq1kl%2BWgQLOXYJ5H4dZ%2B2dsHUfbW3qOn7J3%2FEmu9uTgSWYF9S1tYAGJ32FonaWo%2FKuWdYToF8pktoFeHIoPdDon2MA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae08cce2ce64a55-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNWYzZDU1Nzc2NmEzYmQ1NGE4MzhlODkzNjVkOTdiMzA5Y2RjYmVhM2M4NjQyMjYxZGNkYjI2YzUwYmMyNjg0NSJ9fSwiZXhwIjoxNjM2ODk3MDYxLCJpYXQiOjE2MzY4OTYxNjEsIm5iZiI6MTYzNjg5NjE2MH0.5RSFRDv76o_MyR00T7vR_Hfzt5o1WSe2sV30IzBMPvnTU7ON5iSCNzzaCM6FlMNa6kPWVtUkCjj8fIjio7yw-A","token_expiration":1636897061,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNWYzZDU1Nzc2NmEzYmQ1NGE4MzhlODkzNjVkOTdiMzA5Y2RjYmVhM2M4NjQyMjYxZGNkYjI2YzUwYmMyNjg0NSJ9fSwiZXhwIjoxNjM5NDg4MTYxLCJpYXQiOjE2MzY4OTYxNjEsIm5iZiI6MTYzNjg5NjE2MH0.O_Wdsx-iVY8niyGURaqnzjBTB9AsiAVBkOSs54_aGCOtaVpdkVzzugR3590e80iB7HkKvVt8tg5AaJ8x4GEjpQ"}}}





Change Password Response:{HTTP/1.1 400 Bad Request
Date: Sun, 14 Nov 2021 13:24:37 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=97F98nJ1MD3y%2FKEJ3oOf77VzXgmW2OaCjGpXdiybD%2Bk47n56D8fN2JnITwfmSXXxd%2BdU8LeWW5m%2FBLGnJ72nIrfGahaLHVB8ZLC2yliB1k9Md%2F6b255z4THTSfg3KMEvmE6seA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae08fa56a784a55-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Token not found","payload":null}}





##Response
Failed