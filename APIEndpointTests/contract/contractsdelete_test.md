##ContractsDelete



##Url:{https://main-api.hiringo.tech/contracts/{id}}
{https://auth.hiringo.tech/auth/login}
{https://main-api.hiringo.tech/contracts/new}


##Request

Login Request Headers:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 0860cada-778c-4cf6-a6ee-d856edd43a13
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}

Login Request Body:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Contract_new Request Headers:{POST /contracts/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMzOTZjZWNiMTE3YmI0OTYwODAxNWJiNWE0NmEyMzk1NGM0YjFkYzdmYjVjZWZhNDg1ODc2Nzk1OTI5MGMyNiJ9fSwiZXhwIjoxNjM2OTMyODMwLCJpYXQiOjE2MzY5MzE5MzAsIm5iZiI6MTYzNjkzMTkyOX0.tptCNCepkEEAUW1d8IN5rOuVacIMlrA9rU-pdnsrxBWLMj2DE-S3z2xhRttkaSv-LSzOxVlGiwcgekBoeMm5_g
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: debf01df-deb5-4b8f-aff9-cfd5724c06c3
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 124}



Contract_new Request Body:{{
"end_time": "2021-09-02 16:24",
"job_id": "2ef792f1-720a-4822-abdd-bcde4804cf60",
"start_time": "2020-09-02 12:05"
}}




Contracts_delete Request:{DELETE /contracts/a102d052-bf52-4a8a-b288-234b952f4212 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMzOTZjZWNiMTE3YmI0OTYwODAxNWJiNWE0NmEyMzk1NGM0YjFkYzdmYjVjZWZhNDg1ODc2Nzk1OTI5MGMyNiJ9fSwiZXhwIjoxNjM2OTMyODMwLCJpYXQiOjE2MzY5MzE5MzAsIm5iZiI6MTYzNjkzMTkyOX0.tptCNCepkEEAUW1d8IN5rOuVacIMlrA9rU-pdnsrxBWLMj2DE-S3z2xhRttkaSv-LSzOxVlGiwcgekBoeMm5_g
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 04a24a6a-6b38-4054-80cb-830e63364c21
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}




##Response

Login Response:{HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 23:18:50 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=r8IdaZMZazk%2FzXV%2FCh392cOnfXcqgjXBkUOcQnKADzWErd5TwikJnGTYW1hnyBXjDAipFJixW7V%2B25mHno32n08LUBglCI7qHVHmmpSpl4eo4HUKs3iP7VV%2BWVZQfiw39sfGxg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3f6140fb60629-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMzOTZjZWNiMTE3YmI0OTYwODAxNWJiNWE0NmEyMzk1NGM0YjFkYzdmYjVjZWZhNDg1ODc2Nzk1OTI5MGMyNiJ9fSwiZXhwIjoxNjM2OTMyODMwLCJpYXQiOjE2MzY5MzE5MzAsIm5iZiI6MTYzNjkzMTkyOX0.tptCNCepkEEAUW1d8IN5rOuVacIMlrA9rU-pdnsrxBWLMj2DE-S3z2xhRttkaSv-LSzOxVlGiwcgekBoeMm5_g","token_expiration":1636932830,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMzOTZjZWNiMTE3YmI0OTYwODAxNWJiNWE0NmEyMzk1NGM0YjFkYzdmYjVjZWZhNDg1ODc2Nzk1OTI5MGMyNiJ9fSwiZXhwIjoxNjM5NTIzOTMwLCJpYXQiOjE2MzY5MzE5MzAsIm5iZiI6MTYzNjkzMTkyOX0.eLW_ZpcUPEegTcLbK7GZeZD6qOOaXhMJl4LPvtyPWzvGUdiyBwIFci0U-4N9cLTrvVe0xW8BLje40u4s6AErmA"}}
}



Contract_new Response:{
HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 23:20:48 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=j7ejDDNCev6vEMay2be0o20QBPtQj3A%2BS8PSCzoSvk8Lci22M29P54CdqzIKWsYGiH5JdyW3mFNspftwZRMg67BTBTsiWUsKgOS9KeeqqNdgxwb3alUjryrFGizRGFF1oOcF8YYO%2BO0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3f8f68b880601-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"a102d052-bf52-4a8a-b288-234b952f4212","start_time":"2020-09-02T12:05:00Z","end_time":"2021-09-02T16:24:00Z","signed_by_recruiter_time":"0001-01-01T00:00:00Z","signed_by_professional_time":"2021-11-15T00:20:48.676688165+01:00","recruiter_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","professional_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","job_id":"2ef792f1-720a-4822-abdd-bcde4804cf60"}}}




Contracts_delete Response:{HTTP/1.1 403 Forbidden
Date: Sun, 14 Nov 2021 23:22:54 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=G58ZR%2BelJvB1imkDN%2Bk0aQY5yuA0cYfJS1QL1uj1%2F%2F%2FnCfwc6YCajqVIAmslu4ob%2BycUM%2FJY5dKo8AKqCpS1iWl5pel9CZUnLtjGvCQLiwqVmMy5MaJHFtDrxBXz5D7Y3IJFYJTM3bg%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3fc065da20601-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"You are not permitted to delete contract. Contract is already signed.","payload":null}}




##Results
Failed