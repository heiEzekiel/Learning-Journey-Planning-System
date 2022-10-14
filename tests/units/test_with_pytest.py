from backend.app import Job_Role, Role_Map, Course_Map, Course, Skill, Journey, Journey_Map, \
deleteRole, create_job_role, getSpecificJobRole, getSkillsForJob, updateRole, createSkills, \
getAllJobRole, getskills, updateSkill, createRoleMap, del_role, getCoursesForSkill, getSkillID, \
getSkillById, getSkillById, deleteSkill, createJourneyMap
    
from flask import Flask
import json
import pytest 

#----------- test Class Job_Role ------------------
def test_job_role_success():
    """
    GIVEN a Job_Role model
    WHEN a new Job_Role is created
    THEN check the job_role_name, job_role_desc, job_role_status are defined correctly
    """
    test_job_role = Job_Role('Human Resource', 'HR', 0)
    assert test_job_role.job_role_name == 'Human Resource'
    assert test_job_role.job_role_desc == 'HR'
    assert test_job_role.job_role_status == 0

def test_job_role_invalid_name():
    """
    GIVEN a Job_Role model
    WHEN a new Job_Role is created with an invalid job_role_name
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        Job_Role(123, 'HR', 0)

def test_job_role_invalid_desc():
    """
    GIVEN a Job_Role model
    WHEN a new Job_Role is created with an invalid job_role_desc
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        Job_Role('Human Resource', 123, 0)

def test_job_role_invalid_status():
    """
    GIVEN a Job_Role model
    WHEN a new Job_Role is created with an invalid job_role_status
    THEN check the TypeError is raised
    """
    with pytest.raises(TypeError):
        Job_Role('Human Resource', 'HR', '0')\

def test_job_role_invalid_parameters():
    """
    GIVEN a Job_Role model
    WHEN a new Job_Role is created with invalid amount of parameters
    THEN check the TypeError is raised
    """
    with pytest.raises(Exception):
        Job_Role(0, 'Human Resource', 'HR', 0)

#----------------------test Class Role_map----------------------
def test_class_role_map_suceess():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the job_role_id and skill_id are an valid integer
    """
    role_map1 = Role_Map(1, 1)
    assert role_map1.rm_fk_job_role_id == 1
    assert role_map1.rm_fk_skill_id == 1

def test_class_role_map_fail():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the job_role_id are an valid integer
    """
    with pytest.raises(TypeError):
        Role_Map('1', 1)

def test_class_role_map_fail1():
    """
    GIVEN a role_map class
    WHEN a new role_map is created
    THEN check the skill_id are an valid integer
    """
    with pytest.raises(TypeError):
        Role_Map(1, '1')

#----------------------test Class course_map----------------------
def test_course_map_suceess():
    """
    GIVEN a course_map class
    WHEN a new course_map is created
    THEN check the course_id and skill_id are an valid integer
    """
    course_map1 = Course_Map('1', 1)
    assert course_map1.cm_fk_course_id == '1'
    assert course_map1.cm_fk_skill_id == 1

def test_course_map_fail():
    """
    GIVEN a course_map class
    WHEN a new course_map is created
    THEN check the course_id is an valid string
    """
    with pytest.raises(TypeError):
        Course_Map(1, 1)

def test_course_map_fail1():
    """
    GIVEN a course_map class
    WHEN a new course_map is created
    THEN check the skill_id is an valid integer
    """
    with pytest.raises(TypeError):
        Course_Map('1', '1')

#----------------------test Class Course----------------------
def test_class_course_suceess():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_id, course_name, course_desc, course_status, course_tyep, course_category are of valid type
    """
    course1 = Course('1', 'Human Resource', 'HR', '0', '1', '1')
    assert course1.course_id == '1'
    assert course1.course_name == 'Human Resource'
    assert course1.course_desc == 'HR'
    assert course1.course_status == '0'
    assert course1.course_type == '1'
    assert course1.course_category == '1'

def test_class_course_fail():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_id is an valid string
    """
    with pytest.raises(TypeError):
        Course(1, 'Human Resource', 'HR', '0', '1', '1')

def test_class_course_fail1():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_name is an valid string
    """
    with pytest.raises(TypeError):
        Course('1', 1, 'HR', '0', '1', '1')
    
def test_class_course_fail2():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_desc is an valid string
    """
    with pytest.raises(TypeError):
        Course('1', 'Human Resource', 1, '0', '1', '1')
    
def test_class_course_fail3():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_status is an valid string
    """
    with pytest.raises(TypeError):
        Course('1', 'Human Resource', 'HR', 1, '1', '1')

def test_class_course_fail4():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_type is an valid string
    """
    with pytest.raises(TypeError):
        Course('1', 'Human Resource', 'HR', '0', 1, '1')
    
