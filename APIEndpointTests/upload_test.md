url:{https://storage.hiringo.tech/files/upload}



Request1:{POST /files/upload HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiODgzMDI0ZTZiYTIwNmM4NDQ2YjQ4ZjFkMjUyMWEzYmM2MGJhOWRmNTUwZDU1ODc5MDBlYThmM2VkMzY1NjQwZSJ9fSwiZXhwIjoxNjM2NzA5NjQ0LCJpYXQiOjE2MzY3MDg3NDQsIm5iZiI6MTYzNjcwODc0M30.t6CKS8_h03SvcPMTlJiPIV7AmrrRrmPApZXZSdpI89gRTSQwTeH79t0oLSfH2eBZQ_82vGvMbhV2K0i18P7KTQ
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 19893891-6162-4424-994e-8f26cc28a4ee
Host: storage.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------138574291922893044654299
Content-Length: 806557
 
----------------------------138574291922893044654299
Content-Disposition: form-data; name="file"; filename="-val-vel.pdf"
<-val-vel.pdf>
----------------------------138574291922893044654299--}



Response1:{
HTTP/1.1 201 Created
Date: Fri, 12 Nov 2021 09:19:36 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=iFiZqN%2BwXD4A92nXkZLZFA9Wc6kkhdLoErkmDnn6%2BCp8belQnWgpmqkqlVGeQGGVyLv%2BXdW7SRJaj9CXtB3z1yrrN1iC1jMkE9a4L8arLkpiCV3tthQcfo8jrU%2BpdOLM0aKNSXNMGA%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aceade5ebfa061c-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":true,"message":"Success","payload":{"name":"e8c8d5fd-9c84-45b4-ba6f-485bde44e1ea.pdf","url":"https://api.hiringo.tech/files/dbe52b25-2024-451b-acca-b7a6f5258620/e8c8d5fd-9c84-45b4-ba6f-485bde44e1ea.pdf","type":"application/pdf","size":"806.3 kB"}}}






Request2:{POST /files/upload HTTP/1.1
Authorization: Bearer 111111
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: dc90209a-19f4-47e2-808d-e5a73c7c5b94
Host: storage.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------116814844694160548832929
Content-Length: 806557
 
----------------------------116814844694160548832929
Content-Disposition: form-data; name="file"; filename="-val-vel.pdf"
<-val-vel.pdf>
----------------------------116814844694160548832929--}





Request2:{HTTP/1.1 401 Unauthorized
Date: Fri, 12 Nov 2021 09:27:24 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=b9Lknj86Qa3QH4EOmVSzz%2FDL40PaeaiMJg7goiw2PbhHdejkJ1BEitG4EiQFhKBdZmf8%2BzM5AZl%2F7kAb%2ByAEXV6is%2FvsWbnqOwQdwjx%2Fy2RKBVz%2FOpbWjjR%2Fek6snUelWFaMY1ipjw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aceb9680d434a97-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"invalid or expired jwt, internal=token contains an invalid number of segments","payload":null}
}






Request3:{POST /files/uploadfiles HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMxZGIwNTk0NDE4MmZjYWJlZTEzNTUyNzgwOWIzZTNhYzVjZjQ5NGVhZjU2ZGVhMzRmMjRlNmMwZTU3ZmQ3MyJ9fSwiZXhwIjoxNjM2NzEwNTU1LCJpYXQiOjE2MzY3MDk2NTUsIm5iZiI6MTYzNjcwOTY1NH0.XtNDfMoIXAAd-ElqU6ua_LWJqPfMHPoHXmz5tOVmbYyO3QjcJgFX0sd95MH8JKmRFT06R51tYVQjK8CM6qLjLw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 177f52b9-7c3f-4015-907d-6a7dd12169f4
Host: storage.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------836030729371364363493641
Content-Length: 806557
 
----------------------------836030729371364363493641
Content-Disposition: form-data; name="file"; filename="-val-vel.pdf"
<-val-vel.pdf>
----------------------------836030729371364363493641--}






Response3:{HTTP/1.1 404 Not Found
Date: Fri, 12 Nov 2021 09:35:00 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=lTugDFZiOIbWZKVYb6GYt7kdl%2BWautUymdsGn0ZB92d%2FCpLp5k9svAefT7kjUmdOXAjDC31SVQtyYRMXcp5ZZhwufhsq3C9iZj%2Bt5kqMegJQ%2Bjl04huNK22rluboeMYmyaiadgAbGw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6acec4899db7c277-FRA
Content-Encoding: br
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"Not Found","payload":null}}






Request4:{POST /files/upload HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMxZGIwNTk0NDE4MmZjYWJlZTEzNTUyNzgwOWIzZTNhYzVjZjQ5NGVhZjU2ZGVhMzRmMjRlNmMwZTU3ZmQ3MyJ9fSwiZXhwIjoxNjM2NzEwNTU1LCJpYXQiOjE2MzY3MDk2NTUsIm5iZiI6MTYzNjcwOTY1NH0.XtNDfMoIXAAd-ElqU6ua_LWJqPfMHPoHXmz5tOVmbYyO3QjcJgFX0sd95MH8JKmRFT06R51tYVQjK8CM6qLjLw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: 7af661f2-cedf-46ff-acf9-326ee94594b5
Host: storage.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------397912526100579535084375
Content-Length: 94560
 
----------------------------397912526100579535084375
Content-Disposition: form-data; name="file"; filename="epidemic2021.rtf"
<epidemic2021.rtf>
----------------------------397912526100579535084375--}




