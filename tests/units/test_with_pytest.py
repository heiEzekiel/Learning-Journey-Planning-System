from backend.app import JobRole, role_map, Skill, getSpecificJobRole, getSkillsForJob, change_apt
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

#----------------------check class_role_map----------------------
def test_class_role_map_suceess():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the job_role_id and skill_id are an valid integer
    """
    role_map1 = role_map(1, 1)
    assert role_map1.job_role_id == 1
    assert role_map1.skill_id == 1

def test_class_role_map_fail():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the job_role_id are an valid integer
    """
    with pytest.raises(TypeError):
        JobRole('1', 1)

def test_class_role_map_fail1():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the skill_id are an valid integer
    """
    with pytest.raises(TypeError):
        JobRole(1, '1')


#----------------------check function getSkillsForJob----------------------

def test_get_skills_for_job_success():
    """
    GIVEN a function getSkillsForJob
    WHEN a new role_map is created
    THEN check the function is returning the correct data
    """
    app = Flask(__name__)

    test_data_role_map = [
        role_map(1, 1),
        role_map(1, 2),
        role_map(1, 3),
        role_map(2, 2),
        role_map(2, 3),
    ]

    test_data_skill1 = Skill('skill1', 'desc1', 0)
    test_data_skill1.skill_id = 1
    test_data_skill2 = Skill('skill2', 'desc2', 0)
    test_data_skill2.skill_id = 2
    test_data_skill3 = Skill('skill3', 'desc3', 0)
    test_data_skill3.skill_id = 3

    test_data_skill = [
        test_data_skill1,
        test_data_skill2,
        test_data_skill3
    ]

    test_data_job_role1 = JobRole('job1', 'jobdesc1', 0)
    test_data_job_role1.job_role_id = 1
    test_data_job_role2 = JobRole('job2', 'jobdesc2', 0)
    test_data_job_role2.job_role_id = 2
    test_data_job_role = [
        test_data_job_role1,
        test_data_job_role2
    ]

    with app.app_context():
        result_data = getSkillsForJob(1, test_data_role_map, test_data_skill, test_data_job_role)
        assert result_data.status_code == 200
        assert result_data.json == [{
            "code": 200,
            "data": [
                ['skill1', 'desc1'],
                ['skill2', 'desc2'],
                ['skill3', 'desc3']
            ]
        }, 200]

#----------- test_view_job_role ------------------
def test_view_job_role_success():
    app = Flask(__name__)

    test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getSpecificJobRole(1, [ 
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

def test_update_role_success():
    """
    GIVEN a Role model
    WHEN a new Role is updated
    THEN check the new job_role_name, job_role_desc, job_role_status are defined correctly
    """
    app = Flask(__name__)
    
    test_data_jobrole2 = JobRole('Human Resource', 'HR', 0)
    test_data_jobrole2.job_role_id = 2

    new_data = {
        'job_role_name' : 'Software Developer',
        'job_role_desc' : 'SD',
    }
    with app.app_context():
        result_data = change_apt(2, test_data_jobrole2, new_data)
        assert result_data.status_code == 200
        assert result_data.get_json()['data']['job_role_name'] == 'Software Developer'
        assert result_data.get_json()['data']['job_role_desc'] == 'SD'

