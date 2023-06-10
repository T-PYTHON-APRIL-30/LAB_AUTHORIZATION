# LAB_AUTHORIZATION


## Using what you've learned in Django MVT, ORM, Media,  Authentication and Authorization do the following:

## Create a Hospital Website , the hospital has the following :
- ( 1 ) Home page to display all the clinics in your hospital . 
- ( 2 ) detail page for clinics, when clicked the clinic detail page is displayed.
- ( 1 ) search page for clinics by name.
- ( 3 ) Manager page to manage the clinics (only a manager can access this page, 

use permissions and groups)

- ( 4 ) Add/update a clinic page (only managers can add/update) 
- ( 5 ) A page for managing the appointments (add/delete/update , 

only manager can access this page, use permissions and groups)


### A patient can do the following:
- ( 1 & 2 ) Browse the clinics and view the clinics's detail page.
- ( 6 ) View the previous appointments on the clinics's page.
- ( 7 ) Book an appointment with a date on that clinic.


### Models

# Done

- Clinic model should have
- - name
- - feature_image
- - description
- - department (use text choices field ) choices are : "Heart Center", "Neuroscience Center", "Obesity Center", "Eye Center", "Orthopedic Center", "Pediatric Center"
- - established_at

# Done

- Appointment Model
- - Relation with clinic
- - Relation with user
- - case_description
- - patient_age
- - appointment_datetime
- - is_attended (default is False, only manager can change this field True)


### Add user Accounts (register, login, logout)

# Done

- Add group in the Admin for Managers , and assign some users as manager
- Limit the access to adding a Clinic page to the users in the Managers group only.


### styling
- Use bootstrap CSS library or similar for styling the website . 
- Use some images to represent the hospital building and facilities as a gallery and display some general info.


### Bonus
When patient books an appointmnet with the clinic , check if the clinic is free on that date & time (that there is no previous appointment on the same date & time).
