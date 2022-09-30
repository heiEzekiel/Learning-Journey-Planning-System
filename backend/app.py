import os
from tkinter import S
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from os import environ

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/LJPS_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

CORS(app)

db = SQLAlchemy(app)
#Job Role (For LJPS)
class JobRole(db.Model):
    __tablename__ = 'job_role'
    job_role_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_role_name = db.Column(db.String(50), nullable=False)
    job_role_desc = db.Column(db.String(255), nullable=False)
    job_role_status = db.Column(db.Integer, nullable=False)
    def __init__(self, job_role_name,  job_role_desc, job_role_status):
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

#This segment of code is to do retrieval of all the existing roles. Used by both HR and Learner.
@app.route("/getAllJobRole")
def getAllJobRole():
    jobRoles = JobRole.query.all()
    return jsonify(
            {
                "code": 200,
                "data": 
                   [roles.json() for roles in jobRoles]
            }
        )

#Skill Table
class Skill(db.Model):
    __tablename__ = 'Skill'
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    skill_desc = db.Column(db.String(255), nullable=False)
    skill_status = db.Column(db.Integer, nullable=False)
    def __init__(self, skill_name, skill_desc, skill_status):
        self.skill_name = skill_name
        self.skill_status = skill_status
        self.skill_desc = skill_desc
    skill_status = db.Column(db.Integer, nullable=False)

    def json(self):
        return  {
            "skill_id": self.skill_id, 
            "skill_name": self.skill_name, 
            "skill_desc": self.skill_desc,
            "skill_status": self.skill_status
        }
#Role_Map Table
class role_map(db.Model):
    __tablename__ = 'role_map'
    job_role_id = db.Column(db.Integer, primary_key=True,nullable=False)
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    def __init__(self, job_role_id, skill_id):
        self.job_role_id = job_role_id
        self.skill_id = skill_id

    def json(self):
        return  {
             "job_role_id": self.job_role_id,
            "skill_id": self.skill_id           
        }
        
@app.route("/")
def home():
    pass

#skill = Skill.query.all()
# Get skills required for the selected job role
@app.route("/getSkillsForJob/<int:job_role_id>")
def getSkillsForJob(job_role_id):
    # Get a list of skill_id required for the job
    rolemapping = role_map.query.filter_by(job_role_id=job_role_id).all()
    if rolemapping:
        role = [r.json() for r in rolemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['skill_id'])
        skillName =[]
        # For each skill_id, find the name of skill
        skill = Skill.query.all()
        if skill:
            skill_list = [s.json() for s in skill]
            for i in skill_list:
                if i['skill_id'] in list_of_skill:
                    skillName.append([i['skill_name'], i['skill_desc']])
            return jsonify(
    {
            "code": 200,
            "data": skillName
        }, 200

            )   
                

    return jsonify(
       {
           "code": 404,
           "message": "No records found."
       }
   ), 404





@app.route("/getskills")
def getskills():
    skills = Skill.query.all()
    print(skills)
    return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": [skill.json() for skill in skills]
                }
            }
        )

if __name__ == "__main__":
    app.run(debug=True)
