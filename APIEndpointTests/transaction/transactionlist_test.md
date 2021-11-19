##TransactionList



##Url:{https://main-api.hiringo.tech/transactions/my}


##Request

Request1:{GET /transactions/my HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjA1YTA4NDM2NTRmN2I3NTcwYWZhYTY4ZmUwZGQxZmY1YzAyZmFkYTc5MTE1Yjk5MDU1ZGUwMzkxODM1YzQ3NyJ9fSwiZXhwIjoxNjM2NzA3OTg4LCJpYXQiOjE2MzY3MDcwODgsIm5iZiI6MTYzNjcwNzA4N30.SGt6Zux66jdepsZ0WI6hVHhIc8GES84TO3Q5E54E6wtEaU7NtapjQ7kjJA8skOK08kQ_f2ZKZvJ-dIyjnK1SeQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 523a78cb-f91a-481a-9617-1bc137ba8bc1
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}




Request2:{GET /transactions/mytransaction HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiNjA1YTA4NDM2NTRmN2I3NTcwYWZhYTY4ZmUwZGQxZmY1YzAyZmFkYTc5MTE1Yjk5MDU1ZGUwMzkxODM1YzQ3NyJ9fSwiZXhwIjoxNjM2NzA3OTg4LCJpYXQiOjE2MzY3MDcwODgsIm5iZiI6MTYzNjcwNzA4N30.SGt6Zux66jdepsZ0WI6hVHhIc8GES84TO3Q5E54E6wtEaU7NtapjQ7kjJA8skOK08kQ_f2ZKZvJ-dIyjnK1SeQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 74dab144-b6a8-4a18-a8cf-5ac1125bdf50
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}



Request3:{GET /transactions/my HTTP/1.1
Authorization: Bearer 9999999
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: d0d0526e-27e3-423c-a196-30e9431fd57b
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}





##Response

Response1:{HTTP/1.1 200 OK
Date: Fri, 12 Nov 2021 08:54:23 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=fYbXtFMt3lriDfPPNfN9LJxVaWgB03q4J5sWWe6jvABc3ZwpPiSh3FCtH%2B5Z6rOCnT9pgzJO%2FE4oY0RprszSDEIpZA87cpv2YsUIpg%2BsdOaJUaT0n6EI1u2s2%2BfFd25H%2BPBy7rYurLs%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ace89091d594339-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":[{"id":"e1f0431f-6db3-4495-aa5a-bf48539c9623","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":100000,"currency":"EUR"},{"id":"d40062dd-f993-4ac7-8b60-f0269f38c5ca","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":2000,"currency":"EUR"},{"id":"ad493f8b-54fd-452e-8d63-faf2ae21844d","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":2000,"currency":"HUF"},{"id":"13101885-094e-4e5b-a26f-74a3f90aae21","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":2000,"currency":"HUF"},{"id":"bf31b3bf-0fc6-4659-ba9f-431d4ca232a3","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":700,"currency":"EUR"},{"id":"c59ff530-6786-4b07-ab29-d4219a70805b","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":700,"currency":"EUR"},{"id":"17e6d545-b665-4967-b541-d722808ec913","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":700,"currency":"EUR"},{"id":"abd89b03-13de-42bf-892d-7e749e375782","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":700,"currency":"EUR"},{"id":"003a0cdc-94d5-4e0a-a06e-0ae9ea2de027","user_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","amount":900,"currency":"EUR"}]}
}




Response2:{HTTP/1.1 404 Not Found
Date: Fri, 12 Nov 2021 09:04:58 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=iZ%2FgsKjnWCwI9thVHnW%2FAFEsh4FDKokgkI90vCm%2BB1Ycwt7qrq3cfMhGTssd2ROBo8EzB8W6lKHU46NGkAmNOHZ%2BiWNyOCWU0CvoCA4Sbi4lQEf5OTQdACni7klF7R8XmLjj56Jvikw%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ace98898d8b5c38-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"ERROR: invalid input syntax for type uuid: \"mytransaction\" (SQLSTATE 22P02)","payload":null}}





Response3:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 09:06:17 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=YyGNOn32eROMCnVgYKH6TLxdEvW4Le0zdw5%2B16UXj09Qy692a6lv5kkQIMmEKqpu2iIAB%2F5wTAZ3cAhkvwWwgiF9wwdKuPC1W7ZP2xvPnmSOZBBdVs2X4hErbfZPu8tm7PzuwGp3Fk0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ace9a7aebd85c38-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}
}




##Results
Success