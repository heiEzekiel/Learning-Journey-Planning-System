import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Registration import Registration

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

class TestRegistration(TestApp):
    def test_get_courses_registration(self):
        registration = Registration("1", 1, "Registered", "Completed")
        db.session.add(registration)
        db.session.commit()

        response = self.client.get('/getCourseReg/1')
        self.assertEqual(response.json, 
            {
                'code': 200,
                'data': [
                    {
                        'completion_status' : 'Completed',
                        'course_id' : '1',
                        'reg_status' : 'Registered',
                        'staff_id' : 1
                    }
                ]
            }
        )

        
if __name__ == '__main__':
    unittest.main()