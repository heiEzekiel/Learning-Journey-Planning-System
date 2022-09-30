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

#This segment of code is to do creation of roles. Only used by HR/admin.
#Takes in job_role_name and job_role_desc
# job_role_status 0 means active
@app.route("/createJobRole", methods=['POST'])
def create_job_role():
    data = request.get_json()
    print(data)
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
#=========================================================================


#Run flask app
if __name__ == "__main__":
    app.run(debug=True)