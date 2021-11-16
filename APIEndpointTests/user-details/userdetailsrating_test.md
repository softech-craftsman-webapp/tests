url:{https://main-api.hiringo.tech/user-details/{id}/rating}


Request1:{GET /user-details/%7B0562f99f-0c3b-4a89-91d1-e97493369694%7D/rating HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZjNiMDc4NGYxNjBiNDQzNjQ3YWZlODRmN2QwYTBiMDU1YTE5MWI3YWJlNTZiMWQ3YTg1YmU4OWI4NjNjNmI0NSJ9fSwiZXhwIjoxNjM3MDIyNjU3LCJpYXQiOjE2MzcwMjE3NTcsIm5iZiI6MTYzNzAyMTc1Nn0.l3mAdllT1Syf_8pgl8QP5WSOD2zJAKFzqh5AqiPqw4WaJr-SXezAVZS326DeYJh4Q25cjdBwDCStWS3o_3eyWw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 3254258f-b166-493b-9384-a29fadd3eb93
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response1:{HTTP/1.1 200 OK
Date: Tue, 16 Nov 2021 00:17:19 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Ptv3myW7qDJS%2FPOlirYO6jpd2mt%2F17d5zvgEz6UwqB%2F7FjDjxgMtlCbdkjMxfjva3PumWwRV9fYAeUkaYnjGIuxJBvKbNlUCb%2BGWRmvMCmAT2V0wFmOJiom9K48V1WZqi2LxPnXehUk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec891c29e62b41-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"{0562f99f-0c3b-4a89-91d1-e97493369694}","rating":0,"total_rates":0}}}




Request2:{GET /user-details/%7Bid%7D/rating HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZjNiMDc4NGYxNjBiNDQzNjQ3YWZlODRmN2QwYTBiMDU1YTE5MWI3YWJlNTZiMWQ3YTg1YmU4OWI4NjNjNmI0NSJ9fSwiZXhwIjoxNjM3MDIyNjU3LCJpYXQiOjE2MzcwMjE3NTcsIm5iZiI6MTYzNzAyMTc1Nn0.l3mAdllT1Syf_8pgl8QP5WSOD2zJAKFzqh5AqiPqw4WaJr-SXezAVZS326DeYJh4Q25cjdBwDCStWS3o_3eyWw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: baf0ce66-e2b5-4fea-8e0b-b8b67502f842
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response2:{HTTP/1.1 500 Internal Server Error
Date: Tue, 16 Nov 2021 00:20:06 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=FywP1qzQUNloH9DkEuzy00Qxt%2B33dh9MUiwhedE6l3A90rj0aI7stKWQT2BxzTn8fXAfR2i%2BFDIIMaAYIMJxQlSqqT8DNOzV6Si1VkzKoE2diWaFXvRmHyDT%2FIxwT5WJ1VLxShFMhr8%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec8d328af32b41-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"{id}\" (SQLSTATE 22P02)","payload":null}}




Request3:{GET /user-details/%7B0562f99f-0c3b-4a89-91d1-e97493369694%7D/rating11 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZjNiMDc4NGYxNjBiNDQzNjQ3YWZlODRmN2QwYTBiMDU1YTE5MWI3YWJlNTZiMWQ3YTg1YmU4OWI4NjNjNmI0NSJ9fSwiZXhwIjoxNjM3MDIyNjU3LCJpYXQiOjE2MzcwMjE3NTcsIm5iZiI6MTYzNzAyMTc1Nn0.l3mAdllT1Syf_8pgl8QP5WSOD2zJAKFzqh5AqiPqw4WaJr-SXezAVZS326DeYJh4Q25cjdBwDCStWS3o_3eyWw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: eaf51b52-18bb-460c-a934-085743c10f66
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response3:{
HTTP/1.1 404 Not Found
Date: Tue, 16 Nov 2021 00:20:56 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=t2yfYj7DjauFtU3mnKUlH6SKHYZrg3zpbqxpI9109Vygvw%2B5PR383fBZMuZywDcIlZ%2BkOZ93ODmSyr8X94INdboSUdFfBkj%2BSo1z44xANgvaDOWCaa6zwZ6eRUSw22GruoxauM4b%2BK4%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec8e6feb742b41-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}




Request4:{GET /user-details/%7B0562f99f-0c3b-4a89-91d1-e97493369694%7D/rating HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 80f3cdf6-1071-498d-b198-43a97c3e57bc
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response4:{HTTP/1.1 401 Unauthorized
Date: Tue, 16 Nov 2021 00:23:20 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=EmoQFHtnlPekTXrBb8Bp8MwQq7dorBn56Rx5HkIOaWMKb2OF5wvzZuOaMJ58XQB6FmsKsNLgAwc%2FD5Asnt4QXbKz5F3%2Bff3sN2pcs0UlQZmLar96%2BYupITDvC%2BpskdVkADGSdr9s4BE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec91f10a572b41-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}