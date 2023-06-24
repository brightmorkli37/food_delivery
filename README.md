## Food Delivery App


## Project Setup:
Follow the instructions below to clone and run the project on your local computer;

### Disclaimer:
```This tutorial can be helpful for Windows Operating system based users. However is it tailored for any Linux distribution users.```


- Clone the project

```bash
git clone https://github.com/brightmorkli37/food_delivery.git
```
- cd into the project directory;
```bash
cd food_delivery/
```
   
- Create .env file in the project directory
- Copy the content of .env.example to .env and fill in the params

- Create a virtual environment to install project dependencies
```bash
 - python3 -m venv venv
 - source venv/bin/activate
 - pip install -r requirements.txt
```

## NB:
```Unlike pipenv that can load .env variables, python's default virtual environment creation cannot load environment variables. You would have to leverage on a package such as autoenv to load the .env variables. The quickest fix is to replace the values directly in the settings.py file```

Or using pipenv (https://pipenv.pypa.io/en/latest/) - Recommended

- Establish database connection by providing the database params in the .env file

## NB:
```For local testing purposes, the default database configuration can be used. It has been commented out in favor of the custom database settings. To use it, uncomment it and comment out the custom database settings. This can be done in the project settings file in project_root/settings.py```

- Run Migrations and Migrate 
```bash
- python manage.py makemigrations

- python manage.py migrate
```

- Run development Server
```bash
python manage.py runserver
```

- Local server is listening on localhost:8000 or 127.0.0.1:8000