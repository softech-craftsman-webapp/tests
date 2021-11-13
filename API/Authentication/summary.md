# Login process tests

## Successful login

### Exported postman test result
```
{
	"id": "a0b981a8-ad29-4142-a35e-ae3d9fabff78",
	"name": "Auth tests",
	"timestamp": "2021-11-13T12:33:13.312Z",
	"collection_id": "18048802-3f14596a-1e09-4ed4-a6c0-35a06cabdb49",
	"folder_id": 0,
	"environment_id": "0",
	"totalPass": 3,
	"totalFail": 0,
	"results": [
		{
			"id": "c1830f83-e389-47b5-9330-08dbdf8a07f4",
			"name": "/auth/login",
			"url": "https://auth.hiringo.tech/auth/login",
			"time": 532,
			"responseCode": {
				"code": 200,
				"name": "OK"
			},
			"tests": {
				"Status code is 200": true,
				"Body contains success": true,
				"Check user id": true
			},
			"testPassFailCounts": {
				"Status code is 200": {
					"pass": 1,
					"fail": 0
				},
				"Body contains success": {
					"pass": 1,
					"fail": 0
				},
				"Check user id": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				532
			],
			"allTests": [
				{
					"Status code is 200": true,
					"Body contains success": true,
					"Check user id": true
				}
			]
		}
	],
	"count": 1,
	"totalTime": 532,
	"collection": {
		"requests": [
			{
				"id": "c1830f83-e389-47b5-9330-08dbdf8a07f4",
				"method": "POST"
			}
		]
	}
}
```
### Test script

```
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Body contains success", function () {
    pm.expect(pm.response.text()).to.include("Success");
});

pm.test("Check user id", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.payload["id"]).to.eql("328863de-e2b0-4f9b-9900-cba9fabc2989");
});
```

## Unsuccessful login

### Exported postman test result
```
{
	"id": "b4c5f002-59e7-497c-9591-fc9c57bd3c6d",
	"name": "Auth tests",
	"timestamp": "2021-11-13T12:37:59.380Z",
	"collection_id": "18048802-3f14596a-1e09-4ed4-a6c0-35a06cabdb49",
	"folder_id": "18048802-0b087d3e-d9ee-42f1-a155-9e96dad65e8b",
	"environment_id": "0",
	"totalPass": 2,
	"totalFail": 0,
	"results": [
		{
			"id": "f8797687-c0c3-49c3-af06-0d67eaa0357a",
			"name": "/auth/login",
			"url": "https://auth.hiringo.tech/auth/login",
			"time": 283,
			"responseCode": {
				"code": 400,
				"name": "Bad Request"
			},
			"tests": {
				"Status code is 400": true,
				"Body matches string": true
			},
			"testPassFailCounts": {
				"Status code is 400": {
					"pass": 1,
					"fail": 0
				},
				"Body matches string": {
					"pass": 1,
					"fail": 0
				}
			},
			"times": [
				283
			],
			"allTests": [
				{
					"Status code is 400": true,
					"Body matches string": true
				}
			]
		}
	],
	"count": 1,
	"totalTime": 283,
	"collection": {
		"requests": [
			{
				"id": "f8797687-c0c3-49c3-af06-0d67eaa0357a",
				"method": "POST"
			}
		]
	}
}
```

### Test script
```
pm.test("Status code is 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("Email or password is invalid");
});
```