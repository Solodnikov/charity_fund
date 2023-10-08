# charity_fund

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Static Badge](https://img.shields.io/badge/SQLAlchemy-yellow?style=for-the-badge)

<!-- добавить картинку -->

### Описание проекта

Приложение по поддержке благотворительных проектов фонда. В фонде может быть инициировано несколько благотворительных проектов. Пожертвования не имеют целовой направленности и распределяются по проектам (изначально поступают в проект, созданный ранее других).

### Развертывание проекта

* клонируйте проект

   `git clone git@github.com:Solodnikov/charity_fund.git`

* установите и запустите виртуальное окружение в папке проекта

    `python -m venv venv`

    `. venv/Scripts/activate`

* установите зависимости проекта

    `pip install -r requirements.txt`

### Запуск проекта

* создайте файл `.env` в корневой директории проекта:
    
    ```
    # .env example
    DATABASE_URL = sqlite+aiosqlite:///./fastapi.db
    SECRET = SECRET
    APP_TITLE = Благотворительный фонд (0.9.0)
    APP_DESCRIPTION = Сервис для организации сбора средств на разничные инициативы.
    ```

* ввести комманду в корневой директории проекта

    `uvicorn app.main:app --reload`

* cервис будет доступен по адресу

    `http://127.0.0.1:8000` - API

* автоматически сгенерированная документация Swagger

    `http://127.0.0.1:8000/docs`


