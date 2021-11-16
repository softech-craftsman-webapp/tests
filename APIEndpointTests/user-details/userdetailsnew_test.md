url:{https://main-api.hiringo.tech/user-details/new}


Request Headers1:{POST /user-details/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzY4ZjVlNDI2MGQ0M2ExNzA0ZjMyMjcwMmMwNjVkYjhmMzY2MWFhZGU0ZDhjZDU4ZTFlOWYxMzk0ZDI1MzEyMSJ9fSwiZXhwIjoxNjM3MDA1MjgyLCJpYXQiOjE2MzcwMDQzODIsIm5iZiI6MTYzNzAwNDM4MX0.33Q-oOVJrTmWHw8cbg0Iv5tiGyBgvwxdY7_MnoDmv5oocB6gkyAnzoQJKaHqblUQa6w7ArKcOUvYSIS3q_GjuA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 4812a1ca-c033-49d7-976c-cd5d585d0f99
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 121}


Request Body1:{{
"bio": "lalalalalalala",
"email": "xxxx@gmail.com",
"latitude": 10,
"longitude": 20,
"telephone": "123456"
}}


Response1:{HTTP/1.1 200 OK
Date: Mon, 15 Nov 2021 19:27:25 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=6urL9zKK7RCL8j87G4uGgxxSj860PPcrzR9Aya5RtBTqrEzRuGgDcFidupEoth1eR%2FlC50Yd6NCx493%2BGs%2FG4ERX%2FUCHO2QHXgFxLLnWdDyCjxLxfgGuFjfHU4qRU8%2FTHsQ70ljrG7k%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeae073acfc68f2-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"35b41f98-dfd7-4077-baa4-451edcf368d3","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","bio":"lalalalalalala","telephone":"123456","latitude":10,"longitude":20}}
}




Request Headers2:{POST /user-details/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzY4ZjVlNDI2MGQ0M2ExNzA0ZjMyMjcwMmMwNjVkYjhmMzY2MWFhZGU0ZDhjZDU4ZTFlOWYxMzk0ZDI1MzEyMSJ9fSwiZXhwIjoxNjM3MDA1MjgyLCJpYXQiOjE2MzcwMDQzODIsIm5iZiI6MTYzNzAwNDM4MX0.33Q-oOVJrTmWHw8cbg0Iv5tiGyBgvwxdY7_MnoDmv5oocB6gkyAnzoQJKaHqblUQa6w7ArKcOUvYSIS3q_GjuA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 16ecf2c6-4297-4929-8073-c64b1d876567
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 97}

Request Body2:{{
"email": "xxxx@gmail.com",
"latitude": 10,
"longitude": 20,
"telephone": "123456"
}}

Response2:{HTTP/1.1 400 Bad Request
Date: Mon, 15 Nov 2021 19:30:41 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=%2B4Ild8Sn8PVPvhlQ9xHEhvxbDlIaxGrJ8NhyoO%2Br14kvG8KtYhgPdTWJtvbA%2FtakgjXS6UvBt6zdiiH2ivleSNBzJ1Urd7LBp8CY3frtadn%2B9j7zW0pIeG6UPPDlj7HEcL3N8SDWKrk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeae541cd5168f2-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"code=400, message=Key: 'CreateUserDetailRequest.Bio' Error:Field validation for 'Bio' failed on the 'required' tag","payload":null}}



Request Headers3:{POST /user-details/new111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNzY4ZjVlNDI2MGQ0M2ExNzA0ZjMyMjcwMmMwNjVkYjhmMzY2MWFhZGU0ZDhjZDU4ZTFlOWYxMzk0ZDI1MzEyMSJ9fSwiZXhwIjoxNjM3MDA1MjgyLCJpYXQiOjE2MzcwMDQzODIsIm5iZiI6MTYzNzAwNDM4MX0.33Q-oOVJrTmWHw8cbg0Iv5tiGyBgvwxdY7_MnoDmv5oocB6gkyAnzoQJKaHqblUQa6w7ArKcOUvYSIS3q_GjuA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: e897f8ce-285d-410f-873b-8bb545cfac3c
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 121}


Request Body3:{{
"bio": "lalalalalalala",
"email": "xxxx@gmail.com",
"latitude": 10,
"longitude": 20,
"telephone": "123456"
}}


Response3:{HTTP/1.1 404 Not Found
Date: Mon, 15 Nov 2021 19:31:54 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=VOV1kbOHtG4WIOH0LXXrJPSv%2BsHmumbYddqBOAMMhwGFSRWJoIQ9O3SB8GQZCNQNVpV96Ikj3nkD40fjA4ZiZnbOIpPD%2FukD7Fvfdgv02Lofgf1NQ79RvplghBugKJcictUH3hXrtEE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeae7078ee368f2-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}



Request Headers4:{POST /user-details/new HTTP/1.1
Authorization: Bearer 111
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: bb811011-4422-4aa5-b0f0-81ce2e93b343
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 121}

Request Body4:{{
"bio": "lalalalalalala",
"email": "xxxx@gmail.com",
"latitude": 10,
"longitude": 20,
"telephone": "123456"
}}

Response4:{HTTP/1.1 401 Unauthorized
Date: Mon, 15 Nov 2021 19:32:49 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Ov4zJRGWcXquyNhedpM0vGnBPwLyhsmGPnH1XysmwUmW5LUD5WaQprvgSAWxOj9umEW9nxHIFrohe6BQtIV8cZ2XU3o5K3v0LRUx5ZdfI6vHlc2osF9hL%2FHRypAOwK9UK4YiB1%2FHyZY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeae861789d68f2-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}