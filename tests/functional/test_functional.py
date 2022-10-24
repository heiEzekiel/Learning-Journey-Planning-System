# from backend.app import Job_Role, Role_Map, Course_Map, Course, Skill, Journey, Journey_Map, \
# deleteRole, create_job_role, getSpecificJobRole, getSkillsForJob, updateRole, createSkills, \
# getAllJobRole, getskills, updateSkill, createRoleMap, del_role, getCoursesForSkill, getSkillID, \
# getSkillById, getSkillById, deleteSkill, createJourneyMap, getAllCourses, deleteSkillFromCourse, \
# createSkillMap, getSkillsForCourse, deleteJourneyMap, createJourney\
    
# from flask import Flask
# import json
# import pytest 

# #----------------------test function create_job_role----------------------
# def test_create_job_role_success():
#     """
#     GIVEN a function create_job_role
#     WHEN create a new job role
#     THEN check the job role is created successfully
#     """
#     app = Flask(__name__)

#     test_data_job_role = {
#         "job_role_name": "Human Resource",
#         "job_role_desc": "Human Resource is a job role",
#         "job_role_status": 1
#     }

#     with app.app_context():
#         result_data = create_job_role(test_data_job_role)
#         assert result_data.json['code'] == 201
#         assert result_data.json['message'] == "Job Role successfully created"
#         assert result_data.json['data']['job_role_name'] == "Human Resource"
#         assert result_data.json['data']['job_role_desc'] == "Human Resource is a job role"
#         assert result_data.json['data']['job_role_status'] == 1

# #----------------------test function getSpecificJobRole----------------------
# def test_getSpecificJobRole_success():
#     """
#     GIVEN a function getSpecificJobRole
#     WHEN get a specific job role
#     THEN check the job role is retrieved successfully
#     """
#     test_data = {
#         Job_Role(job_role_name="Human Resource", job_role_desc="Human Resource is a job role", job_role_status=1)
#     }
#     app = Flask(__name__)

#     with app.app_context():
#         result_data = getSpecificJobRole(1, test_data)
#         assert result_data.json['code'] == 200
#         assert result_data.json['data'][0]['job_role_name'] == "Human Resource"
#         assert result_data.json['data'][0]['job_role_desc'] == "Human Resource is a job role"
#         assert result_data.json['data'][0]['job_role_status'] == 1

# #----------- test function getAllJobRole --------------------------
# def test_view_job_role_success():
#     app = Flask(__name__)

#     test_data = [
#         ['Human Resource', 'HR', 0],
#         ['Software Engineer', 'SE', 0],
#         ['Data Scientist', 'DS', 0]
#     ]

#     with app.app_context():
#         result_data = getAllJobRole([ 
#             Job_Role(test_data[0][0], test_data[0][1], test_data[0][2]),
#             Job_Role(test_data[1][0], test_data[1][1], test_data[1][2]),
#             Job_Role(test_data[2][0], test_data[2][1], test_data[2][2])
#         ])

#         assert result_data.json['code'] == 200
#         assert len(result_data.json['data']) == 3
#         for i in range(len(test_data)):
#             assert result_data.json['data'][i]['job_role_name'] == test_data[i][0]
#             assert result_data.json['data'][i]['job_role_desc'] == test_data[i][1]
#             assert result_data.json['data'][i]['job_role_status'] == test_data[i][2]

# #----------------------test function getAllCourses----------------------
# def test_getAllCourses_success():
#     """
#     GIVEN a function getAllCourses
#     WHEN get all courses
#     THEN check the courses are retrieved successfully
#     """
#     test_data = [
#         ['COR5001', 'Introduction to Python', 'Python is a programming language', '0', 'Online', 'Programming'],
#         ['COR5002', 'Introduction to Java', 'Java is a programming language', '0', 'Online', 'Programming'],
#         ['COR5003', 'Introduction to C++', 'C++ is a programming language', '0', 'Online', 'Programming']
#     ]

#     app = Flask(__name__)

#     with app.app_context():
#         result_data = getAllCourses([ 
#             Course(test_data[0][0], test_data[0][1], test_data[0][2], test_data[0][3], test_data[0][4], test_data[0][5]),
#             Course(test_data[1][0], test_data[1][1], test_data[1][2], test_data[1][3], test_data[1][4], test_data[1][5]),
#             Course(test_data[2][0], test_data[2][1], test_data[2][2], test_data[2][3], test_data[2][4], test_data[2][5])
#         ])

