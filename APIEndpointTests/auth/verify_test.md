# Verify


## URL
``` 
https://auth.hiringo.tech/auth/verify/{token}
```


## Request
```

Login Request Headers:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: d7aedef4-c728-4997-8812-faff8ea0f8b5
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}


Login Request Body:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}
```

```
Verify Request:{GET /auth/verify/eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYWRhZGNjZDAxOTA5MTk3NWVmYmIwMzNmODEyMmYwNDAzNjdmNzY0ZGQ4Y2ZiZWZmM2M5YWQyMGM1ODhjMGFhNiJ9fSwiZXhwIjoxNjM2ODk1MTUxLCJpYXQiOjE2MzY4OTQyNTEsIm5iZiI6MTYzNjg5NDI1MH0.eSmwwgPYCWlsJbBoq7Hxyww9kV7enpL-FdFa4s_ZJ6m9dcshqFf9Lcl6TvUkXnFQBbDX4EyeUh9IZRue4aaMsA?email=xxxx@gmail.com HTTP/1.1
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1e39ff9b-fb42-4f9d-bdc6-d6cf3ccb569a
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}
```

## Response
```

Login Response:{HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 12:50:51 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=logOx3G8ofUTROWfjJSntaXwlO7YUnGRrN%2Bqf5uNgEjVD%2BLxxbt4cjwEJbegJp2VzbsPOLQ6ujp347nuGjR3nUDK0c2RSN%2F2RtrRd2RYYwaFs57jn2b7uL04NGym2exf4057zg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae05e2bee1d4dd0-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYWRhZGNjZDAxOTA5MTk3NWVmYmIwMzNmODEyMmYwNDAzNjdmNzY0ZGQ4Y2ZiZWZmM2M5YWQyMGM1ODhjMGFhNiJ9fSwiZXhwIjoxNjM2ODk1MTUxLCJpYXQiOjE2MzY4OTQyNTEsIm5iZiI6MTYzNjg5NDI1MH0.eSmwwgPYCWlsJbBoq7Hxyww9kV7enpL-FdFa4s_ZJ6m9dcshqFf9Lcl6TvUkXnFQBbDX4EyeUh9IZRue4aaMsA","token_expiration":1636895151,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYWRhZGNjZDAxOTA5MTk3NWVmYmIwMzNmODEyMmYwNDAzNjdmNzY0ZGQ4Y2ZiZWZmM2M5YWQyMGM1ODhjMGFhNiJ9fSwiZXhwIjoxNjM5NDg2MjUxLCJpYXQiOjE2MzY4OTQyNTEsIm5iZiI6MTYzNjg5NDI1MH0.VpeXBKThdTQmVgjw0EoTkY4NPcRixVl-JCoWNIfb_T7cVuQaqO_8_9owsrF7u8sCMrLASeaXxWZu33YfitKCgw"}}}
```



```
Verify Response:{HTTP/1.1 400 Bad Request
Date: Sun, 14 Nov 2021 12:55:02 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=OB%2FsSf%2FUpiq7KJ%2FDnxzQI79LvFJnb13Xgfk%2FG95hY1MfP44LAmKOYDWxxz9sS7lWQM1%2BiVAzYnS%2B2NfJXYRMdt0NnhxGyzVM6THbbRrnUN5C40Ca2U1kf21odXVK%2BiXlFUAlmg%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae064512c174dd0-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Token not found","payload":null}}
```



## Result
Failed