def test_class_course_fail5():
    """
    GIVEN a course class
    WHEN a new course is created
    THEN check the course_category is an valid string
    """
    with pytest.raises(TypeError):
        Course('1', 'Human Resource', 'HR', '0', '1', 1)

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

#-------------------------test class Journey-----------------------------------
def test_class_journey_success():
    """
    GIVEN a Journey model
    WHEN a new Journey is created
    THEN check the journey_name, journey_status, j_fk_staff_id, j_fk_job_role_id are defined correctly
    """
    journey = Journey(journey_name = "1",journey_status="1", j_fk_staff_id=1, j_fk_job_role_id=1)
    assert journey.journey_name == "1"
    assert journey.journey_status == "1"
    assert journey.j_fk_staff_id == 1
    assert journey.j_fk_job_role_id == 1

def test_class_journey_fail():
    """
    GIVEN a Journey model
    WHEN a new Journey is created
    THEN check the journey_status is an valid string
    """
    with pytest.raises(TypeError):
        Journey(journey_name = "1",journey_status=1, j_fk_staff_id=1, j_fk_job_role_id=1)

def test_class_journey_fail1():
    """
    GIVEN a Journey model
    WHEN a new Journey is created
    THEN check the j_fk_staff_id is an valid string
    """
    with pytest.raises(TypeError):
        Journey(journey_name = "1",journey_status="1", j_fk_staff_id="1", j_fk_job_role_id=1)

def test_class_journey_fail2():
    """
    GIVEN a Journey model
    WHEN a new Journey is created
    THEN check the j_fk_job_role_id is an valid string
    """
    with pytest.raises(TypeError):
        Journey(journey_name = "1",journey_status="1", j_fk_staff_id=1, j_fk_job_role_id="1")

#-------------------------test class Journey_Map---------------------------
def test_class_journey_map_success():
    """
    GIVEN a Journey_Map model
    WHEN a new Journey_Map is created
    THEN check the jm_fk_journey_id, jm_fk_course_id, jm_fk_skill_id are defined correctly
    """
    journey_map = Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")
    assert journey_map.jm_fk_journey_id == 1
    assert journey_map.jm_fk_course_id == "1"

def test_class_journey_map_fail():
    """
    GIVEN a Journey_Map model
    WHEN a new Journey_Map is created
    THEN check the jm_fk_journey_id is an valid string
    """
    with pytest.raises(TypeError):
        Journey_Map(jm_fk_journey_id="1", jm_fk_course_id="1")

def test_class_journey_map_fail1():
    """
    GIVEN a Journey_Map model
    WHEN a new Journey_Map is created
    THEN check the jm_fk_course_id is an valid string
    """
    with pytest.raises(TypeError):
        Journey_Map(jm_fk_journey_id=1, jm_fk_course_id=1)

#----------------------test function create_job_role----------------------
def test_create_job_role_success():
    """
    GIVEN a function create_job_role
    WHEN create a new job role
    THEN check the job role is created successfully
    """
    app = Flask(__name__)

    test_data_job_role = {
        "job_role_name": "Human Resource",
        "job_role_desc": "Human Resource is a job role",
        "job_role_status": 1
    }

    with app.app_context():
        result_data = create_job_role(test_data_job_role)
        assert result_data.json['code'] == 201
        assert result_data.json['message'] == "Job Role successfully created"
        assert result_data.json['data']['job_role_name'] == "Human Resource"
        assert result_data.json['data']['job_role_desc'] == "Human Resource is a job role"
        assert result_data.json['data']['job_role_status'] == 1

#----------------------test function getSpecificJobRole----------------------
def test_getSpecificJobRole_success():
    """
    GIVEN a function getSpecificJobRole
    WHEN get a specific job role
    THEN check the job role is retrieved successfully
    """
    test_data = {
        Job_Role(job_role_name="Human Resource", job_role_desc="Human Resource is a job role", job_role_status=1)
    }
    app = Flask(__name__)

    with app.app_context():
        result_data = getSpecificJobRole(1, test_data)
        assert result_data.json['code'] == 200
        assert result_data.json['data'][0]['job_role_name'] == "Human Resource"
        assert result_data.json['data'][0]['job_role_desc'] == "Human Resource is a job role"
        assert result_data.json['data'][0]['job_role_status'] == 1

