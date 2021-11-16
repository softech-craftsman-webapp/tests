url:{https://auth.hiringo.tech/auth/refresh}


Request1:{GET /auth/refresh HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNTVjMDA0NzhkYTNhYWU2ZjA1MDQ1YzM2NGRlNTMwNWI2OWQ1NzE5MmRkM2U4ZjI5OTkzYjA1YmM1ZWMxODdkOCJ9fSwiZXhwIjoxNjM2NzI3NjY4LCJpYXQiOjE2MzY3MjY3NjgsIm5iZiI6MTYzNjcyNjc2N30.2ciSBhINxlO-QzFLMdQEJsPb_ORdt7dubW_AvCUAI0ks_TIDXYkG2Ai-WUenfL8s2jVsOBIuUc3uMOYHKPXVQw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 3564ee7a-eb94-4dda-b6fe-010eacb639ee
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}





Response1:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 14:20:40 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=DFwpqN4xh4TdCUUFbeJZ87etoLeYl3KUsh3%2FWpI3DlSOimR9sCRnVOA0PDxso%2B25itoThBEKZo4JN0Igo%2FQYSCL2%2B47NBqMPIzQoQ%2FNnyxwTxhpRrq%2FfekOFvTbLmCxfK%2FVbaA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad067038fa0701f-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=crypto/ecdsa: verification error","payload":null}}




Request2:{GET /auth/refresh HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiMGY5ZDA5ZDgxNDJlODZkODRiM2ZlODM1ZGZkZmVjNDZlOGZlNzA0MGI5MjBiZWUyODhhZGM0NGFhODQ2NDdlMCJ9fSwiZXhwIjoxNjM5NDg0MzI4LCJpYXQiOjE2MzY4OTIzMjgsIm5iZiI6MTYzNjg5MjMyN30.3wpErxiHMbHTpyQc1sMhlKIbmzarACoGfNSI23zJeroH4zyPwB8TmnyXO5uunuy_43OkiAHqX56KZUsTcbpq2Q
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1a70a7e0-6613-440f-a380-ed67dff6d073
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}




Response2:{HTTP/1.1 201 Created
Date: Sun, 14 Nov 2021 12:22:28 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=0V8UJoU2zy0UlolfySURAkwuhgvknBVrgyQLM8BVna2dXuKnnpZYF4C0fhjnXvx1RKrWo%2Boyd9lPEA%2BJtFJr%2BxKvkhe4VUfrKHQLrVclQMFWy%2FpJpQPktwpecuT%2FdkHvNkXHoQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae034973e206963-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiMDRjNGZhN2U0MjI0NjBkZTdiNDdhOTQ5ODhmZDAzMWM1YjgwOWQ2Mjk2YWViNjk1OGFmYWQyNWQ2N2ExMWFiNCJ9fSwiZXhwIjoxNjM2ODkzNDQ4LCJpYXQiOjE2MzY4OTI1NDgsIm5iZiI6MTYzNjg5MjU0N30.3KZrI9FJvqCAkXWWmRMhiJtF5sQW58CQhvYBiFv6tIkgnpUlaNdwEVROE4uZta6PBX-hp5t9bjXdh3Z_o1UyCQ","refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiMDRjNGZhN2U0MjI0NjBkZTdiNDdhOTQ5ODhmZDAzMWM1YjgwOWQ2Mjk2YWViNjk1OGFmYWQyNWQ2N2ExMWFiNCJ9fSwiZXhwIjoxNjM5NDg0NTQ4LCJpYXQiOjE2MzY4OTI1NDgsIm5iZiI6MTYzNjg5MjU0N30.VVNqqad1Hnfn23CRuxMQixleMCEp1KR8jSARCWonxF36fr5A3d7Pi650xToQalVhBA7sY3sWXW5KJAgL6sUEsg","token_expiration":1636893448}}}




Request3:{GET /auth/refresh111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiMGY5ZDA5ZDgxNDJlODZkODRiM2ZlODM1ZGZkZmVjNDZlOGZlNzA0MGI5MjBiZWUyODhhZGM0NGFhODQ2NDdlMCJ9fSwiZXhwIjoxNjM5NDg0MzI4LCJpYXQiOjE2MzY4OTIzMjgsIm5iZiI6MTYzNjg5MjMyN30.3wpErxiHMbHTpyQc1sMhlKIbmzarACoGfNSI23zJeroH4zyPwB8TmnyXO5uunuy_43OkiAHqX56KZUsTcbpq2Q
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: db472059-1509-44bd-a235-9d015d327678
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response3:{
HTTP/1.1 500 Internal Server Error
Date: Sun, 14 Nov 2021 12:26:04 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=KIfC0V6KNcsTjtgLhcyy6wjUYqxnD6ZiCEZhatdtYJxznLaqBK%2F6o2ixlYUBIBzF0ODgjgDDZjh43HHc8%2BdEcq8YlckKTtvSoNx6py%2FLezBON4wXPqaodnowwl1FhGfcmcSr8A%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae039e23ee96963-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}







Request4:{}





Response4:{}