Response4:{HTTP/1.1 406 Not Acceptable
Date: Fri, 12 Nov 2021 09:47:26 GMT
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
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=ZbxiXoMhcb8UvqqDXfs7qj3rzczmTUkj6BybiJuzxnVaTm8aGobxmZbyO3nPhor3QdgEd3Hagq0I7s1IFw5Z%2Bz0DxvykLl9t5vmOM%2Buo%2BH%2BwOzwaBV%2Feuy6QXkmcMr0VKX9fFJoHDw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aced6c15f876993-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
{"success":false,"message":"File is not permitted to upload","payload":null}}






Request5:{POST /files/upload HTTP/1.1
Authorization: Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjYzMTJhNzgtMWY5ZS00ZDc4LWE5ZmItMjMxZTg0OTY3ZjYwIiwibmFtZSI6IlJhY2hlbCIsImVtYWlsIjoieHh4eEBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZF9hdCI6bnVsbCwiY3JlYXRlZF9hdCI6IjIwMjEtMTEtMDJUMDk6NDc6MjEuOTE3NTgyKzAxOjAwIiwidXBkYXRlZF9hdCI6IjIwMjEtMTEtMTFUMjA6MTA6NTYuMDAxODAyKzAxOjAwIiwiYXV0aCI6eyJpZCI6Ijk1YTUxYTNmLTU2ZmEtNDg4OS1iZjgwLTNjNTdkMDU0YjFjMiIsInRva2VuIjoiZmMxZGIwNTk0NDE4MmZjYWJlZTEzNTUyNzgwOWIzZTNhYzVjZjQ5NGVhZjU2ZGVhMzRmMjRlNmMwZTU3ZmQ3MyJ9fSwiZXhwIjoxNjM2NzEwNTU1LCJpYXQiOjE2MzY3MDk2NTUsIm5iZiI6MTYzNjcwOTY1NH0.XtNDfMoIXAAd-ElqU6ua_LWJqPfMHPoHXmz5tOVmbYyO3QjcJgFX0sd95MH8JKmRFT06R51tYVQjK8CM6qLjLw
User-Agent: PostmanRuntime/7.28.4
Accept: */*
Postman-Token: b77b6ece-4a53-4a5e-9df1-948da74ba160
Host: storage.hiringo.tech
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: multipart/form-data; boundary=--------------------------055336249814469268201576
Content-Length: 19281786
 
----------------------------055336249814469268201576
Content-Disposition: form-data; name="file"; filename="04_execution_of_parallel_block.mp4"
<04_execution_of_parallel_block.mp4>
----------------------------055336249814469268201576--}




Response5:{HTTP/1.1 413 Payload Too Large
Date: Fri, 12 Nov 2021 09:43:48 GMT
Content-Type: text/html
Transfer-Encoding: chunked
Connection: keep-alive
CF-Cache-Status: DYNAMIC
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=h2HnKCK6wut8D0zIQAdj4sU0yWlvRTotrYUOrNcnxKqWWsSqxNylRu0fjQ1NrK16vH%2BAlvbQ9KQqGV33lv219CGc%2FONfPSz9jvTSwbwHIaX01%2F9kelYoK5AvCNp1FUNj6OW4AAuJOw%3D%3D"}],"group":"cf-nel","max_age":604800}
NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
Server: cloudflare
CF-RAY: 6aced0a91e526993-FRA
alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400, h3-28=":443"; ma=86400, h3-27=":443"; ma=86400
 
<html>
<head><title>413 Request Entity Too Large</title><script async src='/cdn-cgi/challenge-platform/h/g/scripts/invisible.js'></script></head>
<body>
<center><h1>413 Request Entity Too Large</h1></center>
<hr><center>nginx</center>
<script type="text/javascript">(function(){window['__CF$cv$params']={r:'6aced0a91e526993',m:'mPpqTfVvEV7yiQi79ygCdvVwwKT3qdedoPeOxnGj1P0-1636710228-0-AdwHapQyIcXoZRffNb1U55byzMJXVxchD15OaR1r5JmGjfq+bEZb+Behyr5J1Ek/DeCnZ1cMaeGiRyG4p5eapct+ju+3cyQyFtIeWAHZcQmFP7aF46G8gVgwA/OnSGBdjA==',s:[0x3524d6cab4,0xf99fd07189],u:'/cdn-cgi/challenge-platform/h/g'}})();</script><script defer src="https://static.cloudflareinsights.com/beacon.min.js" data-cf-beacon='{"rayId":"6aced0a91e526993","version":"2021.11.0","r":1,"token":"e35d8ae2966940cb83b28fa95a52c624","si":100}' crossorigin="anonymous"></script>
</body>
</html>}