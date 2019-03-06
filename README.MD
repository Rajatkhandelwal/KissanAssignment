# Creating a RESTful API with Django

## Getting Started

### Pre-Step
1. Clone this repository into directory and will get KissanAssignment folder.
2. Go to KissanAssignment and find manage.py.
3. Run ```python manage.py makemigrations``` in terminal, will create lines of code, help in creating actual fields in your respective database similar to SQL statements.
4. Run ```python manage.py migrate``` in terminal by which model fields will be reflected in database if there are no errors in statement.
5. Create a super user for database by typing command ```Python manage.py createsuperuser``` give your name, email and password for that user. 

Note: if you are facing an error while creating Superuser "creation skipped due to not running in a TTY, Then use `winpty python manage.py createsuperuser`.  

### Run Server
1. Go to KissanAssignment folder and find manage.py.
2. Type ```python manage.py runserver``` in terminal which will start application on 8000( default ) port.
3. Open your browser and type http://localhost:8000/admin which will take you admin page and ask your username and password given in step 5 of pre-Step. 

After successfully login, you will be able to see 3 table for MaxTemp , MinTemp and Rainfalls having no data. 

### Saving
1. Go to KissanAssignment and find manage.py.
2. Type ```python manage.py createdatabase``` in same directory which will fetch data from given weather api's and dump the data into database. 
3. Refresh admin page in browser and can see the data in all 3 tables.

### Fetching from DB
Type http://localhost:8000/weather/getListData?type=Tmax&location=UK&start_date=1910-01-15&end_date=2019-02-25 in your browser and get data as per your given parameter.
  - location value should be one value from UK, England, Scotland and Wales.
  - type value should be either Tmax or Tmin or Rainfall.
  - start_date from which date, data is needed.
  - end_date till which date, data is required. 

### Prerequisites

* [django](https://www.djangoproject.com/) - 2.0
* [python](https://www.python.org/) 3.6.5
* [restframework](https://www.django-rest-framework.org/) 3.9.1

### Plugins
Instructions on how to use them in your own application are linked below.
| Plugin | README |
| ------ | ------ |
| Django | https://github.com/django/django/blob/master/README.rst |
| restframework | https://github.com/encode/django-rest-framework/blob/master/README.md |

## Acknowledgments

* Django Documentation
* Stackoverflow

