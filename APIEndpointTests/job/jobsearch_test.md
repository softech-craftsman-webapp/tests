url:{https://main-api.hiringo.tech/jobs/search}



Request Headers1:{POST /jobs/search HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiODEyNWJjZWZlNjI1NTBjN2QyMTc1Yjc4NTU0ZTEzNmYyNDZiZGM5NTYzNThjMzcyODRiZWU3MjFkOGE1MDBkNCJ9fSwiZXhwIjoxNjM2ODMzMjA3LCJpYXQiOjE2MzY4MzIzMDcsIm5iZiI6MTYzNjgzMjMwNn0.W-yrNEl_mmTEefOZLNZSJZR5IOMvzLD5XuxZrsLeWX6FIvBDZBoiz-VWhnsjedBSghBU7VKlFU8R7213IFqxrg
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 75fe6bcc-831a-495b-b876-8aff37d5d608
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 187}




Request Body1:{{
"category_id": "e0dd0796-924b-4f6a-97ee-e6a196fbb8ed",
"description": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car"
}}



Response1:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 19:42:11 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=o4dELxQ1K%2F7%2FlkEgNL8ZuItfjJ5IqtGw8gRFR9po40BDVlouQ9jkb9LQnRjG63jD%2FP5%2FR1UlsDH8oIp5z%2FalAh9ePDjJPPtwePw2Bpbtk8y8w%2Br4TCe4v925BHPl2bWvro02k%2FeQZdY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ada7b547a434e67-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"items":null,"pagination":{"totalRecords":0,"totalPage":0,"offset":0,"limit":10,"page":1,"prevPage":1,"nextPage":2}}}}





Request Headers2:{POST /jobs/search HTTP/1.1
Authorization: Bearer 1111
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 448b3e6f-c0cf-4167-9d62-0c9c69d1fda3
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 187}



Request Body2:{{
"category_id": "e0dd0796-924b-4f6a-97ee-e6a196fbb8ed",
"description": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car"
}}



Response2:{HTTP/1.1 401 Unauthorized
Date: Sat, 13 Nov 2021 19:51:30 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=oWmotEZnRObRydohDBbavYIqAB59Uek%2F%2Bew0uo%2FXasX63jCc4BNJ3w7a2N2CLpLBa850CHe2jwoz3501bz4%2BTHaCD9jQcdo%2FfkxFUEiWu706q1%2Bdcrz%2FE957Yh3ybltYQ9OQP7%2B51tY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ada89004d5b5c20-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}






Request Headers3:{POST /jobs/search111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMDQ1MmZlYzY0YjRlNzM4OGUwZDg4ZDc2NTAzNDRmNzhkMzg2MDZjZDgyZjczZWQwZDg0MWVjZjg4YjM4ZDAzNCJ9fSwiZXhwIjoxNjM2ODMzOTc1LCJpYXQiOjE2MzY4MzMwNzUsIm5iZiI6MTYzNjgzMzA3NH0.4vDZNSkaWJiSker73VKZRTumTgTm4a4_5msf3eDpj72SxQ3WzanZbz0u_qsJv6AyJ1UiDLfJDLbdYfD3JMdVBQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 591f2c50-18c0-4758-957a-edb342e2d881
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 187}



Request Body3:{{
"category_id": "e0dd0796-924b-4f6a-97ee-e6a196fbb8ed",
"description": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car"
}}



Response3:{HTTP/1.1 404 Not Found
Date: Sat, 13 Nov 2021 19:52:58 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=CV574lQAQGxRF9kMsoWGvKUg60a2fnZmU9qB9AdYyLWSStkShTqMFzhs8GE%2FSdvYtchGNnzrJXQ2nFeqUIEKMFQiy86ZY5l2ngyI48mVbQo5xgzNsuHvVtrjKVrWpmRo%2F35NXj%2FK23g%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ada8b236e415c20-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}






Request Headers4:{POST /jobs/search HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMDQ1MmZlYzY0YjRlNzM4OGUwZDg4ZDc2NTAzNDRmNzhkMzg2MDZjZDgyZjczZWQwZDg0MWVjZjg4YjM4ZDAzNCJ9fSwiZXhwIjoxNjM2ODMzOTc1LCJpYXQiOjE2MzY4MzMwNzUsIm5iZiI6MTYzNjgzMzA3NH0.4vDZNSkaWJiSker73VKZRTumTgTm4a4_5msf3eDpj72SxQ3WzanZbz0u_qsJv6AyJ1UiDLfJDLbdYfD3JMdVBQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 2705b402-1166-4385-8d2f-6c5a51d9e5d7
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 185}




Request Body4:{{
"category_id": "e0dd0796-924b-4f6a-97ee-e6a196fbb8ed",
"description": "lalalalala",
"is_equipment_required": true,
"latitude": 0,
"longitude": 0,
"name": "Repairing Car"
}}



Response4:{HTTP/1.1 400 Bad Request
Date: Sat, 13 Nov 2021 19:55:16 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=JyUserrzH1wKY7nB%2FY1dgNunAPKhtHN%2F15GWbxn0pyDbk0ciN4eBArp8QeUGLWimIPH1BB5IH2i31Q20Xh043wnwYZoPitc82RckaEfumXrE5aOt6d3XuEe6IafPWuYeV2xIaXlFA1o%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ada8e82cd645c20-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"code=400, message=Key: 'SeachJobRequest.Latitude' Error:Field validation for 'Latitude' failed on the 'required' tag\nKey: 'SeachJobRequest.Longitude' Error:Field validation for 'Longitude' failed on the 'required' tag","payload":null}}



