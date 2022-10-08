from cgi import test
import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from os import environ
import json
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
class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
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
class Role_Map(db.Model):
    __tablename__ = 'Role_Map'
    rm_fk_job_role_id = db.Column(db.Integer, primary_key=True,nullable=False)
    rm_fk_skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    def __init__(self, rm_fk_job_role_id, rm_fk_skill_id):
        if not isinstance(rm_fk_job_role_id, int):
            raise TypeError("rm_fk_job_role_id must be a integer")
        if not isinstance(rm_fk_skill_id, int):
            raise TypeError("rm_fk_skill_id must be a integer")
        self.rm_fk_job_role_id = rm_fk_job_role_id
        self.rm_fk_skill_id = rm_fk_skill_id

    def json(self):
        return  {
             "rm_fk_job_role_id": self.rm_fk_job_role_id,
            "rm_fk_skill_id": self.rm_fk_skill_id           
        }

#Course Map Table
class Course_Map(db.Model):
    __tablename__ = 'Course_Map'
    cm_fk_course_id = db.Column(db.String(20), primary_key=True,nullable=False)
    cm_fk_skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    def __init__(self, cm_fk_course_id, cm_fk_skill_id):
        if not isinstance(cm_fk_course_id, str):
            raise TypeError("cm_fk_course_id must be a String")
        if not isinstance(cm_fk_skill_id, int):
            raise TypeError("cm_fk_skill_id must be a integer")
        self.cm_fk_course_id = cm_fk_course_id
        self.cm_fk_skill_id = cm_fk_skill_id

    def json(self):
        return  {
            "cm_fk_course_id": self.cm_fk_course_id,
            "cm_fk_skill_id": self.cm_fk_skill_id           
        }

