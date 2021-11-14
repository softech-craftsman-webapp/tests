url:{https://auth.hiringo.tech/auth/login}
{https://main-api.hiringo.tech/jobs/{id}/image}


Login Request Headers:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 87929330-426c-4755-b701-1ebac8981eb0
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}


Login Request Body:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}


Login Response:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 23:34:56 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=C2SBeXrOq%2FM8jpDC1TwSZ2Ca2kVlGp5882%2BVUepTN2mMFDzv9eL%2BC5UqiFZxwC%2BiNbFLii066a6V06m3BK0D%2FhukxZRmBXpMElU9Z8MCuS%2BilDIwUsODPzGLLYh1Fec%2BZraLyA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adbd046281b697b-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiY2Q3MTc2ZGZkZTZmYzk1NmVjZTc3Y2ZjNDJmNDg2NjU2YmQ5YTMzOGY5Mzc2OGNkODg5NDE0ZTRjOTdlN2FlYSJ9fSwiZXhwIjoxNjM2ODQ3Mzk2LCJpYXQiOjE2MzY4NDY0OTYsIm5iZiI6MTYzNjg0NjQ5NX0.qJ_D30uV1IJhsABOO4vftgtd0GzwY7s7hSqt3fagQLQ6e2VlJusXliGoX6QViigV3FiMQHwvR0TujMFWKJ50kA","token_expiration":1636847395,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiY2Q3MTc2ZGZkZTZmYzk1NmVjZTc3Y2ZjNDJmNDg2NjU2YmQ5YTMzOGY5Mzc2OGNkODg5NDE0ZTRjOTdlN2FlYSJ9fSwiZXhwIjoxNjM5NDM4NDk2LCJpYXQiOjE2MzY4NDY0OTYsIm5iZiI6MTYzNjg0NjQ5NX0.AdIOTZlYLz3yD_e117lkUYkCovRAvbcrQMvuPnh6zOmn-P2GbZpULv9d3pT8Ht5fMektUvnuVQIZH868vVBAlA"}}}




Job_new Request Headers:{POST /jobs/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiY2Q3MTc2ZGZkZTZmYzk1NmVjZTc3Y2ZjNDJmNDg2NjU2YmQ5YTMzOGY5Mzc2OGNkODg5NDE0ZTRjOTdlN2FlYSJ9fSwiZXhwIjoxNjM2ODQ3Mzk2LCJpYXQiOjE2MzY4NDY0OTYsIm5iZiI6MTYzNjg0NjQ5NX0.qJ_D30uV1IJhsABOO4vftgtd0GzwY7s7hSqt3fagQLQ6e2VlJusXliGoX6QViigV3FiMQHwvR0TujMFWKJ50kA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a8348405-4a7f-4532-9c89-bf68327f71d0
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 306}


Job_new Request Body:{{
"category_id": "285932f0-3efe-4b05-a901-af952512fb6b",
"description": "lalalalala",
"image": "image1",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car",
"transaction_id": "d40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}

Job_new Response:{
HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 23:38:04 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=5uZbMozpZEfOvl6SnLxOjDzjYJUJMLPcQhK8DZPL%2FRWGwXyfdYXODItDqMlZlmN3VtIK00V6aqJDwtYSsAwXSAEvTAJI3ZYRy2eEgP5YMzUv9nom0CBE3wMUD58eWJuJfiLFXPu0k%2FA%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adbd4deac9a68e9-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"6ab16755-011c-4471-bbf2-7cbf37927b30","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","name":"Repairing Car","description":"lalalalala","image":"image1","valid_until":"2021-12-13T15:09:00Z","is_premium":false,"is_equipment_required":true,"category_id":"285932f0-3efe-4b05-a901-af952512fb6b","transaction_id":"d40062dd-f993-4ac7-8b60-f0269f38c5ca","latitude":10,"longitude":20,"distance":0,"is_contract_signed":false}}}



jobs_image Request Headers:{PUT /jobs/%7B6ab16755-011c-4471-bbf2-7cbf37927b30%7D/image HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiOTJhMjczZTg0ZGFmODhlYTcyZjM3M2ViM2YxYzJjZjJhMmUwOGE3MTU0ZTFhODQwNjg3NzZkMmFiMmRiNGU2ZSJ9fSwiZXhwIjoxNjM2ODQ3MTc4LCJpYXQiOjE2MzY4NDYyNzgsIm5iZiI6MTYzNjg0NjI3N30.QyXpT3drOvpFIBhOM7nR7sMjFZVNwhw-bdMaItFnFIgPLOhQmsRxlGmCkRXS1b7fmBNYNNfAJbvkcEfLHs88ug
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: f5de9b7d-ad96-402a-ba46-31e39844a0fd
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 24}



jobs_image Request Body:{{
"image": "image1"
}
}



jobs_image Response:{HTTP/1.1 403 Forbidden
Date: Sat, 13 Nov 2021 23:38:20 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=t%2FUtgD8Fhnbyv3XZI%2BDsVCPy9sd6bNeDWXE0MttHv71wmrrY7JMO1wmowYiwRLFAu%2FyC9XebBJFKuo3gLqYZ4T5MAqW9Eag6L%2FfoJ%2BDpMNGQHsgTnn0FBvQcw%2BK2LFBNQBxrF3%2FmFaA%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adbd5461a2468e9-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}