import unittest
import flask_testing
import json
from backend.app import app, db
from backend.Job_Role import Job_Role

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
    def test_create_job_role(self):
        request_body = {
            "job_role_name": "Human Resource",
            "job_role_desc": "HR's job role",
        }
        response = self.client.post('/createJobRole', 
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
            "code" : 201,
            "data": {
                "job_role_desc": "HR's job role",
                "job_role_id": 1,
                "job_role_name": "Human Resource",
                "job_role_status": 0
            },
            "message": "Job Role successfully created",
        })

    def test_get_job_role(self):
        job_role = Job_Role(job_role_name="Human Resource", job_role_desc="HR's job role", job_role_status=1)
        db.session.add(job_role)
        db.session.commit()

        response = self.client.get('/getAllJobRole')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": [
                {
                    "job_role_desc": "HR's job role",
                    "job_role_id": 1,
                    "job_role_name": "Human Resource",
                    "job_role_status": 1
                }
            ]})


    def test_get_specific_job_role_by_id(self):
        job_role = Job_Role("Human Resource", "HR's job role", 1)
        db.session.add(job_role)
        db.session.commit()
        response = self.client.get('/getSpecificJobRole/1')
        self.assertEqual(response.json, {
            "code" : 200,
            "data": [
                {
                    "job_role_desc": "HR's job role",
                    "job_role_id": 1,
                    "job_role_name": "Human Resource",
                    "job_role_status": 1
                }
            ]})

    def test_update_job_role(self):
        job_role = Job_Role("Human Resource", "HR's job role", 1)
        db.session.add(job_role)
        db.session.commit()

        request_body = {
            "job_role_name": "Software Development",
            "job_role_desc": "SD's job role",
            "job_role_status": 0
        }
        
        response = self.client.put('/updateJobRole/1', 
                                    data=json.dumps(request_body),
                                    content_type='application/json') 
        self.assertEqual(response.json, {
            "code" : 200,
            "data": {
                "job_role_desc": "SD's job role",
                "job_role_id": 1,
                "job_role_name": "Software Development",
                "job_role_status": 0
                },
                "message": "Job Role successfully updated",
            })
    
    def test_delete_job_role(self):
        job_role = Job_Role("Human Resource", "HR's job role", 1)
        db.session.add(job_role)
        db.session.commit()
        
        response = self.client.delete('/deleteRole/1')
        self.assertEqual(response.json, {
            "code" : 200,
            "message" : 'Job removed successfully'
        })

if __name__ == '__main__':
    unittest.main()
    

