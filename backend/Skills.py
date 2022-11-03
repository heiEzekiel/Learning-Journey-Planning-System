from flask import  request, jsonify
from db_connector import db

# Skill Table
class Skill(db.Model):
    __tablename__ = 'Skill'
    __table_args__ = {'extend_existing': True}
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
        return {
            "skill_id": self.skill_id,
            "skill_name": self.skill_name,
            "skill_desc": self.skill_desc,
            "skill_status": self.skill_status
        }

#Functions (CRUD)
# ********************************* Create ********************************* 
# Create a new skill
def create_skills():
    data = request.get_json()
    skill_name, skill_desc, skill_status = "", "", ""
    if data['skill_name']:
        skill_name = data['skill_name']
    if data['skill_desc']:
        skill_desc = data['skill_desc']
    # ignored until future feature comes in
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
    # check is existing role is there
    skills = Skill.query.all()
    if skills:
        res = (
            {
                "code": 200,
                "data":  [s.json() for s in skills]
            }
        )
        s = res['data']
        for i in range(len(s)):
            if (s[i]['skill_name'].replace(" ", "").lower()) == data['skill_name'].replace(" ", "").lower():
                return jsonify(
                    {
                        "code": 400,
                        "data": {
                            "skill_name": data['skill_name']
                        },
                        "message": "Skill name already exist!"
                    }
                ), 400
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


# ********************************* Retrieve ********************************* 
# Get all skills
def get_skills():
    skills = Skill.query.all()
    if skills:
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

# Get all skill ids
def get_skill_id(skill_name):
    role = Skill.query.filter_by(skill_name=skill_name)
    if role:
        return jsonify(
            {
                "code": 200,
                "message":  [r.json() for r in role]
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Not Found"
        }
    ), 404

# Get skill by id
def get_skill_by_id(skill_id):

    skill = Skill.query.filter_by(skill_id=skill_id)
    if skill:
        return jsonify(
            {
                "code": 200,
                "message":  [s.json() for s in skill]
            }
        )
    return jsonify(
        {
            "code": 404,

            "message": "Not Found"
        }
    )


# ********************************* Update ********************************* 
# Update skill by id
def update_skill(skill_id):
    data = request.get_json()
    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if skill:
        exist_skill = Skill.query.filter_by(skill_name=str(data['skill_name']).strip()).first()
        if exist_skill and exist_skill.skill_id != skill_id:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "skill_name": data['skill_name']
                    },
                    "message": "Skill name already exist!"
                }
            ), 400
        else:
            skill.skill_name = str(data['skill_name']).strip()
            skill.skill_desc = data['skill_desc']
            skill.skill_status = data['skill_status']
        try:
            db.session.commit()
        except:
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
                "data": skill.json(),
                "message": "Skill successfully updated"
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "skill_id": skill_id
                },
                "message": "Skill not found."
            }
        ), 404

# ********************************* Delete ********************************* 
# Delete skill by id
def delete_skill(skill_id):
    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if skill:
        db.session.delete(skill)
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
            "message": "Skill not found."
        }
    ), 404
