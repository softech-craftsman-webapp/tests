##CategoriesDelete



##Url
{https://main-api.hiringo.tech/categories/{id}}
{https://auth.hiringo.tech/auth/login}
{https://main-api.hiringo.tech/categories/new}



#Request

Login Request Headers:{POST /auth/login HTTP/1.1
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 315d510c-eab6-4111-9914-37bcec5ebb37
Host: auth.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 59}



Login Request Body:{{
"email": "xxxx@gmail.com",
"password": "qwaezsxd12"
}}



Categories_new Request Headers:{POST /categories/new HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYTAzYjY3MWM3YzA2ZTExM2U3ZTFmOWZkMDYxZTE1NDg3NjUzYTE5YTFkZjVkNzc2NWM4MWEwMjhkZGZhNmYxYyJ9fSwiZXhwIjoxNjM2ODQyMTYyLCJpYXQiOjE2MzY4NDEyNjIsIm5iZiI6MTYzNjg0MTI2MX0.jMFf5vTVGubMRpFDsQKEdE3YfZJwKKkgGmxHtXaur8OmytnNIcghyk2c_Isszt3rRAxxfLIGiFOjfj0HA1DFcA
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 5c48a0b0-f529-4b3f-ba39-19fcaa659de1
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 66}



Categories_new Request Body:{{
"description": "lalalalala",
"name": "Repairing Car"
}}





Categories_delete Request:{DELETE /categories/5eaaa0d7-8ae8-4466-ba1a-b729e8730c1e HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYTAzYjY3MWM3YzA2ZTExM2U3ZTFmOWZkMDYxZTE1NDg3NjUzYTE5YTFkZjVkNzc2NWM4MWEwMjhkZGZhNmYxYyJ9fSwiZXhwIjoxNjM2ODQyMTYyLCJpYXQiOjE2MzY4NDEyNjIsIm5iZiI6MTYzNjg0MTI2MX0.jMFf5vTVGubMRpFDsQKEdE3YfZJwKKkgGmxHtXaur8OmytnNIcghyk2c_Isszt3rRAxxfLIGiFOjfj0HA1DFcA
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 50d67664-fddc-4bf3-9f88-0704710d47e2
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive}


##Response

Login Response:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 22:07:42 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=RNeX%2BqcawTZBEGejQjj3teVcSEpoj%2FFvqrIYLtSKVwes5x6cOOrr9O5ppOgaBOxB9DRoSqRyjSI4aeVYlS8Q09yTEErJdfU5sww1W1xfA7QlGhXJRBQK6U3tl74ghGyTW5SQtA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adb5080c8934dd0-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"66312a78-1f9e-4d78-a9fb-231e84967f60","email":"xxxx@gmail.com","name":"Rachel","email_verified_at":null,"token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYTAzYjY3MWM3YzA2ZTExM2U3ZTFmOWZkMDYxZTE1NDg3NjUzYTE5YTFkZjVkNzc2NWM4MWEwMjhkZGZhNmYxYyJ9fSwiZXhwIjoxNjM2ODQyMTYyLCJpYXQiOjE2MzY4NDEyNjIsIm5iZiI6MTYzNjg0MTI2MX0.jMFf5vTVGubMRpFDsQKEdE3YfZJwKKkgGmxHtXaur8OmytnNIcghyk2c_Isszt3rRAxxfLIGiFOjfj0HA1DFcA","token_expiration":1636842162,"refresh_token":"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYTAzYjY3MWM3YzA2ZTExM2U3ZTFmOWZkMDYxZTE1NDg3NjUzYTE5YTFkZjVkNzc2NWM4MWEwMjhkZGZhNmYxYyJ9fSwiZXhwIjoxNjM5NDMzMjYyLCJpYXQiOjE2MzY4NDEyNjIsIm5iZiI6MTYzNjg0MTI2MX0.mxcZgwER2SHScW9-_FSx9KTdBASepAdfqbUTkUmhspoNk5d0gC7SJAVGyytRbHwiI8V3ZkN2HScK9iVXkXeHVQ"}}
}




Categories_new Response:{HTTP/1.1 200 OK
Date: Sat, 13 Nov 2021 22:08:19 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=5W%2BIxjEhMLFbQgOiBmeSQ8OYnnAdiXDszvwYpUrA4Pyy7%2FV1R%2B6tjP6MHeo4VUoqQjupC0gDLbtweePdJ6ggSIQRx9aZ5%2BBY9MGaTjslS%2BJ6cl4k%2BLavyDT9M%2FDHD17OMgWfXqmsXa0%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adb51697fc14eda-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"id":"5eaaa0d7-8ae8-4466-ba1a-b729e8730c1e","created_by_id":"66312a78-1f9e-4d78-a9fb-231e84967f60","name":"Repairing Car","description":"lalalalala"}}}




Categories_delete Response:{HTTP/1.1 403 Forbidden
Date: Sat, 13 Nov 2021 22:09:38 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=5wBluD1fAvU0ku8cKsTkwLzYwdBGZgicea6kQXz41pSm%2FRFpKmzQwXV5zw2wimFeI%2FxtXac2qsq3FFVnlu8K3HaAkfboPGcYg8SyIaZL9AoGSxXEo6X0M%2FV5AY1FO2xVRVjGO2xrfuI%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6adb5352c9774eda-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Forbidden","payload":null}}




##Results
Failed