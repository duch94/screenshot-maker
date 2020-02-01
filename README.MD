# How to run
Just use command `docker-compose down && docker-compose build && docker-compose up -d` 
to build and run a container with app. 

After that you can access 8080 port of it to make screenshots, for 
example: `http://localhost:8080/get_screenshot/1111_000.png` in browser or 
`curl 0.0.0.0:8080/get_screenshot/1111_000.png > 1111_000.png` in terminal.
