# How to run
Just use command `docker-compose down && docker-compose build && docker-compose up -d` 
in this directory to build and run a container with app. 

After that you can access 8080 port of it to make screenshots, for 
example: 
```
curl -X POST \
-H "Content-Type: application/json" \
-d '{"url": "http://yandex.ru", "actions": [{"action": "set_resolution", "width": 1920, "height": 1080}, {"action": "screenshot_element", "selector": "html"}]}' \
0.0.0.0:8080/order_screenshot 
``` 
