from backend.app import Skill, change_apt
from flask import Flask
import json
import pytest 

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


def test_update_skill_success():
    """
    GIVEN a Skill model
    WHEN a new Skill is updated
    THEN check the new skill_name, skill_desc, skill_status are defined correctly
    """
    app = Flask(__name__)
    
    test_data_skill2 = Skill(skill_name="Java", skill_desc="Java is a programming language", skill_status=1)
    test_data_skill2.skill_id = 2

    new_data = {
        'skill_name' : 'Python',
        'skill_desc' : 'Python is a programming language',
    }
    with app.app_context():
        result_data = change_apt(2, test_data_skill2, new_data)
        assert result_data.status_code == 200
        assert result_data.get_json()['data']['skill_name'] == 'Python'
        assert result_data.get_json()['data']['skill_desc'] == 'Python is a programming language'

