# fake_api_server
開發有需求時可以建立簡單的 API 回傳值



```
{
    "api_list": [{
            "name": "api1",
            "route": "/api1", // 設定 api 路徑，記得一定要以 / 作為開頭
            "method": ["GET"], // api 支援的類型
            "data": { // 要回傳的資料
                "status": 1,
                "something": "123"
            }
        },
        {
            "name": "api2",
            "route": "/api2",
            "method": ["GET", "POST"],
            "data": {
                "status": 1,
                "something": "123"
            }
        }
    ]
}

```
