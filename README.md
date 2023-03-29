<div align="center">
  <h1>Django Contact Form</h1>
</div>

<div align="justify">

   Our project is a **"Contact Us Form"** for a website that allows users to contact us by sending a message to our Gmail.

   In addition, to protect against spam, a mechanism has been introduced that limits the number of messages sent to one message every two minutes.

   Form field validation has been performed on the client side, which helps prevent messages from being sent with incorrectly filled fields.

   *Technologies used: Django, HTML, CSS, JavaScript.*

</div>

<br><br>

<div align="center">

# Settings
✨ To use it, you need to complete the following steps:

<br>


<div align="left">

1. Clone this repository

   ```
      git clone https://github.com/lazycatcoder/django-contact-form.git
   ```

2. Open a terminal and navigate to the project **'contact-form-django'** folder

   ```
      cd path/.../contact-form-django
   ```

3. Create a virtual environment in the **'contact-form-django'** folder
   
   ```
      python -m venv venv
   ```

4. Activate the virtual environment

   ```
      source venv/bin/activate   # MacOS/Linux 

      venv\Scripts\activate      # Windows
   ```

5. Install **Django**

   ```
      pip install Django
   ```

6. Use the console to navigate to the **'contact-form-django\contact_form'** folder

   ```
      cd contact_form
   ```

7. Make migration

   ```
      python manage.py migrate
   ```

8. Navigate to folder **'contact-form-django\contact_form\contact_form'**
and open the **settings.py** file.

   The next step is to fill in some data in **settings.py**:
   
* Generating a new *SECRET_KEY* in **Django**

   ```
      python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

   This command will execute a Python script that imports the *get_random_secret_key()* function and calls it to generate a new key. The result will be printed in the terminal.

   When you get the new key, copy it and paste it into **settings.py** instead of *SECRET_KEY = ' '*

* Іnsert your *Email* and *App password*

   ```
      EMAIL_HOST_USER = 'youremail@gmail.com'
      EMAIL_HOST_PASSWORD = 'yourpassword'
   ```

   You can get the *app password* in your Google account:
   https://myaccount.google.com/apppasswords

9. Navigate to the **'contact-form-django\contact_form\emailapp'** folder and paste your email in the **views.py** file

   ```
      ['youremail@gmail.com'],
   ```

9. Use the console to navigate to the **'contact-form-django\contact_form'** folder and run the server 

   ```
      python manage.py runserver
   ```

11. Open a browser and enter the following address
launch of the project 🚀 https://127.0.0.1/contactus/

</div>


<br>


### 🔧 Additional Information

<div align="justify">

🔴 The project implements antispam protection that allows you to send the form once every 2 minutes, if necessary, change the *time threshold* parameter, you can navigate to the folder **'contact-form-django\contact_form\emailapp'**, open the **middleware.py** file and change value
   
   ```
      self.time_threshold = 120 
   ```

</div>