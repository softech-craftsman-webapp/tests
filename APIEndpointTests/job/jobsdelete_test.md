url:{https://main-api.hiringo.tech/jobs/{id}}


Request:{DELETE /jobs/%7Ba4702a42-afc1-4ae1-a7d4-0cf4ffdfb7f7%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMTI3MmUzNTQxNDNhNjlmMTk3NmE4M2IwZTA5MDFmOTg3NTg5ZGI4MzMwMTNjMzQ1ODI2M2RkNjk5OWFkY2UxZiJ9fSwiZXhwIjoxNjM2ODQ1MTE3LCJpYXQiOjE2MzY4NDQyMTcsIm5iZiI6MTYzNjg0NDIxNn0.GvqR_g9qIFdeUWlBzvxdho-1pcY3CyUvVrUzKjOQG3DpfP1EzMGuzoheN13sLbtRVf8n-kcZHTomI3zhRGRRxw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: cb49aab8-3bab-4f7c-be82-14bb5807aed8
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


Response1:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 23:00:32 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Yxi1HNeXSzFptXm%2B5T7c%2FlZ4qdNEhQFV%2FIj%2BW15ZgIQFktaYPkORP8qGboqQmkU8502d598SLGfvos%2FwBZAWkzjJecSbcn0IpiqZvVoarixs5QtFLCspDy2uA28Oj3jKoFVNj%2Fqmuj0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adb9de51d3468e9-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"a4702a42-afc1-4ae1-a7d4-0cf4ffdfb7f7"}}}





Request2:{DELETE /jobs/%7B6e0ade59-7aee-492e-aad0-68a7146d4759 HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: a70b6aa2-1e6f-40ab-8985-cea81957f781
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response2:{HTTP/1.1 401 Unauthorized
Date: Sat, 13 Nov 2021 23:03:38 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=4KMSOej8mMLXEb4sxFVsfECXSDQJXeib%2FYHX8dOz%2BYbHJvZ0aDuP7pw6tXecsTh8y1ISu4LQPdzNwu%2FI617n4Ienwk0hHtdmA26txXDpIZGY1PQElJejSA5r6J%2Fglx2Qz7%2FTdpTKwJY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adba26fdf6f68e9-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}




Request3:{DELETE /jobs/%7Bid%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYWNkNmYzMDQ5ZWRmNTIxOWI4NDFkYWJmODA0NDc2MmFkZWQ3YTJmODdlM2UxOTYyMzg1ZjEzMGRiZGNjOGU1MiJ9fSwiZXhwIjoxNjM2ODQ1NDc4LCJpYXQiOjE2MzY4NDQ1NzgsIm5iZiI6MTYzNjg0NDU3N30.AY5Rm4n6CE-f76Ap-UaJYZQZFHIoTLMRwfuwpJDon6tcWKJ4tPm7rgxEkvNmkvTsGGRXEHoU9Z6j1j3YoL4qqQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1164410c-4675-4151-9715-66a64136835e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response3:{HTTP/1.1 403 Forbidden
Date: Sat, 13 Nov 2021 23:10:47 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=GKO2TTaZYb54ioimFXRXOFSav%2FJ4js9d%2BcBuX2hbSO%2BHdkqcnmZQ%2ByO4q0ljVD4iVjjy6qWsfEjt0uFNweQt8Tr8BbteqpntVnqYqSaXQXaihirm3lD8mFMJVjOLbLl0H8P%2BVIB2lyA%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adbace7d9b668e9-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}



Request4:{DELETE /jobssss/%7B6e0ade59-7aee-492e-aad0-68a7146d4759%7D HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYWNkNmYzMDQ5ZWRmNTIxOWI4NDFkYWJmODA0NDc2MmFkZWQ3YTJmODdlM2UxOTYyMzg1ZjEzMGRiZGNjOGU1MiJ9fSwiZXhwIjoxNjM2ODQ1NDc4LCJpYXQiOjE2MzY4NDQ1NzgsIm5iZiI6MTYzNjg0NDU3N30.AY5Rm4n6CE-f76Ap-UaJYZQZFHIoTLMRwfuwpJDon6tcWKJ4tPm7rgxEkvNmkvTsGGRXEHoU9Z6j1j3YoL4qqQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 6411595b-a249-47fe-b2ab-21a7e8c8e620
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Response4:{
HTTP/1.1 404 Not Found
Date: Sat, 13 Nov 2021 23:13:16 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=VIuWLrg75m43zYMbXwySv1MPsOGgMk%2BxIQqoNIyVSneYcLH6G19aee0M%2FuUn9IvB9ROK2o2HcShdDRgXiVrNfla5Qpnd1QFnr6XsFpbiSXbqEPeLIIcg4BSsVEV5swz9iBEpM%2BH%2BwrI%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adbb08c2a5268e9-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}