#         assert result_data.json['code'] == 200
#         assert len(result_data.json['data']) == 3
#         for i in range(len(test_data)):
#             assert result_data.json['data'][i]['course_id'] == test_data[i][0]
#             assert result_data.json['data'][i]['course_name'] == test_data[i][1]
#             assert result_data.json['data'][i]['course_desc'] == test_data[i][2]
#             assert result_data.json['data'][i]['course_status'] == test_data[i][3]
#             assert result_data.json['data'][i]['course_type'] == test_data[i][4]
#             assert result_data.json['data'][i]['course_category'] == test_data[i][5]
    
# #----------------------test function updateRole----------------------
# def test_update_role_success():
#     """
#     GIVEN a Role model
#     WHEN a new Role is updated
#     THEN check the new job_role_name, job_role_desc, job_role_status are defined correctly
#     """
#     app = Flask(__name__)
    
#     test_data_jobrole2 = Job_Role('Human Resource', 'HR', 0)
#     test_data_jobrole2.job_role_id = 2

#     new_data = {
#         'job_role_name' : 'Software Developer',
#         'job_role_desc' : 'SD',
#     }

#     existing_data= [Job_Role('Teacher', 'TR', 0),Job_Role('Developer', 'Dev', 0)]
#     with app.app_context():
#         result_data = updateRole(2, test_data_jobrole2, new_data, existing_data)
#         assert result_data.status_code == 200
#         assert result_data.get_json()['data']['job_role_name'] == 'Software Developer'
#         assert result_data.get_json()['data']['job_role_desc'] == 'SD'

# #----------- test function deleteRole ------------------
# def test_delete_role_success():
#     """
#     GIVEN a Role model
#     WHEN a new Role is deleted
#     THEN check the job_role_id is deleted correctly
#     """
#     app = Flask(__name__)
#     test_data_jobrole1 = Job_Role('Human Resource', 'HR', 0)
#     test_data_jobrole1.job_role_id = 1
#     test_data_jobrole2 = Job_Role('Software Developer', 'SD', 0)
#     test_data_jobrole2.job_role_id = 2
#     test_data_jobrole3 = Job_Role('Teacher', 'TR', 0)
#     test_data_jobrole3.job_role_id = 3

#     existing_data= [test_data_jobrole1, test_data_jobrole2, test_data_jobrole3]
#     with app.app_context():
#         result_data = deleteRole(2, test_data_jobrole2, existing_data)
#         assert result_data.get_json()['code'] == 200
#         assert result_data.get_json()['message'] == 'Job removed successfully'

# #----------------------test function createRoleMap----------------------
# def test_create_role_map_success():
#     """
#     GIVEN a function createRoleMap
#     WHEN create a new role map
#     THEN check the role map is created successfully
#     """
#     app = Flask(__name__)

#     role_map1 = Role_Map(1, 1)

#     with app.app_context():
#         result_data = createRoleMap(1,1,role_map1)
#         assert result_data.json['code'] == 201
#         assert result_data.json['message'] == "Success"
#         assert result_data.json['data']['rm_fk_job_role_id'] == 1
#         assert result_data.json['data']['rm_fk_skill_id'] == 1

# #----------------------check function getSkillsForJob----------------------
# def test_get_skills_for_job_success():
#     """
#     GIVEN a function getSkillsForJob
#     WHEN a new role_map is created
#     THEN check the function is returning the correct data
#     """
#     app = Flask(__name__)

#     test_data_role_map = [
#         Role_Map(1, 1),
#         Role_Map(1, 2),
#         Role_Map(1, 3),
#         Role_Map(2, 2),
#         Role_Map(2, 3),
#     ]

#     test_data_skill1 = Skill('skill1', 'desc1', 0)
#     test_data_skill1.skill_id = 1
#     test_data_skill2 = Skill('skill2', 'desc2', 0)
#     test_data_skill2.skill_id = 2
#     test_data_skill3 = Skill('skill3', 'desc3', 0)
#     test_data_skill3.skill_id = 3

#     test_data_skill = [
#         test_data_skill1,
#         test_data_skill2,
#         test_data_skill3
#     ]

#     test_data_job_role1 = Job_Role('job1', 'jobdesc1', 0)
#     test_data_job_role1.job_role_id = 1
#     test_data_job_role2 = Job_Role('job2', 'jobdesc2', 0)
#     test_data_job_role2.job_role_id = 2
#     test_data_job_role = [
#         test_data_job_role1,
#         test_data_job_role2
#     ]

