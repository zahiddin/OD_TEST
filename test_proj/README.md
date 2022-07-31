#ЧТОБЫ ЗАПУСТИТЬ ПРОЕКТ ЛОКАЛЬНО НА ДОКЕРЕ:

После того как проект уже спулен с гита
1. в главной директории проекта создать файл .env и вписать следующие ключи:
            
            ALLOWED_HOSTS='*'
            DEBUG=on
            SECRET_KEY=ice2ouq4w901zww@1yl(-ljw(6_tonrly8qbj5l_r-aic6uind
            DATABASE_URL=psql://postgres_user:postgres_password@db:5432/database_name
            EMAIL_HOST_USER='почта@mail.ru' #обязаиельно mail.ru
            EMAIL_HOST_PASSWORD='Уникальный пароль для приложения mail.ru' '''если нет то создать приложение и выданный пароль вписать в ключ EMAIL_HOST_PASSWORD, подробнее на https://help.mail.ru/mail/security/protection/external'''

2. немного подправить docker-compose.yml файл, вписать сюда те же значения что и в DATABASE_URL ключе в созданном локально .env файле:
            
            POSTGRES_DB=database_name
            POSTGRES_USER=postgres_user
            POSTGRES_PASSWORD=postgres_password

3. находясь на директории где расположен docker-compose.yml файл то есть /test_proj, запустить docker compose командой: 
            
            docker compose up --build -d

4. зайти в контейнер od_test_proj и создать там суперюзера:
            
            python3 manage.py createsuperuser

5. все апишки доступны по ссылке:
            
            http://0.0.0.0:8000/swagger/
            
ПРИМЕЧАНИЕ: Чтобы использовать апишку http://0.0.0.0:8000/searchstudents/ для поиска студентов, надо отправить пост запрос с querry param в постмане. в params ввести search = 'Азамат' либо в самой апишке например http://0.0.0.0:8000/searchstudents/?search=Azamat


#ЧТОБЫ ЗАПУСТИТЬ ПРОЕКТ ЛОКАЛЬНО ИСПОЛЬЗУЯ VIRTUALENV:


*После того как проект уже спулен с гита*

1. создать виртуальное окружение
            
            python3 -m venv venv

2. активировать виртуальное окружение
            
            source venv/bin/activate

3. находясь внутри виртуального окружения, установить пакеты проекта
            
            pip install -r requirements.txt

4. в главной директории проекта создать файл .env и вписать следующие ключи:

ALLOWED_HOSTS='*'
DEBUG=on
SECRET_KEY=ice2ouq4w901zww@1yl(-ljw(6_tonrly8qbj5l_r-aic6uind
DATABASE_URL=psql://postgres_user:postgres_password@localhost:5432/database_name
EMAIL_HOST_USER='почта@mail.ru' #обязаиельно mail.ru
EMAIL_HOST_PASSWORD='Уникальный пароль для приложения mail.ru' '''если нет то создать приложение и выданный пароль 
вписать в ключ EMAIL_HOST_PASSWORD, подробнее на https://help.mail.ru/mail/security/protection/external'''

4. миграции
            
            python3 manage.py migrate

5создать суперюзера
            
            python3 manage.py createsuperuser

6. запустить на локальном сервере
            
            python3 manage.py runserver


