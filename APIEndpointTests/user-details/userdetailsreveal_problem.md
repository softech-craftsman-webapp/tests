url:{https://main-api.hiringo.tech/user-details/new}
{https://main-api.hiringo.tech/contracts/new}
{https://main-api.hiringo.tech/user-details/{id}/reveal}


User details_new Request Headers:{POST /user-details/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiMGRmZjkyYmNkYjM4ZmU1NjVmMDVhYzYyNDVkMzZlNzdjNTdkMDcwNmM1NmI5NDAwZTdkNzcxZTk5NmY0YTc2MyJ9fSwiZXhwIjoxNjM3MDIzMzExLCJpYXQiOjE2MzcwMjI0MTEsIm5iZiI6MTYzNzAyMjQxMH0.vjuMzhri2tkBZqghkkdStpC_bQQvW6ba_gLRElILDmWldOykrbHP97_i-bl8mxR4QLjiD1IfTrQjoP-I9ruZ4Q
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 10ca2f02-760a-4664-aae2-d2320f5ee5db
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 122}


User details_new Request Body:{{
"bio": "lalalalakaka",
"email": "xxx18@gmail.com",
"latitude": 20,
"longitude": 50,
"telephone": "12345678"
}}


User details_new Response:{HTTP/1.1 200 OK
Date: Tue, 16 Nov 2021 00:28:17 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=3aQR3H0yPJW2IiFFasK5sVDwXmgHdYD3cjiwLXKrIapq4v%2FOVSlcb7%2FchXuYeLeZQVeLwttE%2FvLjDADCt%2BAbVQ2SSCN0UEvF6p8BiZ5G4qw%2BMslM0sbALtmjwEPG6ueA7Bz%2F5EBz7Hs%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec992f6c7d2b41-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"871833e6-8297-4de1-b27c-3a2e2572641b","user_id":"768653f2-e9cf-48e7-ac5c-7c3350907827","email":"xxx18@gmail.com","bio":"lalalalakaka","telephone":"12345678","latitude":20,"longitude":50}}}





Contracts_new Request Headers:{POST /contracts/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiNGY3Y2ViNTc2NDViYjU0NDRhNWJkN2U5NjdlZmFiMDQwMWU4ZjZiOWM2MDJmMTNiNzg5YjA3NTI5MmQ4MzViMCJ9fSwiZXhwIjoxNjM3MDIzNzQyLCJpYXQiOjE2MzcwMjI4NDIsIm5iZiI6MTYzNzAyMjg0MX0.jNrjUHxjv6xOzfttmxB26vnsY7Of7C_DmwG1znDGeeNJYvSnquxQWZZsWd87AlK2gwGkljo0t1T-QsiCdX5oDQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7908a458-e0fc-4a70-b6ae-8a15aa8feb63
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 124}


Contracts_new Request Body:{{
"end_time": "2021-12-02 16:24",
"job_id": "0f312672-1792-4b0b-bc01-948130c2e1ef",
"start_time": "2020-09-02 12:05"
}}


Contracts_new Response:{HTTP/1.1 200 OK
Date: Tue, 16 Nov 2021 00:36:01 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=GZTTQjIvp9SQbmyA%2BdL4lkSfn0%2B%2FuBIH8tXEbwQRwWR8eqmzbcdhWQyg9QMAssF3ux4oeSVxQYbWz1fnXR3aoiofQp4ZC2BkRFymxPEUV0OriMRp5VSNe2JWOWh0gDfw7x%2BV5DdJlU0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeca482dc362b41-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"a2f7e77b-ca28-474b-8b8d-006b0bf61a42","start_time":"2020-09-02T12:05:00Z","end_time":"2021-12-02T16:24:00Z","signed_by_recruiter_time":"0001-01-01T00:00:00Z","signed_by_professional_time":"2021-11-16T01:36:01.332935772+01:00","recruiter_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","professional_id":"768653f2-e9cf-48e7-ac5c-7c3350907827","job_id":"0f312672-1792-4b0b-bc01-948130c2e1ef"}}}





User details_reveal Request Headers:{POST /user-details/871833e6-8297-4de1-b27c-3a2e2572641b/reveal HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiNGY3Y2ViNTc2NDViYjU0NDRhNWJkN2U5NjdlZmFiMDQwMWU4ZjZiOWM2MDJmMTNiNzg5YjA3NTI5MmQ4MzViMCJ9fSwiZXhwIjoxNjM3MDIzNzQyLCJpYXQiOjE2MzcwMjI4NDIsIm5iZiI6MTYzNzAyMjg0MX0.jNrjUHxjv6xOzfttmxB26vnsY7Of7C_DmwG1znDGeeNJYvSnquxQWZZsWd87AlK2gwGkljo0t1T-QsiCdX5oDQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 33613c21-c17b-4b7a-a538-956cebe10d27
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}


User details_reveal Request Body:{{
"contract_id": "a2f7e77b-ca28-474b-8b8d-006b0bf61a42"
}}


User details_reveal Response:{HTTP/1.1 404 Not Found
Date: Tue, 16 Nov 2021 00:37:46 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=5OEaijljWSA6kMJg%2BWsgQl1CwSoHYTlbw0L8N54YAgZ3%2FWIQUUeTVNPdy%2F7qp%2FsnbsBLMTgI0rTOagyXg6fhzavcSrDljsv10BWmsJRG0u%2BxTazZ58J3OFOucsAq3Kqx2wqZOK%2FkarI%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aeca713df1d2b41-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"record not found","payload":null}}