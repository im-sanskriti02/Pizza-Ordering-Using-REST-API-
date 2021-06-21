# Pizza-Ordering-Using-REST-API-

This is my Django app. I named the project as PizzaApp and app as myapp.

Steps to run this Project:


1. Clone this Repository on your desktop and follow the below steps.

2. Open the command prompt and go to desktop directory.

3. Actiavte the virtual enviroment in the file first, copy the given commemd in your command prompt

   Pizza-Ordering-Using-REST-API-/pizza/env/scripts 

   and hit enter, then type 
   
   activate

   and your virtual enviroment is activated.

3. Then Download the requriements from requirements.txt

   For that run this commend - pip install -r requirements.txt

4. Then come back to the PizzaApp folder by using 
   cd.. command twice.

5. Then open your MongoDB Compass and connect it with the server. Once it is connected with the server create a 
   new Database and name it as 'PizzaApp' and name the collection as 'PizzaCollection' 

6. Then come back to the command prompt and run the following commands simultaneously.
   
   python manage.py makemigrations
   python manage.py migrate

7. Then open the MongoDB Compass again and refresh it and you will see a bunch of pizza available in the database.

   (If MongoDB is not getting connected please read the step mention in last of this file.)

8. Now to move further come back to command prompt and run command 

   python manage.py runserver

9. Once the server is up and running, go to your browser and open localhost address by the following command

   127.0.0.1:8000/view 


I have created 3 endpoints in this Django App

1. 127.0.0.1:8000/view - This endpoint will list all the stored pizza in database. You can also use filter 
   for listing the pizza based on type and size.
   
2. 127.0.0.1:8000/create - This endpoint will allow you to customize a pizza for yourself. It has
   Name, Type, Size, and Toppings fields. To select multiple options in toppings please use 'shift' and hit POST.
   If you wish to delete or make changes in pizza run the next command.

3. 127.0.0.1:8000/<id> - To view the full detail of a pizza enter the 'pizza id' in place of id in endpoint.
   You can also edit or delete details of pizza here.


In case MongoDB Compass is not working I recommend you to use the default sqlite database.

To use default database follow the steps:

1. Open settings.py file present in PizzaApp folder in your code editor.
   Then scroll down and search for DATABASES in the file. You will found the commented codes of sqlite3. Remove the docstrings from those code and put the docstrings on the MongoDB codes.

2. Then come to command prompt and run the following commands one by one. 

   python manage.py makemigrations
   python manage.py migrate

3. Now create the superuser by running the command given below and enter the details 

   python manage.py createsuperuser

4. Now run your server with 
   
   python manage.py runserver

5. Now go to the admin panel and login to the panel
   
   127.0.0.1:8000/admin

6. You will see a table name Pizzas listing the pizzas available in database.
