ЧТОБЫ ЗАПУСТИТЬ ПРОЕКТ ЛОКАЛЬНО НА ДОКЕРЕ:

*После того как проект уже спулен с гита*

в главной директории проекта создать файл .env и вписать следующие ключи:

* ALLOWED_HOSTS='*'
* DEBUG=on
* SECRET_KEY=ice2ouq4w901zww@1yl(-ljw(6_tonrly8qbj5l_r-aic6uind
* DATABASE_URL=psql://postgres_user:postgres_password@db:5432/database_name
* EMAIL_HOST_USER='почта@mail.ru' обязаиельно mail.ru
* EMAIL_HOST_PASSWORD='Уникальный пароль для приложения mail.ru' если нет то создать приложение и выданный пароль 
вписать в ключ EMAIL_HOST_PASSWORD, подробнее на https://help.mail.ru/mail/security/protection/external

запустить docker compose командой

 docker compose up --build -d



ЧТОБЫ ЗАПУСТИТЬ ПРОЕКТ ЛОКАЛЬНО ИСПОЛЬЗУЯ VIRTUALENV:


*После того как проект уже спулен с гита*

создать виртуальное окружение
1. python3 -m venv venv

активировать виртуальное окружение
2. source venv/bin/activate

находясь внутри виртуального окружения, установить пакеты проекта
3. pip install -r requirements.txt

в главной директории проекта создать файл .env и вписать следующие ключи:

* ALLOWED_HOSTS='*'
* DEBUG=on
* SECRET_KEY=ice2ouq4w901zww@1yl(-ljw(6_tonrly8qbj5l_r-aic6uind
* DATABASE_URL=psql://postgres_user:postgres_password@localhost:5432/database_name
* EMAIL_HOST_USER='почта@mail.ru' обязаиельно mail.ru
* EMAIL_HOST_PASSWORD='Уникальный пароль для приложения mail.ru' если нет то создать приложение и выданный пароль 
вписать в ключ EMAIL_HOST_PASSWORD, подробнее на https://help.mail.ru/mail/security/protection/external

миграции
4. python3 manage.py migrate

создать суперюзера
5. python3 manage.py createsuperuser

запустить на локальном сервере
6. python3 manage.py runserver


