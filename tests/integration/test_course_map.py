import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Skills import Skill
from backend.Courses import Course
from backend.Course_Map import Course_Map

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

class TestCourseMap(TestApp):
    def test_create_course_skill_map(self):
        request_body = {
            "cm_fk_course_id": "1",
            "cm_fk_skill_id": 1,
        }
        response = self.client.post('/createSkillMap/1/1', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            'code': 201,
            'data': {
                'cm_fk_course_id': '1', 
                'cm_fk_skill_id': 1
            },
            'message': 'Success'
        })
    
    def test_get_skills_for_course(self):
        skill = Skill(skill_name="Python", skill_desc="Python skill", skill_status=1)
        db.session.add(skill)
        db.session.commit()
        course_map = Course_Map("1", 1)
        db.session.add(course_map)
        db.session.commit()

        response = self.client.get('/getSkillsForCourse/1')
        self.assertEqual(response.json, [
            {
                'code': 200, 
                'data': [
                    ['Python', 'Python skill', 1]
                ]}, 200
            ])
    
    def test_get_courses_for_skill(self):
        course = Course(course_id="1", course_name="Python", course_desc="Python course", course_status="1", course_type="1", course_category="Programming")
        db.session.add(course)
        db.session.commit()
        course_map = Course_Map("1", 1)
        db.session.add(course_map)
        db.session.commit()

        response = self.client.get('/getCoursesForSkill/1')
        self.assertEqual(response.json, [
            {
                'code': 200,
                'data': [
                    {
                        'course_category': 'Programming',
                        'course_desc': 'Python course',
                        'course_id': '1',
                        'course_name': 'Python',
                        'course_status': '1',
                        'course_type': '1'
                    }
                ]},
            200]
        )
    
    def test_delete_skill_from_course(self):
        course = Course(course_id="1", course_name="Python", course_desc="Python course", course_status="1", course_type="1", course_category="Programming")
        db.session.add(course)
        db.session.commit()
        course_map = Course_Map("1", 1)
        db.session.add(course_map)
        db.session.commit()
        response = self.client.delete('/removeSkillFromCourse/1/1')
        self.assertEqual(response.json, {
            'code': 200,
            'message' : 'Course removed successfully'
        })
    
    
if __name__ == '__main__':
    unittest.main()