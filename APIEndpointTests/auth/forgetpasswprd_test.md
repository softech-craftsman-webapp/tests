# ForgetPassword



## URL
```
https://auth.hiringo.tech/auth/forgot-password
```

## Request
```

Request Headers1:{POST //auth/forgot-password HTTP/1.1
Authorization: Bearer yJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZDk2NWJlYWQ5Y2VlNDE2NGY0NzU3MDQ0ODNkYjhmZWVjYTAzNzM5NmQzN2E3MzM0M2RiNmNhNTliMjQ0MmE1MyJ9fSwiZXhwIjoxNjM2NzIzODAzLCJpYXQiOjE2MzY3MjI5MDMsIm5iZiI6MTYzNjcyMjkwMn0.MY_bBx63McY-BMMFHciJ_8FlZQscCFMRevw9Inog0_Ac_EafyNO12DOFJSTHKnfQnCVD8v6HcTyZyQkOJe5jPw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 1b7f78c0-b680-46d4-aae0-06c0972d867a
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 31}

Request Body1:{{
"email": "xxxx@gmail.com"
}
}
```

```
Request Headers2:{POST /auth/forgot-password HTTP/1.1
Authorization: Bearer yJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZDk2NWJlYWQ5Y2VlNDE2NGY0NzU3MDQ0ODNkYjhmZWVjYTAzNzM5NmQzN2E3MzM0M2RiNmNhNTliMjQ0MmE1MyJ9fSwiZXhwIjoxNjM2NzIzODAzLCJpYXQiOjE2MzY3MjI5MDMsIm5iZiI6MTYzNjcyMjkwMn0.MY_bBx63McY-BMMFHciJ_8FlZQscCFMRevw9Inog0_Ac_EafyNO12DOFJSTHKnfQnCVD8v6HcTyZyQkOJe5jPw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 3f061b4b-8386-459f-b6d9-747710d2018f
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 34}

Request Body2:{{
"email": "xxxx123@gmail.com"
}}
```

```
Request Headers3:{POST /auth/forgot-password111 HTTP/1.1
Authorization: Bearer yJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZDk2NWJlYWQ5Y2VlNDE2NGY0NzU3MDQ0ODNkYjhmZWVjYTAzNzM5NmQzN2E3MzM0M2RiNmNhNTliMjQ0MmE1MyJ9fSwiZXhwIjoxNjM2NzIzODAzLCJpYXQiOjE2MzY3MjI5MDMsIm5iZiI6MTYzNjcyMjkwMn0.MY_bBx63McY-BMMFHciJ_8FlZQscCFMRevw9Inog0_Ac_EafyNO12DOFJSTHKnfQnCVD8v6HcTyZyQkOJe5jPw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: e6068ce6-41a6-49c9-9eb4-5cb0283c7de6
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 31}


Request Body3:{{
"email": "xxxx@gmail.com"
}}
```


```
Request Headers4:{POST /auth/forgot-password HTTP/1.1
Authorization: Bearer yJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZDk2NWJlYWQ5Y2VlNDE2NGY0NzU3MDQ0ODNkYjhmZWVjYTAzNzM5NmQzN2E3MzM0M2RiNmNhNTliMjQ0MmE1MyJ9fSwiZXhwIjoxNjM2NzIzODAzLCJpYXQiOjE2MzY3MjI5MDMsIm5iZiI6MTYzNjcyMjkwMn0.MY_bBx63McY-BMMFHciJ_8FlZQscCFMRevw9Inog0_Ac_EafyNO12DOFJSTHKnfQnCVD8v6HcTyZyQkOJe5jPw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 72cb5dfd-f7d5-4803-a957-0bb528b954f2
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 30}


Request Body4:{{
"password": "qwaezsxd12"
}}
```




## Response
```

Response1:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 13:16:06 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=xJO3CQ3uvyot45Ex%2FAXBM8kAVkAWlGUZwWCZrQKNh%2FxC8XWMeTQzDQiO%2FKT4Yp%2BdzokudNGCvzZE5RcwohEyZyV0X99N8rgzJNPrjZVE0HUZGtSIRLqAG3TGLKlrepVVJO0o9w%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad0085d2d2e178e-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Verification sent successfully","payload":null}}
```



```
Response2:{HTTP/1.1 404 Not Found
Date: Fri, 12 Nov 2021 13:27:57 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=qq7SvTtf6owl51UtxQ1T8qhFuiAJ%2ByLgUcP974s7OYfihzublr82bOO1LosBkWrC6I%2FvFC9%2FvsoYPYTdlzWDhktYeb5Lxx83eFJQsKZ6r3mSRXuXKGgHAiSxYgNqcNL18wM0qw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad019c5a9f84ea3-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"User not found","payload":null}}
```



```
Response3:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 13:30:46 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=gjIyN9NDA%2BRMA9gzfxbQcOLqvzuib17L8Ow5GSkJmzHgKdIIbhIuQlGzJC17K1eY9gAB7%2FgT42ZHy1%2FSnR0ZMiDlTG8yN2xc%2BtZn0LPFyeLXTyjbzbdgjQvLZ8BVdqNzvKahoQ%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad01deb8b254ea3-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=invalid character 'È' looking for beginning of value","payload":null}
}
```



```
Response4:{HTTP/1.1 400 Bad Request
Date: Fri, 12 Nov 2021 13:39:14 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=HnJmYtorUE%2B0MDzxg4jKTS6Dmorzl%2FgGzBkrH1cXaJvTHi%2FjiCMzIViZ9hsBzPT6bcqZ7NNZsLtpACbOCkVMYlGgyYMyap0O2Zkb1VJ6I3RO8AfRaNxj6u9Smby7wTkwz9%2Fj1g%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ad02a4b4ad32c26-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Key: 'ForgotPasswordRequest.Email' Error:Field validation for 'Email' failed on the 'required' tag","payload":null}}
```



## Result
Success


