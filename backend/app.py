import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from os import environ

# Flask App and DB connection is done here.
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


 #Role_Map Table
class role_map(db.Model):
    __tablename__ = 'role_map'
    job_role_id = db.Column(db.Integer, primary_key=True,nullable=False)
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    def __init__(self, job_role_id, skill_id):
        if not isinstance(job_role_id, int):
            raise TypeError("job_role_id must be a integer")
        if not isinstance(skill_id, int):
            raise TypeError("skill_id must be a integer")
        self.job_role_id = job_role_id
        self.skill_id = skill_id

    def json(self):
        return  {
             "job_role_id": self.job_role_id,
            "skill_id": self.skill_id           
        }

#Skill Table
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
            raise TypeError("skill_status must be a integer")
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


@app.route("/")
def home():
    pass
#This segment of code is to get a specific job role. Used by both HR and Learner.
@app.route("/getSpecificJobRole/<int:job_role_id>")
def getAllJobRole(job_role_id,test_data= ""):
    jobRoles = None
    if test_data == "":
        jobRoles = JobRole.query.filter_by(job_role_id=job_role_id).all()
    if test_data != "": 
        return (         
                {
                    "code": 200,
                      "data": [jr.json() for jr in jobRoles]
                }
            )
    elif jobRoles != None:
       return jsonify(
           {
               "code": 200,
               "data": [jr.json() for jr in jobRoles]
           }
       )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no job roles found."
            }
        )


#This segment of code is update details of a selected role
#=============== Update Job Role details by job_role_id======================================
@app.route("/updateRole/<int:job_role_id>", methods=['PUT'])
def change_apt(job_role_id):
    jobrole = JobRole.query.filter_by(job_role_id=job_role_id).first()
    if jobrole:
        # take json input and parse it here
        print(jobrole)
        data = request.get_json()
        if data['job_role_name']:
            jobrole.job_role_name = data['job_role_name']
        if data['job_role_desc']:
            jobrole.job_role_desc = data['job_role_desc']
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "job_role_id": job_role_id
                    },
                    "message": "An error occurred updating the job."
                }
            ), 500

        return jsonify(
            {
                "code": 200,
                "data": jobrole.json()
            }
        )
    # return these if job role not found
    return jsonify(
        {
            "code": 404,
            "data": {
                "job_role_id": job_role_id
            },
            "message": "job_role_id not found."
        }
    ), 404


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

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)