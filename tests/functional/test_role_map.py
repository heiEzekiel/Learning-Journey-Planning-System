import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Skills import Skill
from backend.Role_Map import Role_Map

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

class TestRoleMap(TestApp):
    def test_create_role_map(self):
        request_body = {
            "rm_fk_job_role_id": 1,
            "rm_fk_skill_id": 1,
        }
        response = self.client.post('/createRoleMap/1/1', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code" : 201,
            "data": {
                "rm_fk_job_role_id": 1,
                "rm_fk_skill_id": 1,
                },
            "message": "Success"
            })
    def test_get_skills_for_job(self):
        skill = Skill(skill_name="Python", skill_desc="Python skill", skill_status=1)
        db.session.add(skill)
        db.session.commit()
        role_map = Role_Map(1, 1)
        db.session.add(role_map)
        db.session.commit()

        response = self.client.get('/getSkillsForJob/1')
        self.assertEqual(response.json, [
            {
                'code': 200, 
                'data': [
                    ['Python', 'Python skill', 1, 1]
                ]
            }, 200
        ])

    def test_delete_skill_from_job_role(self):
        skill = Skill(skill_name="Python", skill_desc="Python skill", skill_status=1)
        db.session.add(skill)
        db.session.commit()
        role_map = Role_Map(1, 1)
        db.session.add(role_map)
        db.session.commit()

        response = self.client.delete('/removeSkillFromJobRole/1/1')
        self.assertEqual(response.json, 
            {
                "code": 200,
                "message": "Skill removed successfully"
            }
        )
    
if __name__ == '__main__':
    unittest.main()