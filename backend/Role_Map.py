from flask import  request, jsonify
import db_connector
db = db_connector.db_connector()
from Skills import Skill

# Role_Map Table
class Role_Map(db.Model):
    __tablename__ = 'Role_Map'
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
def create_role_map(rm_fk_job_role_id, rm_fk_skill_id, test_data=""):
    if test_data == "":
        data = request.get_json()
        new_map = Role_Map(data['rm_fk_job_role_id'], data['rm_fk_skill_id'])
    else:
        new_map = test_data

    if test_data == "":
        try:
            db.session.add(new_map)
            db.session.commit()
            db.session.remove()
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


# ********************************* Retrieve ********************************* 
# Get all skills for a job role
def get_skills_for_job(job_role_id, test_data_role_map="", test_data_skill="", test_data_job_role=""):
    # Get a list of skill_id required for the job
    rolemapping = None
    if test_data_role_map == "" and test_data_skill == "" and test_data_job_role == "":
        rolemapping = Role_Map.query.filter_by(
            rm_fk_job_role_id=job_role_id).all()
        db.session.remove()
    else:
        rolemapping = [role for role in test_data_role_map if int(
            role.rm_fk_job_role_id) == job_role_id]
    if rolemapping:
        role = [r.json() for r in rolemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['rm_fk_skill_id'])
        skillName = []
        # For each skill_id, find the name of skill
        skill = None
        if test_data_skill == "":
            skill = Skill.query.all()
            db.session.remove()
        else:
            skill = test_data_skill
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
def delete_skill_from_job_role(job_role_id, skill_id, test_data="", existing_data=""):
    all_role = None
    role = None
    if test_data == "":
        role = Role_Map.query.filter_by(
            rm_fk_job_role_id=job_role_id, rm_fk_skill_id=skill_id).first()
    else:
        role = test_data
        all_role = existing_data
    if role and test_data == "":
        db.session.delete(role)
        db.session.commit()
        db.session.remove()
        return jsonify(
            {
                "code": 200,
                "message": "Skill removed successfully"
            }
        )
    elif role and test_data != "":
        for role in all_role:
            if role.rm_fk_job_role_id == job_role_id and role.rm_fk_skill_id == skill_id:
                all_role.remove(role)
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




