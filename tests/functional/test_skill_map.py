import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Skills import Skill
from backend.Skill_Map import Skill_Map

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

class TestSkillMap(TestApp):
    def test_get_staff_skills(self):
        skill = Skill(skill_name="Python", skill_desc="Python skill", skill_status=1)
        db.session.add(skill)
        db.session.commit()
        skill_map = Skill_Map(1, 1)
        db.session.add(skill_map)
        db.session.commit()

        response = self.client.get('/getSkillStaff/1')
        self.assertEqual(response.json, {
            'code': 200, 
            'data': [
                {
                    'sm_fk_skill_id': 1, 
                    'sm_fk_staff_id': 1
                }
            ]}
        )
    

    
if __name__ == '__main__':
    unittest.main()
    

