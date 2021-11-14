url:{https://auth.hiringo.tech/users/{id}/update-email}



Request Headers1:{PUT /users/%7B%7D/update-email HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzQ0MDUyNzBlYmViZGU0M2RmODU1YTE5ZTQ3NDY2YjMzODJmNjQ3MDY2ZGNhMGIzOWRmYjdiMmIyYjEzNGFiNSJ9fSwiZXhwIjoxNjM2NzMyMjI2LCJpYXQiOjE2MzY3MzEzMjYsIm5iZiI6MTYzNjczMTMyNX0.a_cBs5wol42c_Ag1b94D8OQyT4dq3WuRhs7IFezJ0dA2Cm5XswmfF_ic8NQoCVMziLY_vJzcZRwa01g44AAVQg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: ccd1f674-f012-4b36-8ff1-5ee0ba3450fc
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}



Request Body1:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Response1:{HTTP/1.1 403 Forbidden
Date: Fri, 12 Nov 2021 15:36:18 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=bCjCvdLiRAvaL1isEvWK6Xczvi2VcERoZP2Of2TTaQAN%2BpmgbIsYmNkhldp6XDrDkgPV67thnZyX55W9VXMk0YuTQcJCjwnWAWrwGdVn%2FIO9DMwfFkE%2BnwqVhgdjYCKZTKGGOQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad0d5cb2e035c26-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}





Request Headers2:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-email HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzQ0MDUyNzBlYmViZGU0M2RmODU1YTE5ZTQ3NDY2YjMzODJmNjQ3MDY2ZGNhMGIzOWRmYjdiMmIyYjEzNGFiNSJ9fSwiZXhwIjoxNjM2NzMyMjI2LCJpYXQiOjE2MzY3MzEzMjYsIm5iZiI6MTYzNjczMTMyNX0.a_cBs5wol42c_Ag1b94D8OQyT4dq3WuRhs7IFezJ0dA2Cm5XswmfF_ic8NQoCVMziLY_vJzcZRwa01g44AAVQg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 359e02ce-d3ff-4d30-8eaa-d731ce4fff25
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}



Request Body2:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Response2:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 15:42:26 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=9wTs%2FHWcKMRKKFTzwMcBVgVuj9W4CjgKU33RFltJJntIKUCrWmRcURD%2Bcj1uO2H6WsgDDBAgZNcdg5SC0oyDmncnT%2F5XhD3i2p8h3SfqrtLdObJIHOjhQlOEPqUb08P4NyrHMg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad0deb2f8c25c26-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60"}}}






Request Headers3:{PUT /users/%7B66666%7D/update-email HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzQ0MDUyNzBlYmViZGU0M2RmODU1YTE5ZTQ3NDY2YjMzODJmNjQ3MDY2ZGNhMGIzOWRmYjdiMmIyYjEzNGFiNSJ9fSwiZXhwIjoxNjM2NzMyMjI2LCJpYXQiOjE2MzY3MzEzMjYsIm5iZiI6MTYzNjczMTMyNX0.a_cBs5wol42c_Ag1b94D8OQyT4dq3WuRhs7IFezJ0dA2Cm5XswmfF_ic8NQoCVMziLY_vJzcZRwa01g44AAVQg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7b37305d-4b09-4049-b5d7-794645632892
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}




Request Body3:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}






Response3:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 15:51:57 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=IoST%2FzeZdSyYazVKyuvX%2BZ4KmUj4KyD9N8SNK6GRZo7IMuejVmBmFCtA7%2FOPKf3ZY%2B7b8nmSxyeN4Jb2bjSSrkuidKd139uSf7CSaSty3gP%2BPZt%2B4whPL2iPARIkeKtSnDFOzQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad0ecbad89e4a74-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token is expired by 1m31s","payload":null}}





Request Headers4:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-email HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTY6NDI6MjMuODgwODI1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYmZjZGZhNjA2NDQyMDM0NWYwOWUxNDMxNTc2NmU2OTBiNWFiNjAzZjMxZGZkYTU3Y2IwNjlkNDA5ZjY5ZDNlYyJ9fSwiZXhwIjoxNjM2NzM4MTQwLCJpYXQiOjE2MzY3MzcyNDAsIm5iZiI6MTYzNjczNzIzOX0.UNwMY7dqm8j3giW3oZ60Gnp5WLM4V6r1OTIwnWXwK8_hkclJnOta8jKDijR5ALnhVJGfWQgzxEUk3sRX--vNvQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 030c87b7-244e-4bd7-9e36-bd4d478a7d59
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}



Request Body4:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Respoonse4:{HTTP/1.1 500 Internal Server Error
Date: Fri, 12 Nov 2021 17:14:42 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=2EVruNMRXskGze5jWo8T127rQSb7wmQ45CLTF4OVoHbwjqw8iQc%2BtCswxooqXVAx%2BQDiyiniHxa%2FJLVohDlbj70ZqsCm4G3rnSX3WCelauumd9WHazKaKfT27CeQdpEV%2BiaIdA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad165ee5b557031-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}






Request Headers5:{PUT /users/%7B66312a78-1f9e-4d78-a9fb-231e84967f60%7D/update-email HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMTY6NDI6MjMuODgwODI1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNDA3MWFiODBmNmE2NGE3MDY2ODNiMzUxMmFhMjBhZTZjYzEwODc4MTYxMTBhNDk4MTA2ZmNiYmM3YzE0ZjZjZiJ9fSwiZXhwIjoxNjM2NzM4NDgwLCJpYXQiOjE2MzY3Mzc1ODAsIm5iZiI6MTYzNjczNzU3OX0.LxoTboXplYxzCStlUOJgGo1xQGA47rw7WJSabWYRHvuOnj0CWHHkS3ZP5RT5gvbMCp7fI3wl5N3as6CQQ7uaOw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 64ce4603-46d2-4df9-80c4-44e42537e466
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 6}




Request Body5:{{
}}



Response5:{HTTP/1.1 400 Bad Request
Date: Fri, 12 Nov 2021 17:20:05 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=nYNCqR3lBeEr2A3ukHqSYlh89Xpp%2FPSuKXqEKN4N6UYaaPW3tI7QCW%2FnOXIvY%2BdJtI%2B%2Fl9VBJC0XZns%2F4IyIesamE45abtpOgn7kKP2VvjOfNYDNmiz1tLQem7dXkuHskWVMmw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad16dccba907031-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Key: 'UpdateEmailRequest.Email' Error:Field validation for 'Email' failed on the 'required' tag\nKey: 'UpdateEmailRequest.Password' Error:Field validation for 'Password' failed on the 'required' tag","payload":null}}