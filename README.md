# Delivery 

Сервис который позволяет назначать заказы курьерам на основе их текущего местоположения.

## Запуск

Чтобы запустить сервис, выполните следующие шаги:

1. Установите Docker, если он еще не установлен.
2. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/AStmav/delivery.git
    ```

3. Перейдите в каталог проекта:

    ```bash
    cd delivery
    ```

4. Соберите Docker контейнер:

    ```bash
    docker build -t delivery .
    ```

5. Запустите Docker контейнер:

    ```bash
    docker run -it delivery python delivery.py --couriers 1 "55.750717 37.617660" 2 "55.754535 37.621625" 3 "55.752231 37.620697" --order 55.751244 37.618423 55.753930 37.620795 7
    ```

## Использование

Вы можете использовать команды Docker для запуска сервиса и передачи различных параметров для назначения заказов курьерам.

Пример запроса:

Здадаются координаты метосоположения  3-х доставщиков, а также координаты точки А и точки B  заказа с указанием цены заказа. 

```bash
docker run -it delivery python delivery.py --couriers 1 "55.750717 37.617660" 2 "55.754535 37.621625" 3 "55.752231 37.620697" --order 55.751244 37.618423 55.753930 37.620795 7
```
Ответ:

```bash
Order assigned to courier 1, distance: 0.04706952407522667 kilometers
Order location: (55.751244, 37.618423)
```
Заказ взял 1 курьер , указано расстояние между курьером и точкой A .


Дополнительные примеры запросов для тестов:

```bash
docker run -it delivery python delivery.py --couriers 1 "55.750717 37.617660" 2 "55.754535 37.621625" 3 "55.752231 37.620697" 4 "55.760123 37.611234" 5 "55.758976 37.623456" 6 "55.756789 37.619876" 7 "55.754321 37.618765" 8 "55.752543 37.624567" 9 "55.750987 37.622345" 10 "55.751234 37.620987" --order 55.751244 37.618423 55.753930 37.620795 7
```
Заказ возьмет 1 курьер

```bash
python delivery.py --couriers 1 "55.752530 37.616340" 2 "55.754278 37.620101" 3 "55.751975 37.622312" 4 "55.752836 37.617899" 5 "55.753908 37.619821" 6 "55.750925 37.618444" 7 "55.751240 37.620453" --order 55.751244 37.618423 55.753930 37.620795 7
```
Заказ возьмет 6 курьер






