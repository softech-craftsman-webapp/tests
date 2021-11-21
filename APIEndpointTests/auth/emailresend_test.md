# EmailResend

## URL
```
{https://auth.hiringo.tech/auth/email-resend}
```

## Request
```
Request1:{POST /auth/email-resend HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmM2Y2FiMzJlZjJhMDFhMDhiMjFlODViNmFmOWRkYzYxOGNjNmE4OTBlOTkxNjRiMDRjOGIzOGFjYmY1NzFjYyJ9fSwiZXhwIjoxNjM2NzE4MzkyLCJpYXQiOjE2MzY3MTc0OTIsIm5iZiI6MTYzNjcxNzQ5MX0.-9iw8vHSk5oaO6KnoIeTFUX7MT7xAmrOZll4s1Sybu_HTnSKpeiFWidYPQaj50aUXVLgGSRTeXNPWpy44eAE1A
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 892d1100-a737-436b-8606-0e6e0f22ebc6
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```
```
Request2:{OST /auth/email-resend HTTP/1.1
Authorization: Bearer 22222
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 62ad813b-4eb2-429c-af79-cdf069581ac6
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```
```
Request3:{POST /auth/email-resend HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmM2Y2FiMzJlZjJhMDFhMDhiMjFlODViNmFmOWRkYzYxOGNjNmE4OTBlOTkxNjRiMDRjOGIzOGFjYmY1NzFjYyJ9fSwiZXhwIjoxNjM2NzE4MzkyLCJpYXQiOjE2MzY3MTc0OTIsIm5iZiI6MTYzNjcxNzQ5MX0.-9iw8vHSk5oaO6KnoIeTFUX7MT7xAmrOZll4s1Sybu_HTnSKpeiFWidYPQaj50aUXVLgGSRTeXNPWpy44eAE1A
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 25ff774a-ee6e-4952-b43a-1586cbfd5536
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0}
```



## Response
```
Response1:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 11:46:41 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=bnLoGRD2DZ0gsG7aPnYYijEvLzU%2FEoEyEIfCsNrtDnmSA75Qmaref0vW435FnY0vCXsdcLxd1P09TjWzHC2SO4TP3%2FMUrwGsbu%2FVL29BSHbjT8GGObbM0APJ2Jj%2BEu2Fu8m1YQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6acf8561e9ce3128-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Verification sent successfully","payload":null}}
```



```
Response2:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 11:52:55 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=xreGRffC5AapC8OdvoRsJReJZ%2BMmcwEhHoMqawM11owMVyaB8m434%2FRhrxwLBXhH%2F4%2BRbHcVowiMNrDHUnXX%2BekHyE%2Fvtcgm2TVAuf5v1K3%2FTxPCh43lT0F7V%2FzxurbhTIwpsA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6acf8e8fee203128-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}}
```



```
Response3:{HTTP/1.1 500 Internal Server Error
Date: Fri, 12 Nov 2021 11:58:01 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=%2B%2BS2bXuYtbYnahsWdvVN0VNbJAbHye6BzTTk%2BYw0foAv2WobHH4KynTSZHm0p%2FJvP%2BTY0q92I8q%2Fbat%2BVsQ4IO%2BCDvL0tUKvnErkMzZBxcM1iZUXoIwpQzrETb1NCIA35Mdx3w%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6acf9609db5e3128-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"token is blacklisted","payload":null}}
```



##Results
Success
