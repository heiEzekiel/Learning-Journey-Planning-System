from backend.app import JobRole, getAllJobRole
from flask import Flask
import json
import pytest 

#----------- test_create_job_role ------------------
def test_create_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.job_role_name == 'Human Resource'
    assert test_job_role.job_role_desc == 'HR'
    assert test_job_role.job_role_status == 0

def test_create_job_role_invalid_name():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_name
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole(123, 'HR', 0)

def test_create_job_role_invalid_desc():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_desc
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 123, 0)

def test_create_job_role_invalid_status():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with an invalid job_role_status
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        JobRole('Human Resource', 'HR', '0')\

def test_create_job_role_invalid_parameters():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created with invalid amount of parameters
    THEN check the TypeError is raised
    """
    with pytest.raises(Exception):
        JobRole(0, 'Human Resource', 'HR', 0)

def test_view_job_role_success():
    """
    GIVEN a JobRole model
    WHEN a new JobRole is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = JobRole('Human Resource', 'HR', 0)
    assert test_job_role.json()['job_role_name'] == 'Human Resource'
    assert test_job_role.json()['job_role_desc'] == 'HR'
    assert test_job_role.json()['job_role_status'] == 0


#----------- test_view_job_role ------------------
def test_view_job_role_success():
    app = Flask(__name__)

    test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getAllJobRole([ 
            JobRole(test_data[0][0], test_data[0][1], test_data[0][2]),
            JobRole(test_data[1][0], test_data[1][1], test_data[1][2]),
            JobRole(test_data[2][0], test_data[2][1], test_data[2][2])
        ])

        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
            assert result_data.json['data'][i]['job_role_name'] == test_data[i][0]
            assert result_data.json['data'][i]['job_role_desc'] == test_data[i][1]
            assert result_data.json['data'][i]['job_role_status'] == test_data[i][2]


            
        