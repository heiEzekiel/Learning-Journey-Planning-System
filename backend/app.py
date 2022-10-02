from cgi import test
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

#Job Role (For LJPS)
class JobRole(db.Model):
    __tablename__ = 'job_role'
    job_role_id = db.Column(db.Integer, primary_key=True, nullable=False)
    job_role_name = db.Column(db.String(50), nullable=False)
    job_role_desc = db.Column(db.String(255), nullable=False)
    job_role_status = db.Column(db.Integer, nullable=False)
    def __init__(self, job_role_name,  job_role_desc, job_role_status):
        if not isinstance(job_role_name, str):
            raise TypeError('job_role_name must be a string')
        if not isinstance(job_role_desc, str):
            raise TypeError('job_role_desc must be a string')
        if not isinstance(job_role_status, int):
            raise TypeError('job_role_status must be an integer')
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

#This segment of code is to get a specific job role. Used by both HR and Learner.
@app.route("/getSpecificJobRole/<int:job_role_id>")
def getSpecificJobRole(job_role_id,test_data= ""):
    jobRoles = None
    if test_data == "":
        jobRoles = JobRole.query.filter_by(job_role_id=job_role_id).all()
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
def updateRole(job_role_id, test_data="", new_data=""):
    jobrole = None
    if test_data == "":
        jobrole = JobRole.query.filter_by(job_role_id=job_role_id).first()
    else:
        jobrole = test_data
    if jobrole:
        # take json input and parse it here
        data = None
        if new_data == "":
            data = request.get_json()
        else:
            data = new_data
        if data['job_role_name']:
            jobrole.job_role_name = data['job_role_name']
        if data['job_role_desc']:
            jobrole.job_role_desc = data['job_role_desc']
        
        if test_data == "" and new_data == "":
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
        else:
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
def getSkillsForJob(job_role_id, test_data_role_map="", test_data_skill="", test_data_job_role=""):
    # Get a list of skill_id required for the job
    rolemapping = None
    if test_data_role_map == "" and test_data_skill == "" and test_data_job_role == "":
        rolemapping = role_map.query.filter_by(job_role_id=job_role_id).all()
    else:
        rolemapping = [role for role in test_data_role_map if int(role.job_role_id) == job_role_id]
    if rolemapping:
        role = [r.json() for r in rolemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['skill_id'])
        skillName =[]
        # For each skill_id, find the name of skill
        skill = None
        if test_data_skill == "":
            skill = Skill.query.all()
        else:
            skill = test_data_skill
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




@app.route("/removeRole/<int:job_role_id>/<int:skill_id>", methods=['DELETE'])
def del_role(job_role_id,skill_id):
   role = role_map.query.filter_by(job_role_id=job_role_id, skill_id=skill_id).first()
   if role:
       db.session.delete(role)
       db.session.commit()
       return jsonify(
           {
               "code": 200,
               "message" : "Skill removed successfully"
           }
       )
   return jsonify(
       {
           "code": 404,

           "message": "Skill and Role not found."
       }
   ), 404

# Get skill ID using skill name
@app.route("/getSkillID/<string:skill_name>/", methods=['GET'])
def getSkillID(skill_name):
   role = Skill.query.filter_by(skill_name=skill_name)
   if role:
       return jsonify(
           {
               "code": 200,
               "message" :  [r.json() for r in role]
           }
       )
   return jsonify(
       {
           "code": 404,

           "message": "Not Found"
       }
   ), 404
   
# Get skill ID using skill id
@app.route("/getSkillById/<int:skill_id>/", methods=['GET'])
def getSkillById(skill_id):
   skill = Skill.query.filter_by(skill_id=skill_id)
   if skill:
       return jsonify(
           {
               "code": 200,
               "message" :  [s.json() for s in skill]
           }
       )
   return jsonify(
       {
           "code": 404,

           "message": "Not Found"
       }
   ), 404


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


@app.route("/createRoleMap/<int:job_role_id>/<int:skill_id>", methods=['POST'])
def createRoleMap(job_role_id,skill_id):
    data = request.get_json()
    new_map = role_map(data['job_role_id'], data['skill_id'])
    try:
        db.session.add(new_map)
        db.session.commit()
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the record."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": new_map.json(),
            "message": "Success"
        }
    ), 201

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

#This segment of code is to create skill
#=============== Create skill======================================
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

#This segment of code is update details of a selected skill
#=============== Update Skill details by skill_id======================================
@app.route("/updateSkill/<int:skill_id>", methods=['PUT'])
def updateSkill(skill_id, test_data="", new_data=""):
    skill = None
    if test_data == "":
        skill = Skill.query.filter_by(skill_id=skill_id).first()
    else:
        skill = test_data
    if skill:
        data = None
        if new_data == "":
            data = request.get_json()
        else:
            data = new_data
        
        if data['skill_name']:
            skill.skill_name = data['skill_name']
        if data['skill_desc']:
            skill.skill_desc = data['skill_desc']

        if test_data =="" and new_data=="":
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                return jsonify(
                    {
                        "code": 500,
                        "data": {
                            "skill_id": skill_id
                        },
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
    # return these if job role not found
    return jsonify(
        {
            "code": 404,
            "data": {
                "skill_id": skill_id
            },
            "message": "skill_id not found."
        }
    ), 404


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

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)