#     with app.app_context():
#         result_data = getSkillsForJob(1, test_data_role_map, test_data_skill, test_data_job_role)
#         assert result_data.status_code == 200
#         assert result_data.json == [{
#             "code": 200,
#             "data": [
#                 ['skill1', 'desc1',1],
#                 ['skill2', 'desc2',2],
#                 ['skill3', 'desc3',3]
#             ]
#         }, 200]

# #----------------------test function del_role----------------------
# def test_del_role_success():
#     """
#     GIVEN a function del_role
#     WHEN delete a role
#     THEN check the role is deleted successfully
#     """
#     app = Flask(__name__)

#     test_data_role_map = [
#         Role_Map(1, 1),
#         Role_Map(1, 2),
#         Role_Map(1, 3),
#         Role_Map(2, 2),
#         Role_Map(2, 3),
#     ]

#     with app.app_context():
#         result_data = del_role(1, 1, Role_Map(1, 1), test_data_role_map)
#         assert result_data.status_code == 200
#         assert result_data.json['code'] == 200
#         assert result_data.json['message'] == 'Skill removed successfully'

# #----------------------test function getCoursesForSkill----------------------
# def test_get_courses_for_skill_success():
#     """
#     GIVEN a function getCoursesForSkill
#     WHEN a new course_skill is created
#     THEN check the function is returning the correct data
#     """
#     app = Flask(__name__)

#     test_data_course_skill = [
#         Course_Map('1', 1),
#         Course_Map('1', 2),
#         Course_Map('1', 3),
#         Course_Map('2', 2),
#         Course_Map('2', 3),
#     ]

    
#     test_data_course = [
#         Course('1', 'Human Resource', 'HR', '0', '1', '1'),
#         Course('2', 'Software Developer', 'SD', '0', '1', '1'),
#         Course('3', 'Teacher', 'TR', '0', '1', '1')
#     ]

#     test_data_skill1 = Skill('skill1', 'desc1', 0)
#     test_data_skill1.skill_id = 1
#     test_data_skill2 = Skill('skill2', 'desc2', 0)
#     test_data_skill2.skill_id = 2
#     test_data_skill3 = Skill('skill3', 'desc3', 0)
#     test_data_skill3.skill_id = 3

#     test_data_skill = [
#         test_data_skill1,
#         test_data_skill2,
#         test_data_skill3
#     ]

#     with app.app_context():
#         result_data = getCoursesForSkill(3, test_data_course_skill, test_data_course, test_data_skill)
#         assert result_data.status_code == 200
#         assert result_data.json[0]['code'] == 200
#         assert len(result_data.json[0]['data']) == 2

# #----------------------test function getSkillID--------------------
# def test_get_skill_id_success():
#     """
#     GIVEN a function getSkillID
#     WHEN get a skill id
#     THEN check the function is returning the correct data
#     """
#     app = Flask(__name__)

#     test_data_skill1 = Skill('skill1', 'desc1', 0)
#     test_data_skill1.skill_id = 1
#     test_data_skill2 = Skill('skill2', 'desc2', 0)
#     test_data_skill2.skill_id = 2
#     test_data_skill3 = Skill('skill3', 'desc3', 0)
#     test_data_skill3.skill_id = 3

#     test_data_skill = [
#         test_data_skill1,
#         test_data_skill2,
#         test_data_skill3
#     ]

#     with app.app_context():
#         result_data = getSkillID('skill2', test_data_skill)
#         assert result_data.json['code'] == 200
#         assert result_data.json['message']['skill_desc'] == 'desc2'
#         assert result_data.json['message']['skill_name'] == 'skill2'
#         assert result_data.json['message']['skill_id'] == 2
#         assert result_data.json['message']['skill_status'] == 0

# #----------------------test function getSkillById--------------------
# def test_get_skill_by_id_success():
#     """
#     GIVEN a function getSkillById
#     WHEN get a skill by id
#     THEN check the function is returning the correct data
#     """
#     app = Flask(__name__)

#     test_data_skill1 = Skill('skill1', 'desc1', 0)
#     test_data_skill1.skill_id = 1
#     test_data_skill2 = Skill('skill2', 'desc2', 0)
#     test_data_skill2.skill_id = 2
#     test_data_skill3 = Skill('skill3', 'desc3', 0)
#     test_data_skill3.skill_id = 3

