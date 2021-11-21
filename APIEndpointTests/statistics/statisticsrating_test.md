# StatisticsRating




## URL
```
https://main-api.hiringo.tech/statistics/rating
```


## Request
```
Request1:{GET /statistics/rating HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZTkzNzk5YmM2OTBkYmQxMTU4MmI3Y2M4MzI3YjdkYmYyODEwNjljMzUxMDIzMDg4MmU2NzhkY2FhNTcyN2EwNyJ9fSwiZXhwIjoxNjM3MDIxNzgxLCJpYXQiOjE2MzcwMjA4ODEsIm5iZiI6MTYzNzAyMDg4MH0.hOFcJtsU5PJvmM1TeEldqOOze1lBbvwcnBRpzb_9NOW7525tj-WSvgnbPYoohJ6RMu4UwayN0MGvyFS_cA-UuA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: b48a456f-a004-456a-b61d-936640105617
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


```
Request2:{GET /statistics/rating111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNzY4NjUzZjItZTljZi00OGU3LWFjNWMtN2MzMzUwOTA3ODI3IiwibmFtZSI6Inh4IiwiZW1haWwiOiJ4eHgxOEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTNUMTY6NTY6NDIuNjY3MjU3KzAxOjAwIiwiYXV0aCI6eyJpZCI6ImI1NGVjMGM5LWE1ZTEtNDFjNi1iY2NhLTIxMGUzNjQwYWM3NCIsInRva2VuIjoiZTkzNzk5YmM2OTBkYmQxMTU4MmI3Y2M4MzI3YjdkYmYyODEwNjljMzUxMDIzMDg4MmU2NzhkY2FhNTcyN2EwNyJ9fSwiZXhwIjoxNjM3MDIxNzgxLCJpYXQiOjE2MzcwMjA4ODEsIm5iZiI6MTYzNzAyMDg4MH0.hOFcJtsU5PJvmM1TeEldqOOze1lBbvwcnBRpzb_9NOW7525tj-WSvgnbPYoohJ6RMu4UwayN0MGvyFS_cA-UuA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 6b3c2538-31fc-4287-b7c2-9907d23ce36f
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```


```
Request3:{GET /statistics/rating HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7083108e-ecda-4e48-804c-e1201661f11a
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```






## Response
```
Response1:{
HTTP/1.1 200 OK
Date: Tue, 16 Nov 2021 00:02:46 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=yawGbZZrQ%2FniTsOOT%2Fmy7UEkT9HqFnY5QNboDHzy6u%2FldftCJTJE5p%2Byva%2BwnLYnZLZZfsZpXduXHajbpomTmvCsSv3omUFOCqFnmaczvCAhR7etzrizd3oWBGUofatuJr%2BAyxE33rc%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec73d01d754e31-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"total":11,"user_rating_count":0,"latest_rating":{"id":"","submitted_by_id":"","contract_id":"","user_id":"768653f2-e9cf-48e7-ac5c-7c3350907827","points":0,"comment":""},"time":"0001-01-01 00:00:00"}}}
```


```
Response2:{HTTP/1.1 404 Not Found
Date: Tue, 16 Nov 2021 00:06:21 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=ruytldGCM0llS4Ug%2F%2BbuSvqeYdyWPMidD4mHCpAmRC5d0VEsBCEGFkvwy54KbCRXAwquHRiVoI8b7j8wO7HwOQNLbp%2BR3uk4TlW923meppYHxftO5UFRH%2FDrjuhhSmuyugyE3%2BEiQZE%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec790d28e64e31-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```


```
Response3:{
HTTP/1.1 401 Unauthorized
Date: Tue, 16 Nov 2021 00:13:02 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=9Nm6hDnCev0QnbffmddGdH9Pffc8NzOfDXipENS8%2B4qfu8JI7QY2W4uBuNB2OIuGgBvl35SvseGEPQSJweKGv1pFuFDyxAEnXY0aQRkbSnkb%2BaW7x%2BFq2WGnCcMQstioaDE4LAk6pMk%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aec82d86d122b41-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```




## Results
Success