# Тестовый бот, который готовился для мастер-класса

Для запуска бота у себя вам нужно:
- установленный [Python3](https://www.python.org/downloads/),
- полученные [ключи приложения](https://my.telegram.org/apps),
- зарегистрированный бот через [@botfather](https://t.me/botfather)


Далее по шагам:
1. Клонируем репозиторий к себе и заходим в папку проекта:
```sh
git clone https://github.com/makehtml/mk-telegram-bot.git && cd mk-telegram-bot
```

2. Устанавливаем виртуальное окружение и активируем:
```sh
python3 -m venv .venv
source .venv/bin/activate
```

3. Ставим зависимости проекта:
```sh
pip install -r requirements.txt
```

4. Копируем файл с переменными окружения и заполняем своими данными:
```sh
cp .env_example .env
```
Либо просто настраиваем переменные окружения `API_ID`, `API_HASH` и `BOT_TOKEN`

5. Запускаем бота:
```sh
python echobot.py
```
