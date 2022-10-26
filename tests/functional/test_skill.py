import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Skills import Skill

class TestApp(flask_testing.TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
        app.config['TESTING'] = True
        return app

    def setUp(self):
        db.create_all() 

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestSkill(TestApp):
    def test_create_skill(self):
        request_body = {
            "skill_name": "Python",
            "skill_desc": "Python skill",
        }
        response = self.client.post('/createSkills', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": {
                "skill_desc": "Python skill",
                "skill_id": 1,
                "skill_name": "Python",
                "skill_status": 0
            }})
    
    def test_create_skill_with_duplicates(self):
        skill = Skill("Java", "Java skill", 1)
        db.session.add(skill)
        db.session.commit()

        request_body = {
            "skill_name": "Java",
            "skill_desc": "Java skill",
            "skill_status": 1
        }
        response = self.client.post('/createSkills', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code": 400,
            "data": {
                "skill_name": "Java"
            },
            "message": "Skill name already exist!"
            }
        )
    
    def test_get_skill(self):
        skill = Skill(skill_name="Python", skill_desc="Python skill", skill_status=1)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get('/getskills')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": {
                "skill" : [
                    {
                        "skill_desc": "Python skill",
                        "skill_id": 1,
                        "skill_name": "Python",
                        "skill_status": 1
                    }
                ]
            }
        })
    
    def test_get_skill_with_no_data(self):
        response = self.client.get('/getskills')
        self.assertEqual(response.json, {
            "code": 404,
            "message": "No skills found."
        })
    
    def test_get_specific_skill_id(self):
        skill = Skill("Python", "Python skill", 1)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get('/getSkillID/Python')
        self.assertEqual(response.json, {
            "code" : 200,
            'message' : [
                {
                    "skill_desc": "Python skill",
                    "skill_id": 1,
                    "skill_name": "Python",
                    "skill_status": 1
                }
            ]
        })

    def test_get_skill_by_id(self):
        skill = Skill("Python", "Python skill", 1)
        db.session.add(skill)
        db.session.commit()

        response = self.client.get('/getSkillById/1')
        self.assertEqual(response.json, {
            "code" : 200,
            'message' : [
                {
                    "skill_desc": "Python skill",
                    "skill_id": 1,
                    "skill_name": "Python",
                    "skill_status": 1
                }
            ]
        })
    
    def test_update_skill(self):
        skill = Skill("Java", "Java skill", 1)
        db.session.add(skill)
        db.session.commit()

        request_body = {
            "skill_name": "Java",
            "skill_desc": "Java OOP",
            "skill_status": 1
        }
        response = self.client.put('/updateSkill/1', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": {
                "skill_desc": "Java OOP",
                "skill_id": 1,
                "skill_name": "Java",
                "skill_status": 1
            },
            "message": "Skill successfully updated"
        })

    def test_update_skill_with_no_data(self):
        request_body = {
            "skill_name": "Python",
            "skill_desc": "Python skill",
            "skill_status": 1
        }
        response = self.client.put('/updateSkill/1', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "code": 404,
                "data": {
                    "skill_id": 1
                },
                "message": "Skill not found."
            })
        
    def test_delete_skill(self):
        skill = Skill("Java", "Java skill", 1)
        db.session.add(skill)
        db.session.commit()

        response = self.client.delete('/deleteSkill/1')
        self.assertEqual(response.json, {
            "code" : 200,
            "message": "Skill removed successfully"
        })

if __name__ == '__main__':
    unittest.main()
    

