# MyUserDetails



## URL
```
https://main-api.hiringo.tech/user-details/my
```


## Request
```
Request1:{GET /user-details/my HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjI5MjZhOTQ5MDVjODRlZWQyZWM4MjJkNjNjYTliNzc5NTI5OTY5OWQ3YTAyYTNiNjI4ZGUxZmUxYjBkM2ZkYiJ9fSwiZXhwIjoxNjM3MDA1ODUxLCJpYXQiOjE2MzcwMDQ5NTEsIm5iZiI6MTYzNzAwNDk1MH0.SkitRnRjjQ-f0aKn8mGukikCjnUImhSzH9z7UMGVVXgq_fBl_upJOKpA_-h5vCMAWOlKOwBibwimoyQ7GVOtCQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: b2b32b31-1f0a-4abe-99b7-394dea7d9a86
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


```
Request2:{GET /user-details/my111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjI5MjZhOTQ5MDVjODRlZWQyZWM4MjJkNjNjYTliNzc5NTI5OTY5OWQ3YTAyYTNiNjI4ZGUxZmUxYjBkM2ZkYiJ9fSwiZXhwIjoxNjM3MDA1ODUxLCJpYXQiOjE2MzcwMDQ5NTEsIm5iZiI6MTYzNzAwNDk1MH0.SkitRnRjjQ-f0aKn8mGukikCjnUImhSzH9z7UMGVVXgq_fBl_upJOKpA_-h5vCMAWOlKOwBibwimoyQ7GVOtCQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 68a773e0-10f2-48da-8475-5617c578bf7e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```



```
Request3:{GET /user-details/my HTTP/1.1
Authorization: Bearer 33333
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: c6bd2673-856d-40ff-a867-84f98db525c2
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


## Response
```
Response1:{HTTP/1.1 200 OK
Date: Mon, 15 Nov 2021 19:36:06 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=qGnoEWWo%2FUFZ3i8zO35LonlGGvT4CwK%2BdgcrNrYThmm3qGXataQQLlljlVVLBu02bkGoS2uEeEy3lFtjuM1kOVsX5RPxECdYCNzdY4wp2qpieaVSyLiPVX%2B4k8op7Gq9BPl%2BcM8YKr4%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeaed2d1e2268f2-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"35b41f98-dfd7-4077-baa4-451edcf368d3","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","bio":"lalalalalalala","telephone":"123456","latitude":10,"longitude":20}}}
```



```
Response2:{
HTTP/1.1 404 Not Found
Date: Mon, 15 Nov 2021 19:37:32 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=x2FqaSTFO9jwywLLsepHYbTcbD1PXOW8PclDmoiJL4R6ie998AsDR1l0pc1vl60IRroKK%2BtPeYIKA2cV3mmk7oy3cR6%2BlzpqTS%2FdRuGGhN54Av3Xxb18gEycT3tg0TfYeMa7WcRGRsk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeaef4a4c1f68f2-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```






```
Response3:{HTTP/1.1 401 Unauthorized
Date: Mon, 15 Nov 2021 19:38:19 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=hWnug11ca9oQecDJr8fTO3FI3vUgQuoy5WqfARccNo0cbgjab3K2YfRExW%2BA57iQu40ey8xio92b%2BtRpn%2FckxtrdK0nh3BUENlc4bjIZo3HieJ%2Ffakbp4Rpk1wF7xoT7GuLe2c3W%2ByE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeaf06ebb4b68f2-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```





## Results
Success