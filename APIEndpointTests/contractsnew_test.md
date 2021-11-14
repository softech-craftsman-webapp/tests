url:{https://main-api.hiringo.tech/contracts/new}


Request Headers1:{POST /contracts/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWQ0NDUwYWY0M2JjN2JiNTkyODcwYWQ3ZjJjNjAzOWYxZWUzYjk5ZGQ4MzE4ZWQ1MjhkYTQwOTRiODk5NTlhZSJ9fSwiZXhwIjoxNjM2ODAwMzk0LCJpYXQiOjE2MzY3OTk0OTQsIm5iZiI6MTYzNjc5OTQ5M30.RRH3GSs2wqyJ5hAnyIbk9l6esjMhaJ5zCAYdubdQx5syS7OWRqhs9JvIQ6HLiomxDd91RkbirWlgcePG-YUhDg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 62711b63-1367-4968-974e-fb1b84bcbd95
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 79}


Request Body1:{{
"end_time": "2021-09-02",
"job_id": "001",
"start_time": "2020-09-02"
}}


Response1:{HTTP/1.1 400 Bad Request
Date: Sat, 13 Nov 2021 10:33:01 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=VMhq2edbWuQ7C874sALP28PoglR9aH4Bh1td32oxy6%2FiONpXd8wI8vQcgPOOAeY8Htqu5%2BbFK3ur4ij4q4TEsKX9iG%2FvlpYdRBIz8KgeoPQ%2BVFUyqrlDodLzgfq%2Fw%2BJ6vmI2A7nANxU%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad756e7386d4de8-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"StartTime validation failed, example 2006-01-02 15:04","payload":null}
}






Request Headers2:{POST /contracts/new111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWQ0NDUwYWY0M2JjN2JiNTkyODcwYWQ3ZjJjNjAzOWYxZWUzYjk5ZGQ4MzE4ZWQ1MjhkYTQwOTRiODk5NTlhZSJ9fSwiZXhwIjoxNjM2ODAwMzk0LCJpYXQiOjE2MzY3OTk0OTQsIm5iZiI6MTYzNjc5OTQ5M30.RRH3GSs2wqyJ5hAnyIbk9l6esjMhaJ5zCAYdubdQx5syS7OWRqhs9JvIQ6HLiomxDd91RkbirWlgcePG-YUhDg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1a918392-d649-487d-82f7-063934e9abd3
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 79}



Request Body2:{{
"end_time": "2021-09-02",
"job_id": "001",
"start_time": "2020-09-02"
}}



Response2:{HTTP/1.1 404 Not Found
Date: Sat, 13 Nov 2021 10:34:30 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=QuznYOYsGiJXk7J%2FGCimEH7ldefxPYZ9zmpFVx77Ty5%2Fvq56GWIOdmLNkYOkwZPZbZzwWFMtwpMfLsQGiy7oRGMrg8h7QIkkFQUOtzUdtAZ%2F9jPr42q9IYPTkTCJouA9VqRvAhHAmYA%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad759157b674de8-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}
}




