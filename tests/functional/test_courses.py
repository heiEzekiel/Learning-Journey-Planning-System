import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Courses import Course

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

class TestJobRole(TestApp):
    def test_get_all_courses(self):
        course = Course(course_id="1", course_name="Python", course_desc="Python course", course_status="1", course_type="1", course_category="Programming")
        db.session.add(course)
        db.session.commit()

        response = self.client.get('/getAllCourses')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": [
                {
                    "course_category": "Programming",
                    "course_desc": "Python course",
                    "course_id": "1",
                    "course_name": "Python",
                    "course_status": "1",
                    "course_type": "1"
                }
            ]})

if __name__ == '__main__':
    unittest.main()
    

