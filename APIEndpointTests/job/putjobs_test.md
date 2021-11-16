url:{https://main-api.hiringo.tech/jobs/{id}}



Request Headers1:{PUT /jobs/%7B%7D HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1ac2313a-9111-4d6f-ada4-91c038024fb8
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 287}




Request Body1:{{
"category_id": "2b19ce44-d3a8-4a47-90ff-c98930e9bda3",
"descriptions": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Pipe repairing",
"transaction_id": "sd40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}




Response1:{HTTP/1.1 400 Bad Request
Date: Sat, 13 Nov 2021 20:22:15 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=tRANjbgYQ%2FJQZMXcIw3Hw%2FDb%2B73KlejoVnJMVi9MAPQ3ZYh%2FIshh0SvKPES%2FksQPElL6MA%2BA0326wOjmi4SDzv7bexqu38Zlf5K0XXjwNkLYkCQgokS2PEc1NBAz1c5UvG2A50PO2kU%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adab6095d995c20-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"missing or malformed jwt","payload":null}}






Request Headers2:{PUT /jobs/%7B%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNmFmYjJmMGFiOGI0Mjk2NTE2MzNkYTEwZWViZjRiNzc5Yjg4ZjQ1NDczMWM5ZDEzOTM3MzdkMjc2ZTlmMjVkZSJ9fSwiZXhwIjoxNjM2ODM1NjkxLCJpYXQiOjE2MzY4MzQ3OTEsIm5iZiI6MTYzNjgzNDc5MH0.BNQxv62zg0RePhvUVtZh2sZ3YpxBBnefob1RtkKZ9Pdl82b3nBvZXosWS8noaOhdaXF5wFHzwHdb03qZghGVoA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: dab2b908-a871-43a3-83c5-7fcb039283d6
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 287}




Request Body2:{{
"category_id": "2b19ce44-d3a8-4a47-90ff-c98930e9bda3",
"descriptions": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Pipe repairing",
"transaction_id": "sd40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}



Response2:{HTTP/1.1 403 Forbidden
Date: Sat, 13 Nov 2021 20:24:29 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=ZavKIMjZXRCW%2FhGdbaict%2FOQHaMinBBVrMM874oVCgEsobWiDEeuK8Kr7BKIGdfnXK1DeEDwqP4EAeWbYj9VwZdbX40FyPrdbdiZEe%2FiV1kbA5mA5zSY6GaDXojoVwuZhqok4AJTW6E%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adab94c2b5b5c20-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}
} 





Request Header3:{PUT /jobs/%7B0998e0bc-a98e-416f-96ba-9b9d9d4de8c0%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWI0YjZiZDE0OGI5YzBjMTk2ODExNTU0Zjg1OTExOGMzMjg1NWNhMTUxODgzMDc2Mzc4NzNiNmVmYzQ0YjNiZCJ9fSwiZXhwIjoxNjM2ODM3MTc4LCJpYXQiOjE2MzY4MzYyNzgsIm5iZiI6MTYzNjgzNjI3N30.sJngpbnIneNhrbajlYYwjBGqEpcUWuT4Kd-PmzpEiZ_eErbJ-loCMatuCogWhCO2eu6Na3StF62dsaGCHP6cXQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 2a602034-1a76-4b62-91db-7da9f5793e3d
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 287}



Request Body3:{{
"category_id": "2b19ce44-d3a8-4a47-90ff-c98930e9bda3",
"descriptions": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Pipe repairing",
"transaction_id": "sd40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}
}


Response3:{HTTP/1.1 500 Internal Server Error
Date: Sat, 13 Nov 2021 20:45:28 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=mQdqBNSkINRy9IdmfMgxR8rzE%2FaTJG%2FNyu7dPP6z1FsVThLB%2BwywmV47rXDY5MdMDwf%2BTMDveMiKgJhi5R6E43XcWO4Wmd6TVEcUlill9IsBmDuDXtb1iNZiPnECyWsxznA3Vc91yCo%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adad80c8cf95caa-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"sd40062dd-f993-4ac7-8b60-f0269f38c5ca\" (SQLSTATE 22P02)","payload":null}}



Request Headers4:{PUT /jobs/%7B0998e0bc-a98e-416f-96ba-9b9d9d4de8c0%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWI0YjZiZDE0OGI5YzBjMTk2ODExNTU0Zjg1OTExOGMzMjg1NWNhMTUxODgzMDc2Mzc4NzNiNmVmYzQ0YjNiZCJ9fSwiZXhwIjoxNjM2ODM3MTc4LCJpYXQiOjE2MzY4MzYyNzgsIm5iZiI6MTYzNjgzNjI3N30.sJngpbnIneNhrbajlYYwjBGqEpcUWuT4Kd-PmzpEiZ_eErbJ-loCMatuCogWhCO2eu6Na3StF62dsaGCHP6cXQ
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 4fb48d3c-d613-470f-8cd8-86ea181d6d8e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 286}



Request Body4:{{
"category_id": "2b19ce44-d3a8-4a47-90ff-c98930e9bda3",
"descriptions": "lalalalala",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Pipe repairing",
"transaction_id": "784d41d8-2d55-4c46-a409-99d48528b14e",
"valid_until": "2021-12-13 15:09"
}}


Response4:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 20:51:28 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Li10hUHzj13x%2BnOT241mW9%2BzCZxq6nZfdsIWxzHsqb%2FAdTNt3lQSAAg2s6Eo38NBARCtFurwO51vFxPOehksj%2FMZgPYiZZc%2F4VEtqEjqB51kujX%2BA%2BYjBouIAdzlDvtC%2Bog%2FhSf7c5Y%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adae0d39b7a5caa-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"0998e0bc-a98e-416f-96ba-9b9d9d4de8c0"}}}