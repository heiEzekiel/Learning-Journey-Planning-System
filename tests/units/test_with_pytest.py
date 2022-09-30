from backend.app import role_map, JobRole, Skill, getSkillsForJob
from flask import Flask
import json
import pytest 

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