#Course  Table
class Course(db.Model):
    __tablename__ = 'Course'
    course_id = db.Column(db.String(20), primary_key=True, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    course_desc = db.Column(db.String(255), nullable=False)
    course_status = db.Column(db.String(15), nullable=False)
    course_type = db.Column(db.String(10), nullable=False)
    course_category = db.Column(db.String(50), nullable=False)
    def __init__(self, course_id,course_name, course_desc,course_status,course_type,course_category):
        if not isinstance(course_id, str):
            raise TypeError("course_id must be a String")
        if not isinstance(course_name, str):
            raise TypeError("course_name must be a String")
        if not isinstance(course_desc, str):
            raise TypeError("course_desc must be a String")
        if not isinstance(course_status, str):
            raise TypeError("course_status must be a String")
        if not isinstance(course_type, str):
            raise TypeError("course_type must be a String")
        if not isinstance(course_category, str):
            raise TypeError("course_category must be a String")
        self.course_id = course_id
        self.course_name = course_name
        self.course_desc = course_desc
        self.course_status = course_status
        self.course_type = course_type
        self.course_category = course_category

    def json(self):
        return  {
            "course_id": self.course_id,
            "course_name": self.course_name   ,
            "course_desc": self.course_desc,
            "course_status": self.course_status ,
            "course_type": self.course_type,
            "course_category": self.course_category         
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
        
#Journey Table
class Journey(db.Model):
    __tablename__ = 'Journey'
    journey_id = db.Column(db.Integer, primary_key=True,nullable=False)
    journey_status = db.Column(db.String(100), nullable=False)
    j_fk_staff_id = db.Column(db.Integer, nullable=False)
    j_fk_job_role_id = db.Column(db.Integer, nullable=False)
    def __init__(self, journey_status, j_fk_staff_id, j_fk_job_role_id):
        if not isinstance(journey_status, str):
            raise TypeError("journey_status must be a string")
        if not isinstance(j_fk_staff_id, int):
            raise TypeError("j_fk_staff_id must be an integer")
        if not isinstance(j_fk_job_role_id, int):
            raise TypeError("j_fk_job_role_id must be an integer")
        self.journey_status = journey_status
        self.j_fk_staff_id = j_fk_staff_id
        self.j_fk_job_role_id = j_fk_job_role_id

    def json(self):
        return  {
            "journey_id": self.journey_id, 
            "journey_status": self.journey_status, 
            "j_fk_staff_id": self.j_fk_staff_id,
            "j_fk_job_role_id": self.j_fk_job_role_id         
        }
        
#Journey Map Table
class Journey_Map(db.Model):
    __tablename__ = 'Journey_Map'
    jm_fk_journey_id = db.Column(db.Integer, primary_key=True,nullable=False)
    jm_fk_course_id = db.Column(db.String(20), primary_key=True, nullable=False)
    def __init__(self, jm_fk_journey_id, jm_fk_course_id):
        if not isinstance(jm_fk_journey_id, int):
            raise TypeError("jm_fk_journey_id must be an Integer")
        if not isinstance(jm_fk_course_id, str):
            raise TypeError("jm_fk_course_id must be a String")
        self.jm_fk_journey_id = jm_fk_journey_id
        self.jm_fk_course_id = jm_fk_course_id

    def json(self):
        return  {
            "jm_fk_journey_id": self.jm_fk_journey_id,
            "jm_fk_course_id": self.jm_fk_course_id           
        }
        
@app.route("/")
def home():
    pass

#=======================================================================================Job Role Related=======================================================================#
#This segment of code is to do creation of roles. Only used by HR/admin.
#Create Job Role
@app.route("/createJobRole", methods=['POST'])
def create_job_role(test_data = ''):
    data = None
    if test_data == '':
        data = request.get_json()
        new_job_role = Job_Role(data['job_role_name'], data['job_role_desc'],1)
        #check is existing role is there
        if test_data == "":
            jobRoles = Job_Role.query.all()
        else:
            jobRoles = test_data
        if jobRoles != None:
            res =  (
           {
               "code": 200,
               "data":  [roles.json() for roles in jobRoles]
           }
       )
            roles = res['data']
            for i in range(len(roles)):
                if (roles[i]['job_role_name'].replace(" ","").lower())==data['job_role_name'].replace(" ","").lower():
                    return jsonify(
                {
                    "code": 400,
                    "data": {
                        "job_role_name": data['job_role_name']
                    },
                    "message": "Job role already exist!"
                }
            ), 500

        # if don't exist then execute these codes
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
        new_job_role = Job_Role(test_data['job_role_name'], test_data['job_role_desc'],test_data['job_role_status'])
        return jsonify(
                {
                    "code": 201,
                    "data": new_job_role.json(),
                    "message": "Job Role successfully created"
                }
            )

#This segment of code is to get a specific job role. Used by both HR and Learner.
#=============== Get Job Role details by job_role_id======================================
@app.route("/getSpecificJobRole/<int:job_role_id>")
def getSpecificJobRole(job_role_id,test_data= ""):
    jobRoles = None
    if test_data == "":
        jobRoles = Job_Role.query.filter_by(job_role_id=job_role_id).all()
    else:
        jobRoles = test_data
    if test_data == "": 
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


#This segment of code is to do retrieval of all the existing roles. Used by both HR and Learner.
@app.route("/getAllJobRole")
def getAllJobRole(test_data= ""):
    jobRoles = None
    if test_data == "":
        jobRoles = Job_Role.query.all()
        return jsonify (
            {
                "code": 200,
                "data": 
                [r.json() for r in jobRoles]
            }
        )
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


#This segment of code is update details of a selected role
#=============== Update Job Role details by job_role_id======================================
@app.route("/updateRole/<int:job_role_id>", methods=['PUT'])
def updateRole(job_role_id, test_data="", new_data="",test_data_2=""):
    jobrole = None
    if test_data == "":
        jobrole = Job_Role.query.filter_by(job_role_id=job_role_id).first()
    else:
        jobrole = test_data
    if jobrole:
        # take json input and parse it here
        data = None
        if new_data == "":
            data = request.get_json()
        else:
            data = new_data

        pre_change = jobrole.job_role_name

        #check if Job Role  Already Exist
        #Note that this codes allows updating role name to the same role name we are updating
        if test_data == "":
            jobRoles = Job_Role.query.all()
        else:
            jobRoles = test_data_2
        if jobRoles != None:
            res =  (
           {
               "code": 200,
               "data":  [roles.json() for roles in jobRoles]
           }
       )
            roles = res['data']
            for i in range(len(roles)):
                if (roles[i]['job_role_name'].replace(" ","").lower())==pre_change.replace(" ","").lower():
                    continue
                if (roles[i]['job_role_name'].replace(" ","").lower())==data['job_role_name'].replace(" ","").lower():
                    return jsonify(
                {
                    "code": 400,
                    "data": {
                        "job_role_name": data['job_role_name']
                    },
                    "message": "Job role already exist!"
                }
            ), 500

        
        if data['job_role_name']:
            jobrole.job_role_name = data['job_role_name']
        if data['job_role_desc']:
            jobrole.job_role_desc = data['job_role_desc']



         #If don't exist run these
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

#This segment of code is delete a selected role
#=============== Delete Role details by job_role_id======================================
@app.route("/deleteRole/<int:job_role_id>", methods=['DELETE'])
def deleteRole(job_role_id, test_data="", existing_data=""):
    all_job = None
    job = None
    if test_data == "":
        job = Job_Role.query.filter_by(job_role_id=job_role_id).first()
    else:
        job = test_data
        all_job = existing_data 
    if job and test_data == "":
        db.session.delete(job)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message" : "Job removed successfully"
            }
        )
    elif job and test_data != "":
        for job in all_job:
            if job.job_role_id == job_role_id:
                all_job.remove(job)
                return jsonify(
                    {
                        "code": 200,
                        "message" : "Job removed successfully"
                    }
                )
    return jsonify(
        {
            "code": 404,
            "message": "Job not found."
        }
    )


