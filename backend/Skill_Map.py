from flask import  request, jsonify
from db_connector import db

# Andy to test this new DB
# Skill Map Table
class Skill_Map(db.Model):
    __tablename__ = 'Skill_Map'
    sm_fk_skill_id = db.Column(
        db.Integer, primary_key=True, nullable=False)
    sm_fk_staff_id = db.Column(db.Integer, primary_key=True, nullable=False)
    def __init__(self, sm_fk_skill_id, sm_fk_staff_id):
        if not isinstance(sm_fk_skill_id, int):
            raise TypeError("sm_fk_skill_id must be a integer")
        if not isinstance(sm_fk_staff_id, int):
            raise TypeError("sm_fk_staff_id must be a integer")
        self.sm_fk_skill_id = sm_fk_skill_id
        self.sm_fk_staff_id = sm_fk_staff_id

    def json(self):
        return {
            "sm_fk_skill_id": self.sm_fk_skill_id,
            "sm_fk_staff_id": self.sm_fk_staff_id
        }

#Functions (CRUD)
# ********************************* Create ********************************* 


# ********************************* Retrieve ********************************* 
# Get Staff Skills
def get_staff_skills(sm_fk_staff_id):
    skill = Skill_Map.query.filter_by(sm_fk_staff_id=sm_fk_staff_id).all()
    db.session.remove()
    if skill:
        return jsonify(
            {
                "code": 200,
                "data": [s.json() for s in skill]
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no records found."
            }
        )        


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 

