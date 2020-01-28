# Зачем:
Чтобы автоматизировать работу человека, который 
-> вручную ходит по страничке с результатами анализа BI данных
-> делает скриншоты разных частей этой страницы 
-> отправляет их в глип

# Что:
* Даёшь на вход урлу (пост запрос) и таргетинг элемента на странице (html class id, например, или позиционно в пикселях)
* Оно отдаёт на выход картинку: 
  * скрин этого элемента на странице, которая вернулась по пост запросу, 
  * то есть нужно отрендерить страницу будет, сделать скрин и crop image

# Как:
* Запускаться будет в докере
* Нужен python3
* Микросервис с эндпоинтами:
  * `/get_screenshot/<date_start>/<date_end>/`