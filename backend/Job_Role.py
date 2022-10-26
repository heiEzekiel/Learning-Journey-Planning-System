from flask import  request, jsonify
from db_connector import db

class Job_Role(db.Model):
    __tablename__ = 'Job_Role'
    __table_args__ = {'extend_existing': True}
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
        self.job_role_desc = job_role_desc
        self.job_role_status = job_role_status

    def json(self):
        return {
            "job_role_id": self.job_role_id,
            "job_role_name": self.job_role_name,
            "job_role_desc": self.job_role_desc,
            "job_role_status": self.job_role_status
        }
        
#Functions (CRUD)
# ********************************* Create ********************************* 
# Create Job Role
def create_job_role():
    data = request.get_json()
    new_job_role = Job_Role(
        data['job_role_name'], data['job_role_desc'], 0)
    # check is existing role is there
    jobRoles = Job_Role.query.all()
    if jobRoles:
        res = (
            {
                "code": 200,
                "data":  [roles.json() for roles in jobRoles]
            }
        )
        roles = res['data']
        for i in range(len(roles)):
            if (roles[i]['job_role_name'].replace(" ", "").lower()) == data['job_role_name'].replace(" ", "").lower():
                return jsonify(
                    {
                        "code": 400,
                        "data": {
                            "job_role_name": data['job_role_name']
                        },
                        "message": "Job role already exist!"
                    }
                ), 400

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


# ********************************* Retrieve ********************************* 
# Get all job roles
def get_all_job_role():
    jobRoles = Job_Role.query.all()
    if jobRoles:
        return jsonify(
            {
                "code": 200,
                "data":
                [r.json() for r in jobRoles]
            }
        )
    else:
                    return jsonify(
            {
                "code": 404,
                "data": 'No records found'
                
            }
        )

# Get job role by id
def get_specific_job_role_by_id(job_role_id):
    jobRoles = Job_Role.query.filter_by(job_role_id=job_role_id).all()
    if jobRoles:
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

# ********************************* Update ********************************* 
# Update job role
def update_job_role_by_id(job_role_id):
    data = request.get_json()
    job_role = Job_Role.query.filter_by(job_role_id=job_role_id).first()
    if job_role:
        job_role.job_role_name = data['job_role_name']
        job_role.job_role_desc = data['job_role_desc']
        job_role.job_role_status = data['job_role_status']
        try:
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "job_role_id": job_role_id
                    },
                    "message": "An error occurred updating the job role."
                }
            ), 500

        return jsonify(
            {
                "code": 200,
                "data": job_role.json(),
                "message": "Job Role successfully updated"
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "job_role_id": job_role_id
                },
                "message": "Job Role not found."
            }
        ), 404


# ********************************* Delete ********************************* 
# Delete job role
def delete_job_role_by_id(job_role_id):
    job = Job_Role.query.filter_by(job_role_id=job_role_id).first()
    if job:
        db.session.delete(job)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": "Job removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Job not found."
        }
    )
