import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Journey import Journey
from backend.Journey_Map import Journey_Map

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

class TestJourneyMap(TestApp):
    def test_create_journey_map(self):
        request_data = {
            "jm_fk_journey_id" : 1,
            "jm_fk_course_id": "1",
        }
        response = self.client.post('/createJourneyMap/1/1', json=request_data)
        self.assertEqual(response.json, 
            {
                'code': 201,
                'data': {
                    'jm_fk_course_id': '1', 
                    'jm_fk_journey_id': 1
                },
                'message': 'Success'
            }
        )
    
    def test_get_journey_map(self):
        journey_map = Journey_Map(jm_fk_journey_id = 1, jm_fk_course_id = '1')
        db.session.add(journey_map)
        db.session.commit()

        response = self.client.get('/getJourneyMaps')
        self.assertEqual(response.json,
            {
                'code': 200,
                'data': [{
                    'jm_fk_course_id': '1', 
                    'jm_fk_journey_id': 1
                }]
            }
        )
    
    def test_delete_journey_map(self):
        journey_map = Journey_Map(jm_fk_journey_id = 1, jm_fk_course_id = '1')
        db.session.add(journey_map)
        db.session.commit()

        response = self.client.delete('/deleteJourneyMap/1/1')
        self.assertEqual(response.json,
            {
                "code": 200,
                "message": "Journey Map removed successfully"
            }
        )
if __name__ == '__main__':
    unittest.main()