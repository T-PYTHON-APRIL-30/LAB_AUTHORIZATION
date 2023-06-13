# LAB_AUTHORIZATION


## Using what you've learned in Django MVT, ORM, Media,  Authentication and Authorization do the following:

## Create a Hospital Website , the hospital has the following :
- Home page to display all the clinics in your hospital .###
- detail page for clinics, when clicked the clinic detail page is displayed.###
- search page for clinics by name.###
- Manager page to manage the clinics (only a manager can access this page, use permissions and groups)###
- Add/update a clinic page (only managers can add/update) ###
- A page for managing the appointments (add/delete/update , only manager can access this page, use permissions and groups)


### A patient can do the following:
- Browse the clinics and view the clinics's detail page.##
- View the previous appointments on the clinics's page.
- Book an appointment with a date on that clinic.##


### Models###

- Clinic model should have
- - name
- - feature_image
- - description
- - department (use text choices field ) choices are : "Heart Center", "Neuroscience Center", "Obesity Center", "Eye Center", "Orthopedic Center", "Pediatric Center"
- - established_at



- Appointment Model
- - Relation with clinic
- - Relation with user
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended (default is False, only manager can change this field True)


### Add user Accounts (register, login, logout)###
- Add group in the Admin for Managers , and assign some users as manager###
- Limit the access to adding a Clinic page to the users in the Managers group only.


### styling###
- Use bootstrap CSS library or similar for styling the website . 
- Use some images to represent the hospital building and facilities as a gallery and display some general info.


### Bonus
When patient books an appointmnet with the clinic , check if the clinic is free on that date & time (that there is no previous appointment on the same date & time).
