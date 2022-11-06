# Simple-Sig
Simple Signature to secure your website's traffic with backend validation api

#### Usage example
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/xtekky/Simple-Sig/src/sig.js"></script>
    <title>sig demo</title>
  </head>
  <body>
    <button type="button" id="test">test</button>
    <script src="/assets/js/index.js"></script>
  </body>
</html>
```

```js
$('#test').click(function() {
    data = 'username=grgrg&password=1234'

    fetch("/test", {
        headers: {
            ...x(data),
        },
        body   : data,
        method : "POST",
        mode   : "cors",
  });
});
```
#### Backend (verification api)
```curl
curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 156' -H 'Content-Type: application/json' -H 'User-Agent: python-requests/2.28.1' -d '{"x-kspx-00": "x-kspx-00 HEADER", "x-tx-00": "x-tx-00 HEADER", "data": "POST DATA"}' https://sig.xtekky.repl.co/verify

```
- response :

```json
{
  "is_valid": True/False,
  "tts": time elapsed since sig creation (you can then define a limit so sig cant be used again)
}

```

#### Heavy obfuscation - fast execution
![image](https://user-images.githubusercontent.com/98614666/200146256-5c713947-2d26-43db-94ee-a028225c3193.png)
