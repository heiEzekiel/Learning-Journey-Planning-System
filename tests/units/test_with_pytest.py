from backend.app import Job_Role, Role_Map, Course_Map, Course, Skill, Journey, Journey_Map
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