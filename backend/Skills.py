from flask import  request, jsonify
import db_connector
db = db_connector.db_connector()

# Skill Table
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
        return {
            "skill_id": self.skill_id,
            "skill_name": self.skill_name,
            "skill_desc": self.skill_desc,
            "skill_status": self.skill_status
        }

#Functions (CRUD)
# ********************************* Create ********************************* 
# Create a new skill
def create_skills(test_data=""):
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
    if test_data == "":
        # check is existing role is there
        skills = Skill.query.all()
        if skills != None:
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


# ********************************* Retrieve ********************************* 
# Get all skills
def get_skills(test_data=""):
    skills = None
    if test_data == "":
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
    else:
        skills=test_data
        if skills:
            return jsonify(
                {
                    "code": 200,
                    "data":
                    [skill.json() for skill in test_data]
                }
            )
        else:
            return jsonify(
                {
                    "code": 424,
                    "data": 'No record found'
                }
            )

# Get all skill ids
def get_skill_id(skill_name, test_data=""):
    role = None
    if test_data == "":
        role = Skill.query.filter_by(skill_name=skill_name)
    else:
        role = test_data
    if role and test_data == "":
        return jsonify(
            {
                "code": 200,
                "message":  [r.json() for r in role]
            }
        )
    elif role and test_data != "":
        for r in role:
            if r.skill_name == skill_name:
                return jsonify(
                    {
                        "code": 200,
                        "message": r.json()
                    }
                )
    return jsonify(
        {
            "code": 404,
            "message": "Not Found"
        }
    ), 404

# Get skill by id
def get_skill_by_id(skill_id, test_data=""):
    skill = None
    if test_data == "":
        skill = Skill.query.filter_by(skill_id=skill_id)
    else:
        skill = test_data
    if skill and test_data == "":
        return jsonify(
            {
                "code": 200,
                "message":  [s.json() for s in skill]
            }
        )
    elif skill and test_data != "":
        for s in skill:
            if s.skill_id == skill_id:
                return jsonify(
                    {
                        "code": 200,
                        "message": s.json()
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
def update_skill(skill_id, test_data="", new_data="", test_data2=""):
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

     # check is existing role is there
        if test_data == "":
            skills = Skill.query.all()
        else:
            skills = test_data2
        if skills != None:
            res = (
                {
                    "code": 200,
                    "data":  [s.json() for s in skills]
                }
            )
            s = res['data']
            for i in range(len(s)):
                if (preskill.replace(" ", "").lower() == s[i]['skill_name'].replace(" ", "").lower()):
                    continue
                if (s[i]['skill_name'].replace(" ", "").lower()) == data['skill_name'].replace(" ", "").lower():
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
        if data['skill_status']:
            skill.skill_status = data['skill_status']

        # if no duplicate skill then run these codes
        if test_data == "" and new_data == "":
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


# ********************************* Delete ********************************* 
# Delete skill by id
def delete_skill(skill_id, test_data=""):
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
                "message": "Skill removed successfully"
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
                "message": "Skill removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skill not found."
        }
    ), 404
