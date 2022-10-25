from flask import  request, jsonify
from db_connector import db
from Skills import Skill

# Role_Map Table
class Role_Map(db.Model):
    __tablename__ = 'Role_Map'
    __table_args__ = {'extend_existing': True}
    rm_fk_job_role_id = db.Column(db.Integer, primary_key=True, nullable=False)
    rm_fk_skill_id = db.Column(db.Integer, primary_key=True, nullable=False)

    def __init__(self, rm_fk_job_role_id, rm_fk_skill_id):
        if not isinstance(rm_fk_job_role_id, int):
            raise TypeError("rm_fk_job_role_id must be a integer")
        if not isinstance(rm_fk_skill_id, int):
            raise TypeError("rm_fk_skill_id must be a integer")
        self.rm_fk_job_role_id = rm_fk_job_role_id
        self.rm_fk_skill_id = rm_fk_skill_id

    def json(self):
        return {
            "rm_fk_job_role_id": self.rm_fk_job_role_id,
            "rm_fk_skill_id": self.rm_fk_skill_id
        }


#Functions (CRUD)
# ********************************* Create ********************************* 
# Create role mapping
def create_role_map(rm_fk_job_role_id, rm_fk_skill_id):
    data = request.get_json()
    new_map = Role_Map(data['rm_fk_job_role_id'], data['rm_fk_skill_id'])
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


# ********************************* Retrieve ********************************* 
# Get all skills for a job role
def get_skills_for_job(job_role_id):
    # Get a list of skill_id required for the job
    rolemapping = Role_Map.query.filter_by(
        rm_fk_job_role_id=job_role_id).all()
    if rolemapping:
        role = [r.json() for r in rolemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['rm_fk_skill_id'])
        skillName = []
        # For each skill_id, find the name of skill
        skill = Skill.query.all()
        if skill:
            skill_list = [s.json() for s in skill]

            for i in skill_list:
                if i['skill_id'] in list_of_skill:
                    skillName.append(
                        [i['skill_name'], i['skill_desc'], i['skill_id'], i['skill_status']])
            return jsonify(
                {
                    "code": 200,
                    "data": skillName
                }, 200

            )
        else:
            return jsonify(
                {
                    "code": 404,
                    "data": "No records found"
                }, 404)

    return jsonify(
        {
            "code": 404,
            "message": "No records found."
        }
    ), 404


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 
# Delete role mapping
def delete_skill_from_job_role(job_role_id, skill_id):
    role = Role_Map.query.filter_by(
        rm_fk_job_role_id=job_role_id, rm_fk_skill_id=skill_id).first()
    if role:
        db.session.delete(role)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": "Skill removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,

            "message": "Skill and Role not found."
        }
    ), 404




