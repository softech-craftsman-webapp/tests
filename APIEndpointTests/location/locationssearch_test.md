## LocationsSearch

## URL
```
https://main-api.hiringo.tech/locations/search
```

## Request
```
Request Headers1:{POST /locations/search HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYzQwODU0NjZmNTRiYjNkYWI4MDM1OGVmYTc4Yjg2MThhNzdkZDEyMmJlOWMwZDlhZjFmNGEyOWFmNzIxZWM4MSJ9fSwiZXhwIjoxNjM2ODkyMDI4LCJpYXQiOjE2MzY4OTExMjgsIm5iZiI6MTYzNjg5MTEyN30.tLycfWMVZ4aGJLlCJgdm-VupYe-Rw3omRqy9b7ImiHVhWMczi9f3ctRHEeaArVCt6GnwclH4mu6ln3zTOS7lLw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 3a88ffba-be4a-44a6-9e40-3619bf837360
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 39}


Request Body1:{{
"latitude": 10,
"longitude": 20
}}
```


```
Request Headers2:{POST /locations/search HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYzQwODU0NjZmNTRiYjNkYWI4MDM1OGVmYTc4Yjg2MThhNzdkZDEyMmJlOWMwZDlhZjFmNGEyOWFmNzIxZWM4MSJ9fSwiZXhwIjoxNjM2ODkyMDI4LCJpYXQiOjE2MzY4OTExMjgsIm5iZiI6MTYzNjg5MTEyN30.tLycfWMVZ4aGJLlCJgdm-VupYe-Rw3omRqy9b7ImiHVhWMczi9f3ctRHEeaArVCt6GnwclH4mu6ln3zTOS7lLw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7ac8701d-7b02-4135-ad8c-9b5ef20d3a09
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 37}


Request Body2:{{
"latitude": 0,
"longitude": 0
}}
```


```
Request Headers3:{POST /locationsss/search HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTJUMjE6NTI6MzEuMzA4Mjc1KzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiYzQwODU0NjZmNTRiYjNkYWI4MDM1OGVmYTc4Yjg2MThhNzdkZDEyMmJlOWMwZDlhZjFmNGEyOWFmNzIxZWM4MSJ9fSwiZXhwIjoxNjM2ODkyMDI4LCJpYXQiOjE2MzY4OTExMjgsIm5iZiI6MTYzNjg5MTEyN30.tLycfWMVZ4aGJLlCJgdm-VupYe-Rw3omRqy9b7ImiHVhWMczi9f3ctRHEeaArVCt6GnwclH4mu6ln3zTOS7lLw
Content-Type: application/json
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 02bca519-988d-422d-a5b4-df053df4da85
Host: main-api.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 39}


Request Body3:{{
"latitude": 10,
"longitude": 20
}}
```






## Response

```
Response1:{
HTTP/1.1 200 OK
Date: Sun, 14 Nov 2021 11:59:12 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=p8LAP5So7c17zFhGzNjoItymoeXL51pqDQgao5%2FNBmCj365CBPnX6q9p6Obg8VAfQ94GaTWMHCcefeuy3gVxqVfb1zwaujotg%2FHyMKqQSnoixz3N4f3MDVdfsMCPn6r0wODuB%2BCu1GI%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae012873bfd5c26-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"place_id":282384302,"osm_type":"relation","osm_id":3106489,"lat":"10.7575596","lon":"20.6934116","display_name":"Salamat, Chad","address":{"house_number":"","road":"","suburb":"","city_district":"","region":"","postcode":"","country":"Chad","country_code":"td"},"boundingbox":["9.0830416","12.123","18.874","22.387222"]}}}
```

```
Response2:{
HTTP/1.1 400 Bad Request
Date: Sun, 14 Nov 2021 12:03:54 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=Q56T1DRR%2B1LHw6oD%2BYOaEwpKM9InKb5kUDEDargl6myWb01HojqJClPOYZ3jSICIlexhi0whzOOVztHPhaS4Lnt%2BdE4qtk2buQ59SVzRufX1RdxWSDz0xCj56IH%2F0fSs6hrrBDwRS7s%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae01968ef775c26-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"code=400, message=Key: 'CreateLocationRequest.Longitude' Error:Field validation for 'Longitude' failed on the 'required' tag\nKey: 'CreateLocationRequest.Latitude' Error:Field validation for 'Latitude' failed on the 'required' tag","payload":null}}
```

```
Response3:{
HTTP/1.1 404 Not Found
Date: Sun, 14 Nov 2021 12:06:51 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=aItUDY4R5xLTUk8INsi98A3KvoWabZjY76e%2BdZPEyt9e%2BfWDqs82xjaY6rs8FeqlQ%2B6Cc8964fDKgFUQou02vxoCL5yCiKUlig5JoZCDHrAnI0xIHxfOXqtXCS84msdMz8U0NYnDpqo%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6ae01db98dc25c26-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}
```




## Results
Success
