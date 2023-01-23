### デプロイ

```bash
$ sls deploy --stage dev
```

### 実行

```bash
$ curl "https://{restapi_id}.execute-api.ap-northeast-1.amazonaws.com/dev/fizz-buzz" --header 'x-api-key:{指定のAPI Key}'

$ curl "https://{restapi_id}.execute-api.ap-northeast-1.amazonaws.com/dev/health-check" --header 'x-api-key:{指定のAPI Key}'  
```

### Unit Test

```bash
$ pip install -U pytest

$ pytest
```
