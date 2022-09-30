from backend.app import Skill, getskills
from flask import Flask
import json
import pytest 


#-------------------------test class Skill-----------------------------------
def test_class_skill_success():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    skill = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
    assert skill.skill_name == "Python"
    assert skill.skill_desc == "Python is a programming language"
    assert skill.skill_status == 1

def test_class_skill_invalid_skill_name():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_name
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name=0, skill_desc="Python is a programming language", skill_status=1)

def test_class_skill_invalid_skill_desc():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_desc
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc=0, skill_status=1)

def test_class_skill_invalid_skill_status():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with an invalid skill_status
    THEN check the skill_name, skill_desc, skill_status are defined correctly
    """
    with pytest.raises(TypeError):
        Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status="1")

def test_class_skill_invalid_parameters():
    """
    GIVEN a Skill model
    WHEN a new Skill is created with invalid amount of parameters parameters
    THEN check the Exception is raised
    """
    with pytest.raises(Exception):
        Skill(skill_id=0, skill_name=0, skill_desc=0, skill_status="1")

#-------------------------test function getskills-----------------------------------
def test_get_skills_success():
    """
    GIVEN a getskills function
    WHEN getskills is called
    THEN check the response code is 200 and the data is returned as per expected
    """
    app = Flask(__name__)
    test_data = test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getskills([
            Skill(test_data[0][0], test_data[0][1], test_data[0][2]),
            Skill(test_data[1][0], test_data[1][1], test_data[1][2]),
            Skill(test_data[2][0], test_data[2][1], test_data[2][2])
        ])
        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
                assert result_data.json['data'][i]['skill_name'] == test_data[i][0]
                assert result_data.json['data'][i]['skill_desc'] == test_data[i][1]
                assert result_data.json['data'][i]['skill_status'] == test_data[i][2]