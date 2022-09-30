import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from os import environ

# Flask App and DB connection is done here.
app = Flask(__name__)   
# ---for windows---
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/LJPS_DB'
# ---for mac---
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/LJPS_DB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}


CORS(app)
db = SQLAlchemy(app)

#skill = Skill.query.all()
<<<<<<< HEAD

#Job Role (For LJPS)
class JobRole(db.Model):
    __tablename__ = 'job_role'
    job_role_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_role_name = db.Column(db.String(50), nullable=False)
    job_role_desc = db.Column(db.String(255), nullable=False)
    job_role_status = db.Column(db.Integer, nullable=False)
    def __init__(self, job_role_name,  job_role_desc, job_role_status):
        if not isinstance(job_role_name, str):
            raise TypeError("job_role_name must be a string")
        if not isinstance(job_role_desc, str):
            raise TypeError("job_role_desc must be a string")
        if not isinstance(job_role_status, int):
            raise TypeError("job_role_status must be an integer")
        self.job_role_name = job_role_name
        self.job_role_desc= job_role_desc
        self.job_role_status = job_role_status

    def json(self):
        return  {
            "job_role_id": self.job_role_id, 
            "job_role_name": self.job_role_name, 
            "job_role_desc":self.job_role_desc,
            "job_role_status": self.job_role_status
        }


=======
>>>>>>> 2973a42efc078b1d42bf7d514f3f8b3137ef5ade

#Job Role (For LJPS)
class JobRole(db.Model):
    __tablename__ = 'job_role'
    job_role_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_role_name = db.Column(db.String(50), nullable=False)
    job_role_desc = db.Column(db.String(255), nullable=False)
    job_role_status = db.Column(db.Integer, nullable=False)
    def __init__(self, job_role_name,  job_role_desc, job_role_status):
        if not isinstance(job_role_name, str):
            raise TypeError("job_role_name must be a string")
        if not isinstance(job_role_desc, str):
            raise TypeError("job_role_desc must be a string")
        if not isinstance(job_role_status, int):
            raise TypeError("job_role_status must be an integer")
        self.job_role_name = job_role_name
        self.job_role_desc= job_role_desc
        self.job_role_status = job_role_status

    def json(self):
        return  {
            "job_role_id": self.job_role_id, 
            "job_role_name": self.job_role_name, 
            "job_role_desc":self.job_role_desc,
            "job_role_status": self.job_role_status
        }
        
class Skill(db.Model):
    __tablename__ = 'Skill'
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    skill_desc = db.Column(db.String(255), nullable=False)
    skill_status = db.Column(db.Integer, nullable=False)
    def __init__(self, skill_name, skill_desc, skill_status):
        if not isinstance(skill_name, str):
            raise TypeError("skill_name must be a string")
        if not isinstance(skill_desc, str):
            raise TypeError("skill_desc must be a string")
        if not isinstance(skill_status, int):
            raise TypeError("skill_status must be an integer")
        self.skill_name = skill_name
        self.skill_status = skill_status
        self.skill_desc = skill_desc

    def json(self):
        return  {
            "skill_id": self.skill_id, 
            "skill_name": self.skill_name, 
            "skill_desc": self.skill_desc,
            "skill_status": self.skill_status
        }
@app.route("/")
def home():
    pass

#This segment of code is to do creation of roles. Only used by HR/admin.
#Takes in job_role_name and job_role_desc
# job_role_status 0 means active
@app.route("/createJobRole", methods=['POST'])
def create_job_role(test_data = ''):
    data = None
    if test_data == '':
        data = request.get_json()
        new_job_role = JobRole(data['job_role_name'], data['job_role_desc'],0)
        try:
            db.session.add(new_job_role)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "job_role_name": data['job_role_name']
                    },
                    "message": "An error occurred creating the job role."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_job_role.json(),
                "message": "Job Role successfully created"
            }
        ), 201
    else:
        new_job_role = JobRole(test_data['job_role_name'], test_data['job_role_desc'],0)
        return jsonify(
                {
                    "code": 201,
                    "data": new_job_role.json(),
                    "message": "Job Role successfully created"
                }
            ), 201
    
#This segment of code is to do retrieval of all the existing roles. Used by both HR and Learner.
@app.route("/getAllJobRole")
def getAllJobRole(test_data= ""):
    jobRoles = None
    if test_data == "":
        jobRoles = JobRole.query.all()
    if test_data != "": 
        return jsonify(
                {
                    "code": 200,
                    "data": 
                    [roles.json() for roles in test_data]
                }
            )
    elif jobRoles != None:
        return jsonify(
                {
                    "code": 200,
                    "data": 
                    [roles.json() for roles in jobRoles]
                }
            )
#skill = Skill.query.all()

@app.route("/getskills")
def getskills(test_data= ""):
    skills = None
    if test_data == "":
        skills = Skill.query.all()
    if test_data != "":
        return jsonify (
            {
                "code": 200,
                "data": 
                [skill.json() for skill in test_data]
            }
        )
    elif skills != None:
        return jsonify(
                {
                    "code": 200,
                    "data": {
                        "skill": [skill.json() for skill in skills]
                    }
                }
            )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "No skills found."
            }
        )

#This segment of code is update details of a selected skill
#=============== Update Skill details by skill_id======================================
@app.route("/createSkills", methods=['POST'])
def createSkills(test_data=""):
    data = None
    if test_data == "":
        data = request.get_json()
    else:
        data = test_data
    skill_name, skill_desc, skill_status = "", "", ""
    if data['skill_name']:
        skill_name = data['skill_name']
    if data['skill_desc']:
        skill_desc = data['skill_desc']
    if data['skill_status']:
        skill_status = int(data['skill_status'])
    if (skill_name == "") or (skill_desc == "") or (skill_status == ""):
        return jsonify(
            {
                "code": 500,
                "message": "Skill name or Skill desc is empty"
            }
        ) 
    skill = Skill(skill_name=skill_name, skill_desc=skill_desc, skill_status=skill_status)
    if test_data == "":
        try:
            db.session.add(skill)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred updating the skill."
                }
            ), 500

        return jsonify(
            {
                "code": 200,
                "data": skill.json()
            }
        )
    else:
        return jsonify(
            {
                "code": 200,
                "data": skill.json()
            }
        )

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)
