import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Job_Role import Job_Role

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root@localhost:3306/LJPS_DB"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestJobRole(TestApp):
    def test_create_job_role(self):
        request_body = {
            "job_role_name": "Human Resource",
            "job_role_desc": "Human Resource is a job role",
            "job_role_status": 1
        }
        with app.app_context():
            response = self.client.post("/createJobRole",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
            assert response.json['code'] == 201
            assert response.json['message'] == "Job Role successfully created"
            assert response.json['data']['job_role_name'] == "Human Resource"
            assert response.json['data']['job_role_desc'] == "Human Resource is a job role"
            assert response.json['data']['job_role_status'] == 1
    #deletion
        
    

