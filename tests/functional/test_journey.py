import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Journey import Journey

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

class TestJourney(TestApp):
    def test_create_journey(self):
        request_data = {
            "journey_name" : "HR Journey",
            "journey_status" : "Completed",
            "j_fk_staff_id": 1,
            "j_fk_job_role_id": 1
        }
        response = self.client.post('/createJourney', json=request_data)
        self.assertEqual(response.json, 
            {
                'code': 211,
                'data': {
                    'j_fk_job_role_id': 1,
                    'j_fk_staff_id': 1,
                    'journey_id': 1,
                    'journey_name': 'HR Journey',
                    'journey_status': 'Completed'
                }
            }
        )

    def test_get_journey(self):
        journey = Journey(j_fk_staff_id = 1,j_fk_job_role_id = 1,journey_name = 'HR Journey',journey_status = 'Completed')
        db.session.add(journey)
        db.session.commit()

        response = self.client.get('/getJourney/1')
        self.assertEqual(response.json,
            {
                'code': 200,
                'data': [{
                    'j_fk_job_role_id': 1,
                    'j_fk_staff_id': 1,
                    'journey_id': 1,
                    'journey_name': 'HR Journey',
                    'journey_status': 'Completed'
                }]
            }
        )
    
    def test_delete_journey(self):
        journey = Journey(j_fk_staff_id = 1,j_fk_job_role_id = 1,journey_name = 'HR Journey',journey_status = 'Completed')
        db.session.add(journey)
        db.session.commit()

        response = self.client.delete('/deleteJourney/1')
        self.assertEqual(response.json,
            {
                'code': 200,
                'message': 'Journey removed successfully'
            }
        )

if __name__ == '__main__':
    unittest.main()