#----------- test function getAllJobRole --------------------------
def test_view_job_role_success():
    app = Flask(__name__)

    test_data = [
        ['Human Resource', 'HR', 0],
        ['Software Engineer', 'SE', 0],
        ['Data Scientist', 'DS', 0]
    ]

    with app.app_context():
        result_data = getAllJobRole([ 
            Job_Role(test_data[0][0], test_data[0][1], test_data[0][2]),
            Job_Role(test_data[1][0], test_data[1][1], test_data[1][2]),
            Job_Role(test_data[2][0], test_data[2][1], test_data[2][2])
        ])

        assert result_data.json['code'] == 200
        assert len(result_data.json['data']) == 3
        for i in range(len(test_data)):
            assert result_data.json['data'][i]['job_role_name'] == test_data[i][0]
            assert result_data.json['data'][i]['job_role_desc'] == test_data[i][1]
            assert result_data.json['data'][i]['job_role_status'] == test_data[i][2]
    
#----------------------test function updateRole----------------------
def test_update_role_success():
    """
    GIVEN a Role model
    WHEN a new Role is updated
    THEN check the new job_role_name, job_role_desc, job_role_status are defined correctly
    """
    app = Flask(__name__)
    
    test_data_jobrole2 = Job_Role('Human Resource', 'HR', 0)
    test_data_jobrole2.job_role_id = 2

    new_data = {
        'job_role_name' : 'Software Developer',
        'job_role_desc' : 'SD',
    }

    existing_data= [Job_Role('Teacher', 'TR', 0),Job_Role('Developer', 'Dev', 0)]
    with app.app_context():
        result_data = updateRole(2, test_data_jobrole2, new_data, existing_data)
        assert result_data.status_code == 200
        assert result_data.get_json()['data']['job_role_name'] == 'Software Developer'
        assert result_data.get_json()['data']['job_role_desc'] == 'SD'

#----------- test function deleteRole ------------------
def test_delete_role_success():
    """
    GIVEN a Role model
    WHEN a new Role is deleted
    THEN check the job_role_id is deleted correctly
    """
    app = Flask(__name__)
    test_data_jobrole1 = Job_Role('Human Resource', 'HR', 0)
    test_data_jobrole1.job_role_id = 1
    test_data_jobrole2 = Job_Role('Software Developer', 'SD', 0)
    test_data_jobrole2.job_role_id = 2
    test_data_jobrole3 = Job_Role('Teacher', 'TR', 0)
    test_data_jobrole3.job_role_id = 3

    existing_data= [test_data_jobrole1, test_data_jobrole2, test_data_jobrole3]
    with app.app_context():
        result_data = deleteRole(2, test_data_jobrole2, existing_data)
        assert result_data.get_json()['code'] == 200
        assert result_data.get_json()['message'] == 'Job removed successfully'

#----------------------test function createRoleMap----------------------
def test_create_role_map_success():
    """
    GIVEN a function createRoleMap
    WHEN create a new role map
    THEN check the role map is created successfully
    """
    app = Flask(__name__)

    role_map1 = Role_Map(1, 1)

    with app.app_context():
        result_data = createRoleMap(1,1,role_map1)
        assert result_data.json['code'] == 201
        assert result_data.json['message'] == "Success"
        assert result_data.json['data']['rm_fk_job_role_id'] == 1
        assert result_data.json['data']['rm_fk_skill_id'] == 1

#----------------------check function getSkillsForJob----------------------
def test_get_skills_for_job_success():
    """
    GIVEN a function getSkillsForJob
    WHEN a new role_map is created
    THEN check the function is returning the correct data
    """
    app = Flask(__name__)

    test_data_role_map = [
        Role_Map(1, 1),
        Role_Map(1, 2),
        Role_Map(1, 3),
        Role_Map(2, 2),
        Role_Map(2, 3),
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

    test_data_job_role1 = Job_Role('job1', 'jobdesc1', 0)
    test_data_job_role1.job_role_id = 1
    test_data_job_role2 = Job_Role('job2', 'jobdesc2', 0)
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
                ['skill1', 'desc1',1],
                ['skill2', 'desc2',2],
                ['skill3', 'desc3',3]
            ]
        }, 200]

#----------------------test function del_role----------------------
def test_del_role_success():
    """
    GIVEN a function del_role
    WHEN delete a role
    THEN check the role is deleted successfully
    """
    app = Flask(__name__)

    test_data_role_map = [
        Role_Map(1, 1),
        Role_Map(1, 2),
        Role_Map(1, 3),
        Role_Map(2, 2),
        Role_Map(2, 3),
    ]

    with app.app_context():
        result_data = del_role(1, 1, Role_Map(1, 1), test_data_role_map)
        assert result_data.status_code == 200
        assert result_data.json['code'] == 200
        assert result_data.json['message'] == 'Skill removed successfully'

