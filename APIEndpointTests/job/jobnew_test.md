url:{https://main-api.hiringo.tech/jobs/new}



Request Headers1:{POST /jobs/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMDE1MmY2MWZhYmIzMDBiOWRhMGU3ZmZkNmE1NWZkZjY1MGY5MGYyMmU0MGM1NTJhNWY5OTIzNzU3NzFiYzg2NSJ9fSwiZXhwIjoxNjM2ODIyMjQzLCJpYXQiOjE2MzY4MjEzNDMsIm5iZiI6MTYzNjgyMTM0Mn0.UwA37kOAzOQEtWbKECYPYT-BBFFsFryAQ0p977wPpiBVTwdBSH-A-1I4Oz55XivraoPaZgvjDBINK23XpIWQzA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 36dfb470-820c-4431-9387-d0823f02db7e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 298}


Request Body1:{{
"category_id": "cdfb3630-1eae-4854-97e6-981f14b691ca",
"description": "lalalalala",
"image": "image1",
"is_equipment_required": true,
"latitude": 0,
"longitude": 0,
"name": "Repairing Car",
"transaction_id": "e1f0431f-6db3-4495-aa5a-bf48539c9623",
"valid_until": "2021-12-13"
}}



Response1:{HTTP/1.1 400 Bad Request
Date: Sat, 13 Nov 2021 16:37:39 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=vLHXuBGgQ2cAYzaqpLa5hpLucuehaQ8ivXOPoHEkprNzFK8LiRGvD3cPa7aKEX6oL3BD%2Bh0PA6tnd6PG%2F86AMY9EqywEQzEa3RFXXpwnw2aFU7z4M4w8ud%2F2wKAMfluiF0M0YHp%2BW30%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad96d0a4873697b-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"code=400, message=Key: 'CreateJobRequest.Latitude' Error:Field validation for 'Latitude' failed on the 'required' tag\nKey: 'CreateJobRequest.Longitude' Error:Field validation for 'Longitude' failed on the 'required' tag","payload":null}}




Request Headers2:{POST /jobs/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNTVmYmQ5NmFjMTE0MjM1NjhlNjllYWQyMWY0ZDI2YTIxMDMyMDVkMWE4ZGM3YWNjYWMxMjYwYzdlNDFmZjRmYSJ9fSwiZXhwIjoxNjM2ODIyNjg1LCJpYXQiOjE2MzY4MjE3ODUsIm5iZiI6MTYzNjgyMTc4NH0.LNIvBdeJ-ArE0u3fFHliGnnCZoP0ugA85kp4itx45K0sTyjyYZTrGpKL0oFJPXdhTGiacwV_qZccwfBHJkN_Zw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: c56feb98-3714-4aa3-8137-aa04255ca531
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 306}




Request Body2:{{
"category_id": "285932f0-3efe-4b05-a901-af952512fb6b",
"description": "lalalalala",
"image": "image1",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car",
"transaction_id": "d40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}




Response2:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 16:45:16 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=3uFozNfIG5K8YYZMONb3SRJ50H8FFvTtn%2B0Y0ffMobKqpvLBLu8UkSgREroZ7AdcFaswxoP2PZ77inL1ANr7nRUbCQbE4Pt3SihwAixl0f5HKCLh%2FDppckfZeY3QEuo%2BYcekmREwg%2B8%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad9782d7f10697b-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"87baf4eb-ca40-4df9-acec-d842cc8b0bce","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","name":"Repairing Car","description":"lalalalala","image":"image1","valid_until":"2021-12-13T15:09:00Z","is_premium":false,"is_equipment_required":true,"category_id":"285932f0-3efe-4b05-a901-af952512fb6b","transaction_id":"d40062dd-f993-4ac7-8b60-f0269f38c5ca","latitude":10,"longitude":20,"distance":0,"is_contract_signed":false}}
}





Request Headers3:{POST /jobs/new111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNTVmYmQ5NmFjMTE0MjM1NjhlNjllYWQyMWY0ZDI2YTIxMDMyMDVkMWE4ZGM3YWNjYWMxMjYwYzdlNDFmZjRmYSJ9fSwiZXhwIjoxNjM2ODIyNjg1LCJpYXQiOjE2MzY4MjE3ODUsIm5iZiI6MTYzNjgyMTc4NH0.LNIvBdeJ-ArE0u3fFHliGnnCZoP0ugA85kp4itx45K0sTyjyYZTrGpKL0oFJPXdhTGiacwV_qZccwfBHJkN_Zw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: e4e2721f-f4e8-46f9-838e-1e3fb15ec6e5
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 306}



Request Body3:{{
"category_id": "285932f0-3efe-4b05-a901-af952512fb6b",
"description": "lalalalala",
"image": "image1",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car",
"transaction_id": "d40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}


Response3:{HTTP/1.1 404 Not Found
Date: Sat, 13 Nov 2021 16:48:38 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=3gDHofa3dwXybt4NIaoxdlzg2mWOD%2FjrXVw0WoRZ3HPMk45fOw%2BXZ7ZfFsrE0HGngtmcDVCEC%2F1gYvZ0AQEYwawbyZSKRdV2PgQQFt1O1xZRWDC%2Fj1g2unvV%2BN%2FW8WqFKytASo3x%2Fi4%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad97d1f4f06697b-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}
}









Request Headers4:{POST /jobs/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiODkxYTY5NjBjYmYyOWQ1YTdiZTM5ZWU3MzQ4MjM1OTIxZDY2NTFhMmMyMzY5NDZjNWQ5ZjViOTQ1MTA3YWVhZiJ9fSwiZXhwIjoxNjM2ODIzMTgxLCJpYXQiOjE2MzY4MjIyODEsIm5iZiI6MTYzNjgyMjI4MH0.zIy0aePLpuYg7gcfHDotnReyWIK4KqM8Teq6u14veRJ9VY4jYLOZ703JODQMT-nHlSTZjh0JEu_Najfp9Q8GlA111
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 329035de-aa97-473a-885a-052821dc4bb2
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 306}





Request Body4:{{
"category_id": "285932f0-3efe-4b05-a901-af952512fb6b",
"description": "lalalalala",
"image": "image1",
"is_equipment_required": true,
"latitude": 10,
"longitude": 20,
"name": "Repairing Car",
"transaction_id": "d40062dd-f993-4ac7-8b60-f0269f38c5ca",
"valid_until": "2021-12-13 15:09"
}}






Response4:{
HTTP/1.1 401 Unauthorized
Date: Sat, 13 Nov 2021 16:51:52 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=TNX0XopeLbTB2Ma5B0eepKK4WhwYKQ8KFQK79gKBMZKkU6igrYJmqVav4eLgKS1HYCq8rCAa%2FSN%2BBb03C7nAtxeBrq1j9Eq0uFxpTt4EciCtiLMA7gTXOP7G%2FNqTLyJNuD3qy9OFlbk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad981db58f9697b-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=illegal base64 data at input byte 88","payload":null}}
