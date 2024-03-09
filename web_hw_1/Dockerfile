FROM python:3.11

# Встановимо змінну середовища
ENV BOT_HOME /web_hw_1

# Встановимо робочу директорію всередині контейнера
WORKDIR $BOT_HOME

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "main.py"]