#     test_data_skill = [
#         test_data_skill1,
#         test_data_skill2,
#         test_data_skill3
#     ]

#     with app.app_context():
#         result_data = getSkillById(2, test_data_skill)
#         assert result_data.json['code'] == 200
#         assert result_data.json['message']['skill_desc'] == 'desc2'
#         assert result_data.json['message']['skill_name'] == 'skill2'
#         assert result_data.json['message']['skill_id'] == 2
#         assert result_data.json['message']['skill_status'] == 0

# #-------------------------test function getskills-----------------------------------
# def test_get_skills_success():
#     """
#     GIVEN a getskills function
#     WHEN getskills is called
#     THEN check the response code is 200 and the data is returned as per expected
#     """
#     app = Flask(__name__)
#     test_data = test_data = [
#         ['Human Resource', 'HR', 0],
#         ['Software Engineer', 'SE', 0],
#         ['Data Scientist', 'DS', 0]
#     ]

#     with app.app_context():
#         result_data = getskills([
#             Skill(test_data[0][0], test_data[0][1], test_data[0][2]),
#             Skill(test_data[1][0], test_data[1][1], test_data[1][2]),
#             Skill(test_data[2][0], test_data[2][1], test_data[2][2])
#         ])
#         assert result_data.json['code'] == 200
#         assert len(result_data.json['data']) == 3
#         for i in range(len(test_data)):
#                 assert result_data.json['data'][i]['skill_name'] == test_data[i][0]
#                 assert result_data.json['data'][i]['skill_desc'] == test_data[i][1]
#                 assert result_data.json['data'][i]['skill_status'] == test_data[i][2]

# #-------------------------test function createSkills-----------------------------------
# def test_create_skills():
#     """
#     GIVEN a Skill model
#     WHEN a new Skill is created
#     THEN check the skill_status, skill_name, skill_desc are defined correctly
#     """
#     app = Flask(__name__)

#     test_data = {
#         "skill_name": "Python",
#         "skill_desc": "Python is a programming language",
#         "skill_status": 0
#     }

#     with app.app_context():
#         result_data = createSkills(test_data)
#         assert result_data.json['code'] == 200
#         assert result_data.json['data']['skill_status'] == 0
#         assert result_data.json['data']['skill_name'] == "Python"
#         assert result_data.json['data']['skill_desc'] == "Python is a programming language"

# #-------------------------test function updateSkill-----------------------------------
# def test_update_skill_success():
#     """
#     GIVEN a Skill model
#     WHEN a new Skill is updated
#     THEN check the new skill_name, skill_desc, skill_status are defined correctly
#     """
#     app = Flask(__name__)
    
#     test_data_skill2 = Skill(skill_name="Java", skill_desc="Java is a programming language", skill_status=1)
#     test_data_skill2.skill_id = 2

#     new_data = {
#         'skill_name' : 'Python',
#         'skill_desc' : 'Python is a programming language',
#     }

#     test_data_existing=[Skill(skill_name="C sharp", skill_desc="C sharp is a programming language", skill_status=1),Skill(skill_name="Android Studio", skill_desc="This is an IDE", skill_status=1)]



#     with app.app_context():
#         result_data = updateSkill(2, test_data_skill2, new_data,test_data_existing)
#         assert result_data.status_code == 200
#         assert result_data.get_json()['data']['skill_name'] == 'Python'
#         assert result_data.get_json()['data']['skill_desc'] == 'Python is a programming language'

# #-------------------------test function deleteSkill-----------------------------------
# def test_delete_skill_success():
#     """
#     GIVEN a Skill model
#     WHEN a new Skill is deleted
#     THEN check the skill_status is changed to 1
#     """
#     app = Flask(__name__)
#     test_data_skill1 = Skill(skill_name="Java", skill_desc="Java is a programming language", skill_status=1)
#     test_data_skill1.skill_id = 1
#     test_data_skill2 = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
#     test_data_skill2.skill_id = 2
#     test_data_skill3 = Skill(skill_name="C sharp", skill_desc="C sharp is a programming language", skill_status=1)
#     test_data_skill3.skill_id = 3

#     test_data_existing=[
#         test_data_skill1,
#         test_data_skill2,
#         test_data_skill3
#     ]

#     with app.app_context():
#         result_data = deleteSkill(2,test_data_existing)
#         assert result_data.status_code == 200
#         assert result_data.get_json()['code'] == 200
#         assert result_data.get_json()['message'] == 'Skill removed successfully'