#----------------------test function getCoursesForSkill----------------------
def test_get_courses_for_skill_success():
    """
    GIVEN a function getCoursesForSkill
    WHEN a new course_skill is created
    THEN check the function is returning the correct data
    """
    app = Flask(__name__)

    test_data_course_skill = [
        Course_Map('1', 1),
        Course_Map('1', 2),
        Course_Map('1', 3),
        Course_Map('2', 2),
        Course_Map('2', 3),
    ]

    
    test_data_course = [
        Course('1', 'Human Resource', 'HR', '0', '1', '1'),
        Course('2', 'Software Developer', 'SD', '0', '1', '1'),
        Course('3', 'Teacher', 'TR', '0', '1', '1')
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

    with app.app_context():
        result_data = getCoursesForSkill(3, test_data_course_skill, test_data_course, test_data_skill)
        assert result_data.status_code == 200
        assert result_data.json[0]['code'] == 200
        assert len(result_data.json[0]['data']) == 2

#----------------------test function getSkillID--------------------
def test_get_skill_id_success():
    """
    GIVEN a function getSkillID
    WHEN get a skill id
    THEN check the function is returning the correct data
    """
    app = Flask(__name__)

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

    with app.app_context():
        result_data = getSkillID('skill2', test_data_skill)
        assert result_data.json['code'] == 200
        assert result_data.json['message']['skill_desc'] == 'desc2'
        assert result_data.json['message']['skill_name'] == 'skill2'
        assert result_data.json['message']['skill_id'] == 2
        assert result_data.json['message']['skill_status'] == 0

#----------------------test function getSkillById--------------------
def test_get_skill_by_id_success():
    """
    GIVEN a function getSkillById
    WHEN get a skill by id
    THEN check the function is returning the correct data
    """
    app = Flask(__name__)

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

    with app.app_context():
        result_data = getSkillById(2, test_data_skill)
        assert result_data.json['code'] == 200
        assert result_data.json['message']['skill_desc'] == 'desc2'
        assert result_data.json['message']['skill_name'] == 'skill2'
        assert result_data.json['message']['skill_id'] == 2
        assert result_data.json['message']['skill_status'] == 0

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

#-------------------------test function createSkills-----------------------------------
def test_create_skills():
    """
    GIVEN a Skill model
    WHEN a new Skill is created
    THEN check the skill_status, skill_name, skill_desc are defined correctly
    """
    app = Flask(__name__)

    test_data = {
        "skill_name": "Python",
        "skill_desc": "Python is a programming language",
        "skill_status": 0
    }

    with app.app_context():
        result_data = createSkills(test_data)
        assert result_data.json['code'] == 200
        assert result_data.json['data']['skill_status'] == 0
        assert result_data.json['data']['skill_name'] == "Python"
        assert result_data.json['data']['skill_desc'] == "Python is a programming language"

#-------------------------test function updateSkill-----------------------------------
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

    test_data_existing=[Skill(skill_name="C sharp", skill_desc="C sharp is a programming language", skill_status=1),Skill(skill_name="Android Studio", skill_desc="This is an IDE", skill_status=1)]



    with app.app_context():
        result_data = updateSkill(2, test_data_skill2, new_data,test_data_existing)
        assert result_data.status_code == 200
        assert result_data.get_json()['data']['skill_name'] == 'Python'
        assert result_data.get_json()['data']['skill_desc'] == 'Python is a programming language'

#-------------------------test function deleteSkill-----------------------------------
def test_delete_skill_success():
    """
    GIVEN a Skill model
    WHEN a new Skill is deleted
    THEN check the skill_status is changed to 1
    """
    app = Flask(__name__)
    test_data_skill1 = Skill(skill_name="Java", skill_desc="Java is a programming language", skill_status=1)
    test_data_skill1.skill_id = 1
    test_data_skill2 = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
    test_data_skill2.skill_id = 2
    test_data_skill3 = Skill(skill_name="C sharp", skill_desc="C sharp is a programming language", skill_status=1)
    test_data_skill3.skill_id = 3

    test_data_existing=[
        test_data_skill1,
        test_data_skill2,
        test_data_skill3
    ]

    with app.app_context():
        result_data = deleteSkill(2,test_data_existing)
        assert result_data.status_code == 200
        assert result_data.get_json()['code'] == 200
        assert result_data.get_json()['message'] == 'Skill removed successfully'

#-------------------------test function createJourney-----------------------------------
def test_create_journey_success():
    pass

#-------------------------test function createJourneyMap-----------------------------------
def test_create_journey_map_success():
    """
    GIVEN a Journey_Map model
    WHEN a new Journey_Map is created
    THEN check the jm_fk_journey_id and jm_fk_course_id are defined correctly
    """
    app = Flask(__name__)

    journey_map = Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")


    with app.app_context():
        result_data = createJourneyMap(None,None,journey_map)
        assert result_data.json['code'] == 201
        assert result_data.json['data']['jm_fk_journey_id'] == 1
        assert result_data.json['data']['jm_fk_course_id'] == "1"
        assert result_data.json['message'] == 'Success'



