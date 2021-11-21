# SignContracts





## URL
```
https://main-api.hiringo.tech/contracts/{id}/sign
```




## Request
```
Request1:{POST /contracts/%7B3bc83e6c-35c6-4eca-925a-1372fe7e804a%7D/sign HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWY2ODUwODY4MWNiMDhjNjk3YTQ0OWZlMjY4NTExNWZjNDVmNjNjNGNiNTRhMGY5N2ZiNzUwMjE0NmE4MzUwNiJ9fSwiZXhwIjoxNjM2OTMxNzE1LCJpYXQiOjE2MzY5MzA4MTUsIm5iZiI6MTYzNjkzMDgxNH0.j_LCKOPoTzb1rA6HIQ0hpl6WRDK0A_wHv4P4eKl4bX6798tTD5NHyk-hYSdXUP2CSjbt1PP9KYzg-hGilvTxMw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 94c97528-a7b6-41f2-9de4-ac2ae1fda004
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```


```
Request2:{POST /contracts/%7B3bc83e6c-35c6-4eca-925a-1372fe7e804a%7D/sign111 HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWY2ODUwODY4MWNiMDhjNjk3YTQ0OWZlMjY4NTExNWZjNDVmNjNjNGNiNTRhMGY5N2ZiNzUwMjE0NmE4MzUwNiJ9fSwiZXhwIjoxNjM2OTMxNzE1LCJpYXQiOjE2MzY5MzA4MTUsIm5iZiI6MTYzNjkzMDgxNH0.j_LCKOPoTzb1rA6HIQ0hpl6WRDK0A_wHv4P4eKl4bX6798tTD5NHyk-hYSdXUP2CSjbt1PP9KYzg-hGilvTxMw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: c241e85b-ac60-496d-b9a8-6d8ba19a7d83
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```



```
Request3:{POST /contracts/%7B3bc83e6c-35c6-4eca-925a-1372fe7e804a%7D/sign HTTP/1.1
Authorization: Bearer 111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 91c35afb-6a24-442d-8b65-68872dcf8930
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```




```
Request4:{POST /contracts/%7B%7D/sign HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiMWY2ODUwODY4MWNiMDhjNjk3YTQ0OWZlMjY4NTExNWZjNDVmNjNjNGNiNTRhMGY5N2ZiNzUwMjE0NmE4MzUwNiJ9fSwiZXhwIjoxNjM2OTMxNzE1LCJpYXQiOjE2MzY5MzA4MTUsIm5iZiI6MTYzNjkzMDgxNH0.j_LCKOPoTzb1rA6HIQ0hpl6WRDK0A_wHv4P4eKl4bX6798tTD5NHyk-hYSdXUP2CSjbt1PP9KYzg-hGilvTxMw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 499f0fe0-c002-4dfd-b40c-e68bdfdbf62e
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```



## Response
```
Response1:{HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 23:00:56 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=XSileX%2FcZPD9Nf0PrbEg86FtsvFQlM1KL26%2FFhDQFmzKCWEfHjoiC8gSN3WcdYJhTLXcAZZy0Qs8NbeXEreSwSo4dTaK9rvSJ%2FyT5dSBQqO2kunBbcbykAe0rogpz52tK8k8O2eyBlo%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3dbd7fbdf5c6e-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"3bc83e6c-35c6-4eca-925a-1372fe7e804a"}}}
```



```
Response2:{
HTTP/1.1 404 Not Found
Date: Sun, 14 Nov 2021 23:03:11 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=df1lLBLxbZXOnBJvDoSDPmYpUbsToFS54PoqLX%2BU1jUiNdNxhdJc%2FQoPoXV5rWDFGUZgDINuFWEuG4bNSvbB8rGZCitBteI8iW6v24EPSpETI%2FSXzzA2%2Bz66d%2BMarB2rAphJAsyL6I8%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3df279acc5c6e-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```




```
Response3:{
HTTP/1.1 401 Unauthorized
Date: Sun, 14 Nov 2021 23:04:59 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=pINnru4v7oVrMfdo7inYrc1yd%2FygnlAC8UyDQOZkd83bUUA3K2iwRmbK2Hh%2BHYM4UwJqBBaGubi84V%2F0PiU0zzKdbDXj%2BSskxeeaGP0G%2FzSxEzDB2rxgfMkHajmjh0FDOjOCXa6C0sA%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3e1cb398b6d6d-MUC
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```



```
Response4:{HTTP/1.1 500 Internal Server Error
Date: Sun, 14 Nov 2021 23:05:39 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=wOVfD861CGaB43L%2B8wDZB%2BEgPISLzppcdg5R%2BdVZdlWnhaSjZBv%2FbDVmdS0mIdCsV%2FeGPMd%2FGhFtob5m%2FRlvKFTT0Zr17JgHZVZgZyTYj7bq5ym%2BqgNYyJh4UddVEuUv4ikeyM6l3FY%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae3e2c69f150601-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"{}\" (SQLSTATE 22P02)","payload":null}}
```





## Results
Success