# #-------------------------test function createJourney-----------------------------------
# def test_create_journey_success():
#     """
#     GIVEN a Journey model
#     WHEN a new Journey is created
#     THEN check the journey_status, journey_name, j_fk_staff_id, j_fk_job_role_id are defined correctly
#     """
#     app = Flask(__name__)

#     test_data = {
#         "journey_name": "Python",
#         "journey_desc": "Python is a programming language",
#         "journey_status": 0
#     }

#     with app.app_context():
#         result_data = createJourney(test_data)
#         assert result_data.json['code'] == 200

# #-------------------------test function createJourneyMap-----------------------------------
# def test_create_journey_map_success():
#     """
#     GIVEN a Journey_Map model
#     WHEN a new Journey_Map is created
#     THEN check the jm_fk_journey_id and jm_fk_course_id are defined correctly
#     """
#     app = Flask(__name__)

#     journey_map = Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")


#     with app.app_context():
#         result_data = createJourneyMap(None,None,journey_map)
#         assert result_data.json['code'] == 201
#         assert result_data.json['data']['jm_fk_journey_id'] == 1
#         assert result_data.json['data']['jm_fk_course_id'] == "1"
#         assert result_data.json['message'] == 'Success'

# #-------------------------test function createSkillMap-----------------------------------
# def test_create_skill_map_success():
#     """
#     GIVEN a Course_Map model
#     WHEN a new Course_Map is created
#     THEN check the cm_fk_course_id and cm_fk_skill_id are defined correctly
#     """
#     app = Flask(__name__)

#     course_map = Course_Map(cm_fk_course_id='1', cm_fk_skill_id=1)

#     with app.app_context():
#         result_data = createSkillMap(None,None,course_map)
#         assert result_data.json['code'] == 201
#         assert result_data.json['data']['cm_fk_course_id'] == '1'
#         assert result_data.json['data']['cm_fk_skill_id'] == 1
#         assert result_data.json['message'] == 'Success'

# #-------------------------test function getSkillsForCourse-----------------------------------
# def test_get_skills_for_course_success():
#     """
#     GIVEN a Course_Map model
#     WHEN a new Course_Map is created
#     THEN check the cm_fk_course_id and cm_fk_skill_id are defined correctly
#     """
#     app = Flask(__name__)

#     course_map = [
#         Course_Map(cm_fk_course_id='1', cm_fk_skill_id=1),
#         Course_Map(cm_fk_course_id='1', cm_fk_skill_id=2),
#         Course_Map(cm_fk_course_id='1', cm_fk_skill_id=3)
#     ]
#     skill1 = Skill(skill_name="Java", skill_desc="Java is a programming language", skill_status=1)
#     skill1.skill_id = 1
#     skill2 = Skill(skill_name="Python", skill_desc="Python is a programming language", skill_status=1)
#     skill2.skill_id = 2
#     skill3 = Skill(skill_name="C sharp", skill_desc="C sharp is a programming language", skill_status=1)
#     skill3.skill_id = 3
#     skills = [
#         skill1,
#         skill2,
#         skill3
#     ]
#     with app.app_context():
#         result_data = getSkillsForCourse('1',course_map, skills)
#         assert result_data.json[0]['code'] == 200

# #-------------------------test function deleteJourneyMap-----------------------------------
# def test_delete_journey_map_success():
#     """
#     GIVEN a Journey_Map model
#     WHEN a new Journey_Map is deleted
#     THEN check the journey_status is changed to 1
#     """
#     app = Flask(__name__)
#     test_data_journey_map1 = Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")
#     test_data_journey_map1.jm_id = 1
#     test_data_journey_map2 = Journey_Map(jm_fk_journey_id=2, jm_fk_course_id="2")
#     test_data_journey_map2.jm_id = 2
#     test_data_journey_map3 = Journey_Map(jm_fk_journey_id=3, jm_fk_course_id="3")
#     test_data_journey_map3.jm_id = 3

#     test_data_existing=[
#         test_data_journey_map1,
#         test_data_journey_map2,
#         test_data_journey_map3
#     ]

#     with app.app_context():
#         result_data = deleteJourneyMap(1, "1", test_data_existing)
#         assert result_data.status_code == 200
#         assert result_data.get_json()['code'] == 200
#         assert result_data.get_json()['message'] == 'Journey Map removed successfully'

