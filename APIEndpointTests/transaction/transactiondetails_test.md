url:{https://main-api.hiringo.tech/transactions/{abd89b03-13de-42bf-892d-7e749e375782}}


Request1:{GET /transactions/%7Babd89b03-13de-42bf-892d-7e749e375782%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiY2VmMWI2MjJlM2VhOTlmOTJhOGI1OTk3NGQ0ZTVmNDlhNjEwN2UxYWFmYzBjOTBiNWM3MDcyMjk4OWIyMDVkOCJ9fSwiZXhwIjoxNjM2NjYyNTU3LCJpYXQiOjE2MzY2NjE2NTcsIm5iZiI6MTYzNjY2MTY1Nn0.hLvEY_iBu_sMXlWOauR3KOvYRH6hHj6SLkYcav-AU0En1oMfWakD_EaTiD6bxNKmFF_pNKwAsyiQ-9a-DaswUA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 21d70980-a904-40af-8d29-7295cce3b1c7
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}





Response1:{HTTP/1.1 200 OK
Date: Thu, 11 Nov 2021 20:18:31 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=z3%2Ftz12CMZw%2BhCqIY7qWMVNnhvngROgk%2B8EI%2FFooAr7qFTX%2Bp4zI%2BFyQ%2Fqk4TKLpdstyLl%2FptgDhSemW%2FNCgiwVxzxou2%2BM%2BzfhnrBKsP3FA5DHFwqDDY98gBZjV%2Fn0Fet9Q7vJd2bY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aca35d3dd761f3d-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"abd89b03-13de-42bf-892d-7e749e375782","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":700,"currency":"EUR"}}}






Request2:{GET /transactions/%7Bid%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiY2VmMWI2MjJlM2VhOTlmOTJhOGI1OTk3NGQ0ZTVmNDlhNjEwN2UxYWFmYzBjOTBiNWM3MDcyMjk4OWIyMDVkOCJ9fSwiZXhwIjoxNjM2NjYyNTU3LCJpYXQiOjE2MzY2NjE2NTcsIm5iZiI6MTYzNjY2MTY1Nn0.hLvEY_iBu_sMXlWOauR3KOvYRH6hHj6SLkYcav-AU0En1oMfWakD_EaTiD6bxNKmFF_pNKwAsyiQ-9a-DaswUA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a3bc1da2-d4e6-497b-8e9e-583c6dfbe335
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response2:{HTTP/1.1 401 Unauthorized
Date: Thu, 11 Nov 2021 20:29:51 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=AkFjTg3x2RFoQON0pYTB2ML2M7v%2F%2FjMlSSS%2BAhkMWlZEXYqCAw0lyN4UiRVN93ljlCHEnLt8oia4pzuIlhN6Itwj%2BrDY2vouIgYp6IjGFe9eIFRjLNX3iWB91S4hVUZhehRIseqiDEk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aca466f4cbd4edf-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token is expired by 34s","payload":null}}



Request3:{GET /transactions/%7B%22abd89b03-13de-42bf-892d-7e749e375782%22%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMzA2YjlhNDcyNjRiYjRiNzRkYzQ1YmM0OGEwZDYyMjNkOGU1OGZiODBmODQ1MTcxM2VmZDA1MGVmMTRjMzQwZSJ9fSwiZXhwIjoxNjM2NjYzOTAwLCJpYXQiOjE2MzY2NjMwMDAsIm5iZiI6MTYzNjY2Mjk5OX0.jhzAiWn9yUyWybDFxFRg-MArtXyuLqDcfTDZOUXlmEUCiVASQTQaAI7htVCKJxn7HjYP0T3IvJkhYD4f73bo-g
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 4cbf0444-b3c9-46f8-9beb-441906593ef3
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response3:{HTTP/1.1 404 Not Found
Date: Thu, 11 Nov 2021 20:36:56 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=LYRisbW1qN49zwbip5JTOd7AeEl0TJKrGZBKN92GXQuPUeMRF9BTnhXpgD04g1cMARrUCf6QkxUka2mdwfXGIU4QzYjbTeWJe4OE7zFblJHoP2kr5A8HAp%2FSzHL3%2FLUT0RBDfZGPA7U%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aca50cd6d864edf-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"{\"abd89b03-13de-42bf-892d-7e749e375782\"}\" (SQLSTATE 22P02)","payload":null}
}



