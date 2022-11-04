# BananaOrange

# Table of contents

- [Project Description](#project-description)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Credits](#credits)

# Project Description

BananaOrange is a Learning Journey Planning System (LJPS) which aims to guide staff on courses they can take to assist them for their upcoming new positions or in a different area within the organisation.

# Technologies

### Frontend is created with:

- Bootstrap == 5.2.1

### Backend is created with:

- Python == 3.10.8
- Flask==2.0.3
- Flask-Cors==3.0.10
- Flask-SQLAlchemy==2.5.1
- requests==2.27.1
- SQLAlchemy==1.4.31
- Werkzeug==2.0.3
- Flask-MySQLdb==1.0.1
- mysql-connector==2.2.9
- mysql-connector-python==8.0.28
- mysqlclient==2.1.1

### Testing is created with:

- selenium==4.1.0
- webdriver-manager==3.5.4
- flask_testing==0.8.1

# Installation

1. Download and install WAMP/MAMP for Windows/Mac users respectively. Visit https://www.wampserver.com/en/download-wampserver-64bits/ for WAMP and https://www.mamp.info/en/downloads/ for MAMP.
2. Install Visual Studio Code (VSC). Visit https://code.visualstudio.com/download.
3. Install Live Server from VSC. Visit https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer.

# Usage

1. Start WAMP/MAMP and import LJPS_DB.sql (located at the root directory).
2. To run this project, install the libraries locally using pip:

```
$ pip install -r requirements.txt
```

3. To start backend services, run the following commands in terminal from root directory:

```
python backend/app.py
```

4. To start frontend services, click on the Live Server located at the bottom-right of Visual Studio Code.
   ![Alt text](assets/img/live-server.png?raw=true "Title")

5. The image shown below will be the starting page the of our website. You can select your role and login.
   ![Alt text](assets/img/indexpage.jpg?raw=true "Title")

### Learner

1. The image shown below will be the login page for Learner.
   ![Alt text](assets/img/learnerpage.jpg?raw=true "Title")

2. After logging in, you will be redirected to this main page.
   ![Alt text](assets/img/learnerhomepage.jpg?raw=true "Title")

This system allows learner to select a role they want and see a list of skills required. Learners also can see the courses they can take to acquire those skills, and add/remove them on their learning journey.

### HR/Admin

1. The image shown below will be the login page for HR/Admin.
   ![Alt text](assets/img/hrpage.jpg?raw=true "Title")

2. After logging in, you will be redirected to this main page.
   ![Alt text](assets/img/hrhomepage.jpg?raw=true "Title")

This system allows HR/Admin to view, create, update & remove job roles and skills. HR/Admin also can assign the skills to roles & skills to courses as required.

With this, you have successfully setup this project and please feel free to try out this project!

# Tests

This project has 3 different testing methods with their respective commands:

1. Unit Testing

```
python -m unittest tests/units/test_unit.py
```

2. Integration Testing

```
python -m unittest discover tests/integration
```

3. Frontend Testing

```
python -m unittest discover tests/frontend_test
```

# Credits

Special shoutout to the Prof. Swavek, Instructor Kong Ming and Boris for the guidance.
