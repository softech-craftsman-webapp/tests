url:{https://main-api.hiringo.tech/contracts/{id}/ratings}




Request1:{GET /contracts/%7B9c2d2242-f66d-486f-a75f-ab01e93e3b56%7D/ratings HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 268094c6-8cc1-4698-b4b6-46164256b905
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response1:{
HTTP/1.1 401 Unauthorized
Date: Sun, 14 Nov 2021 22:36:19 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=WauXzlPrVGNxfzKhi5Uz%2BLKih8AYX%2ByM3%2BNUIuMdzTwPYgNtQssEDUcmMLKhGPq8JfUtaq1qsNme75nF1v0nlDimmcxFoYGPArAJmwoYRz4J3JgTl0nH6AgxO4xA%2FrXeOYTaG0mS%2Fs4%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3b7ce8fb25c6e-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}




Request2:{GET /contracts/%7B9c2d2242-f66d-486f-a75f-ab01e93e3b56%7D/ratings HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNGM0MGFhMTVjYmEzMTMzMDRmZTUwYjBkM2VlOTE5MGRhY2IwZWMzZjAzZDg2YTcwZTYxNzY0MmIxM2E4MzdlZSJ9fSwiZXhwIjoxNjM2OTMwMzE1LCJpYXQiOjE2MzY5Mjk0MTUsIm5iZiI6MTYzNjkyOTQxNH0.dgCKjfrP5SyxhlnjsZHGG0Altj987S6uhU0K6Ygloqhi2xJF3WBW2CsYm6xdDhGeygjiGPJObq9iL7GdhLEjQQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 65a3a101-3872-42fe-99c9-682c08ef5338
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response2:{HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 22:37:04 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=HICjvuvjsn9ZGR2hCH3F4MAtTr4CNGuDiiIo7ndR%2BV0KwEPUqQe4iC53L6eCXYfiWA4S3mJRu8x3fOKKpeBfS9%2Broi714OPN3f6zHStJbs8Q2lwyuW5Kq3hJk6FY7ReMq2cda1TKErE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3b8e76af85c6e-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"job_id":"2ef792f1-720a-4822-abdd-bcde4804cf60","contract_id":"9c2d2242-f66d-486f-a75f-ab01e93e3b56","recruiter_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","professional_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","is_rating_finished":false,"rating_items":null}}}



Request3:{GET /contracts/%7B%7D/ratings HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNGM0MGFhMTVjYmEzMTMzMDRmZTUwYjBkM2VlOTE5MGRhY2IwZWMzZjAzZDg2YTcwZTYxNzY0MmIxM2E4MzdlZSJ9fSwiZXhwIjoxNjM2OTMwMzE1LCJpYXQiOjE2MzY5Mjk0MTUsIm5iZiI6MTYzNjkyOTQxNH0.dgCKjfrP5SyxhlnjsZHGG0Altj987S6uhU0K6Ygloqhi2xJF3WBW2CsYm6xdDhGeygjiGPJObq9iL7GdhLEjQQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 353050cc-9d22-4d95-93ab-ab797948804e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response3:{HTTP/1.1 500 Internal Server Error
Date: Sun, 14 Nov 2021 22:39:09 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tAOdxlPpuqZUbQSG3Dan4dNWh3neqgTzkhJv%2FfxjAqmfgbY65VC%2BoMgIx%2B8TlsTMZOdTzlUA2hl7q3xKukZLu41zIlpabQZjKJqqbB6kS5BxvQNpNI3ggKmwwm7LVirLYmouNApfP8A%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3bbf149035c6e-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"{}\" (SQLSTATE 22P02)","payload":null}}




Request4:{GET /contracts/%7B9c2d2242-f66d-486f-a75f-ab01e93e3b56%7D/ratings1111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNGM0MGFhMTVjYmEzMTMzMDRmZTUwYjBkM2VlOTE5MGRhY2IwZWMzZjAzZDg2YTcwZTYxNzY0MmIxM2E4MzdlZSJ9fSwiZXhwIjoxNjM2OTMwMzE1LCJpYXQiOjE2MzY5Mjk0MTUsIm5iZiI6MTYzNjkyOTQxNH0.dgCKjfrP5SyxhlnjsZHGG0Altj987S6uhU0K6Ygloqhi2xJF3WBW2CsYm6xdDhGeygjiGPJObq9iL7GdhLEjQQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7a7b31f1-e460-448f-b2f6-2ac65085f80b
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response4:{HTTP/1.1 404 Not Found
Date: Sun, 14 Nov 2021 22:40:14 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=b3YzAY5UrDm0iQr%2FWn855dFygdGf5tAsGy2J1oYjkJsGFXMWVwBU7wSBK5GXM4aVj%2F1sMkGMX3dfwVPOyiZ37y%2FCHkV28wlhBbin5sz1VfPCFXkU7iTb6T%2B8lvOeE%2FBy76iEMu2hlTU%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3bd89df215c6e-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}