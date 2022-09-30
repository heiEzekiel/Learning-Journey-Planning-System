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

#skill = Skill.query.all()

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
@app.route("/")
def home():
    pass

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
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no job roles."
            }
        )


#Run flask app
if __name__ == "__main__":
    app.run(debug=True)