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
@app.route("/")
def home():
    pass

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

#Run flask app
if __name__ == "__main__":
    app.run(debug=True)