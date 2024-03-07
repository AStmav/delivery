# Базовый образ
FROM python:3.9

# Установка зависимостей
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копирование исходного кода приложения в контейнер
COPY . /app
WORKDIR /app

# Запуск приложения
CMD ["python", "delivery.py"]