#=======================================================================================Role-Skill Related=======================================================================#
#==============================Create job to role mapping===================================
#Used when updating role information, or mapping role information. Used in assign skill to role and update.
@app.route("/createRoleMap/<int:rm_fk_job_role_id>/<int:rm_fk_skill_id>", methods=['POST'])
def createRoleMap(test_data=""):
    if test_data == "":
        data = request.get_json()
        new_map = Role_Map(data['rm_fk_job_role_id'], data['rm_fk_skill_id'])
    else:
        new_map = test_data
    
    if test_data == "":
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
    else:
        return jsonify(
            {
                "code": 201,
                "data": new_map.json(),
                "message": "Success"
            }
        )
        

#==============================Retrieve Skill for job role with job_role_id===================================
# Get skills required for the selected job role using job_role_id
@app.route("/getSkillsForJob/<int:job_role_id>")
def getSkillsForJob(job_role_id, test_data_role_map="", test_data_skill="", test_data_job_role=""):
    # Get a list of skill_id required for the job
    rolemapping = None
    if test_data_role_map == "" and test_data_skill == "" and test_data_job_role == "":
        rolemapping = Role_Map.query.filter_by(rm_fk_job_role_id=job_role_id).all()
        
    else:
        rolemapping = [role for role in test_data_role_map if int(role.rm_fk_job_role_id) == job_role_id]
    if rolemapping:
        role = [r.json() for r in rolemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['rm_fk_skill_id'])
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
    else:
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
                    skillName.append([i['skill_name'], i['skill_desc']])
            return jsonify(
                {
            "code": 209,
            "data": skillName
            }, 200)        


    return jsonify(
       {
           "code": 404,
           "message": "No records found."
       }
   ), 404

#==============================Remove Skill from Job Role===================================
# Remove a skill from a job role 
@app.route("/removeSkillFromJobRole/<int:job_role_id>/<int:skill_id>", methods=['DELETE'])
def del_role(job_role_id,skill_id, test_data="", existing_data=""):
    all_role = None
    role = None
    if test_data=="":   
        role = Role_Map.query.filter_by(rm_fk_job_role_id=job_role_id, rm_fk_skill_id=skill_id).first()
    else:
        role = test_data
        all_role = existing_data
    if role and test_data=="":
        db.session.delete(role)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message" : "Skill removed successfully"
            }
        )
    elif role and test_data!="":
        for role in all_role:
            if role.rm_fk_job_role_id == job_role_id and role.rm_fk_skill_id == skill_id:
                all_role.remove(role)
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

    


 #=======================================================================================Skill-Course Related=======================================================================#  
# Get courses available for the selected skill using skill_id
@app.route("/getCoursesForSkill/<int:skill_id>")
def getCoursesForSkill(skill_id, test_data_course_map="", test_data_course="", test_data_skill=""):
    # Get a list of courses related to this job
    coursemapping = None
    if test_data_course_map == "" and test_data_course == "" and test_data_skill == "":
        coursemapping = Course_Map.query.filter_by(cm_fk_skill_id=skill_id).all()
    else:
        coursemapping = test_data_course_map
    if coursemapping:
        c = [c.json() for c in coursemapping]
        list_of_course = []
        for i in (c):
            list_of_course.append(i['cm_fk_course_id'])
        skillName =[]

        # For each course_id, find the name of course
        course = None
        if test_data_course == "":
            course = Course.query.all()
        else:
            course = test_data_course
        if course:
            course_list = [course.json() for course in course]
            for i in course_list:
                if i['course_id'] in list_of_course:
                    # skillName.append([i['skill_name'], i['skill_desc']])
                    skillName.append(i)
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

#=======================================================================================Skill Related=======================================================================#
# Get skill ID using skill name
@app.route("/getSkillID/<string:skill_name>/", methods=['GET'])
def getSkillID(skill_name, test_data=""):
    role = None
    if test_data == "":
        role = Skill.query.filter_by(skill_name=skill_name)
    else:
        role = test_data
    if role and test_data == "":
        return jsonify(
            {
                "code": 200,
                "message" :  [r.json() for r in role]
            }
        )
    elif role and test_data != "":
        for r in role:
            if r.skill_name == skill_name:
                return jsonify(
                    {
                        "code": 200,
                        "message" : r.json()
                    }
                )
    return jsonify(
        {
            "code": 404,

            "message": "Not Found"
        }
    ), 404
   
