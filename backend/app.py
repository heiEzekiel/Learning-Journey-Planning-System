import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from os import environ

app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/LJPS_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

CORS(app)

db = SQLAlchemy(app)

class Skill(db.Model):
    __tablename__ = 'Skill'
    skill_id = db.Column(db.Integer, primary_key=True, nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    skill_desc = db.Column(db.String(255), nullable=False)
    skill_status = db.Column(db.Integer, nullable=False)
    def __init__(self, skill_id, skill_name, skill_desc, skill_status):
        self.skill_id = skill_id
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

@app.route("/")
def home():
    pass

#skill = Skill.query.all()

@app.route("/getskills")
def getskills():
    skills = Skill.query.all()
    print(skills)
    return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": [skill.json() for skill in skills]
                }
            }
        )

if __name__ == "__main__":
    app.run()