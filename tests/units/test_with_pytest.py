from backend.app import role_map, JobRole, Skill, getSkillsForJob, createSkills
from flask import Flask
import json
import pytest 

#----------------------check Class skill----------------------
def test_skill_success():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    skill = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
    assert skill.skill_name == "Python"
    assert skill.skill_desc == "Python is a programming language"
    assert skill.skill_status == 1

def test_skill_invalid_skill_name():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_name
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name=0, skill_desc="Python is a programming language", skill_status=1)

def test_skill_invalid_skill_desc():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_desc
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc=0, skill_status=1)

def test_skill_invalid_skill_status():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_status
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status="1")

def test_skill_invalid_parameters():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with invalid amount of parameters parameters
    THEN check the Exception is raised
    """
    with pytest.raises(Exception):
        Skill(skill_id=0, skill_name=0, skill_desc=0, skill_status="1")

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


#-------------------------test function createSkills-----------------------------------
def test_new_skill():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_status, skill_name, skill_desc are defined correctly
    """
    app = Flask(__name__)

    test_data = {
        "skill_name": "Python",
        "skill_desc": "Python is a programming language",
        "skill_status": 1
    }

    with app.app_context():
        result_data = createSkills(test_data)
        assert result_data.json['code'] == 200
        assert result_data.json['data']['skill_status'] == 1
        assert result_data.json['data']['skill_name'] == "Python"
        assert result_data.json['data']['skill_desc'] == "Python is a programming language"