# =================================Get skill ID using skill id=================
@app.route("/getSkillById/<int:skill_id>/", methods=['GET'])
def getSkillById(skill_id, test_data=""):
    skill = None
    if test_data == "":
        skill = Skill.query.filter_by(skill_id=skill_id)
    else:
        skill = test_data
    if skill and test_data == "":
        return jsonify(
            {
                "code": 200,
                "message" :  [s.json() for s in skill]
            }
        )
    elif skill and test_data != "":
        for s in skill:
            if s.skill_id == skill_id:
                return jsonify(
                    {
                        "code": 200,
                        "message" : s.json()
                    }
                )
    return jsonify(
        {
            "code": 404,

            "message": "Not Found"
        }
    )

# =================================Get a list of skills=================

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

#This segment of code is to create skill
#=========================================== Create skill======================================
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
    #ignored until future feature comes in
    # if data['skill_status']:
    #     skill_status = int(data['skill_status'])
    if (skill_name == "") or (skill_desc == ""):
        return jsonify(
            {
                "code": 500,
                "message": "Skill name or Skill desc is empty"
            }
        ) 
    skill = Skill(skill_name=skill_name, skill_desc=skill_desc, skill_status=0)
    if test_data == "":
                #check is existing role is there
        skills = Skill.query.all()
        if skills != None:
            res =  (
           {
               "code": 200,
               "data":  [s.json() for s in skills]
           }
       )
            s = res['data']
            for i in range(len(s)):
                if (s[i]['skill_name'].replace(" ","").lower())==data['skill_name'].replace(" ","").lower():
                    return jsonify(
                {
                    "code": 400,
                    "data": {
                        "skill_name": data['skill_name']
                    },
                    "message": "Skill name already exist!"
                }
            ), 500
            # if no duplicate skill then run these codes
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
def updateSkill(skill_id, test_data="", new_data="",test_data2=""):
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

        preskill = skill.skill_name
        

     #check is existing role is there
        if test_data == "":
            skills = Skill.query.all()
        else:
            skills = test_data2
        if skills != None:
            res =  (
           {
               "code": 200,
               "data":  [s.json() for s in skills]
           }
       )
            s = res['data']
            for i in range(len(s)):
                if (preskill.replace(" ","").lower()==s[i]['skill_name'].replace(" ","").lower()):
                    continue
                if (s[i]['skill_name'].replace(" ","").lower())==data['skill_name'].replace(" ","").lower():
                    return jsonify(
                {
                    "code": 400,
                    "data": {
                        "skill_name": data['skill_name']
                    },
                    "message": "Skill name already exist!"
                }
            ), 500
            
        if data['skill_name']:
            skill.skill_name = data['skill_name']
        if data['skill_desc']:
            skill.skill_desc = data['skill_desc']

        # if no duplicate skill then run these codes
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

#This segment of code is delete a selected skill
#=============== Delete Skill details by skill_id======================================
@app.route("/deleteSkill/<int:skill_id>", methods=['DELETE'])
def deleteSkill(skill_id, test_data=""):
    skill = None
    if test_data == "":
        skill = Skill.query.filter_by(skill_id=skill_id).first()
    else:
        skill = test_data
    if skill and test_data == "":
        db.session.delete(skill)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message" : "Skill removed successfully"
            }
        )
    elif skill and test_data != "":
        for i in skill:
            if i.skill_id == skill_id:
                skill.remove(i)
                break
        return jsonify(
            {
                "code": 200,
                "message" : "Skill removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skill not found."
        }
    ), 404


#This segment of code is for learning journey
#=========================================== journey======================================
@app.route("/createJourney", methods=['POST'])
def createJourney(test_data=""):
    data = None
    if test_data == "":
        data = request.get_json()
    else:
        data = test_data
    journey_status, j_fk_staff_id, j_fk_job_role_id = "", "", ""
    if data['journey_status']:
        journey_status = data['journey_status']
    if data['j_fk_staff_id']:
        j_fk_staff_id = data['j_fk_staff_id']
    if data['j_fk_job_role_id']:
        j_fk_job_role_id = data['j_fk_job_role_id']
    pass


@app.route("/createJourneyMap/<int:jm_fk_journey_id>/<int:jm_fk_course_id>", methods=['POST'])
def createJourneyMap(test_data=""):
    data = None
    new_map = None
    if test_data=="":
        data = request.get_json()
        new_map = Journey_Map(data['jm_fk_journey_id'], data['jm_fk_course_id'])
    else:
        new_map = test_data
    if test_data =="" and data and new_map:
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
    else:
        return jsonify(
            {
                "code": 201,
                "data": new_map.json(),
                "message": "Success"
            }
        )

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)
