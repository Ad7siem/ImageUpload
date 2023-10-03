Launching the application

in the console
- venv\Scripts\activate
- cd image
- py manage.py runserver

Open url localhost
localhost:8000/admin
login: admin password: admin

App url: localhost:8000

Two users have been created:
admin - Enterprise
B - Basic (password: 200Basic)

When creating a new user, you must first assign a profile to them before starting to upload images. You can assign a profile either through the administration page or in the application using the link "http://localhost:8000/profile/".

In the "show_all_images" tab, "http://localhost:8000/show_all_images/", you can view all the photos. Clicking on an image link will open its content in the appropriate resolution.
