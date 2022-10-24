import unittest
from backend.Job_Role import Job_Role 
from backend.Role_Map import Role_Map 
from backend.Course_Map import Course_Map 
from backend.Courses import Course 
from backend.Skills import Skill 
from backend.Journey import Journey 
from backend.Journey_Map import Journey_Map 
from backend.Registration import Registration 
from backend.Skill_Map import Skill_Map 

#----------- test Class Job_Role ------------------
class TestJobRole(unittest.TestCase):
    def test_job_role_success(self):
        job_role = Job_Role("Human Resource", "HR's job role", 1)
        self.assertEqual(job_role.job_role_name, "Human Resource")
        self.assertEqual(job_role.job_role_desc, "HR's job role")
        self.assertEqual(job_role.job_role_status, 1)

    def test_job_role_invalid_name(self):
        try:
            Job_Role(1, "HR's job role", 1)
        except Exception as e:
            self.assertEqual(str(e), 'job_role_name must be a string')

    def test_job_role_invalid_desc(self):
        try:
            Job_Role("Human Resource", 1, 1)
        except Exception as e:
            self.assertEqual(str(e), 'job_role_desc must be a string')
    
    def test_job_role_invalid_status(self):
        try:
            Job_Role("Human Resource", "HR's job role", "1")
        except Exception as e:
            self.assertEqual(str(e), 'job_role_status must be an integer')

# #----------------------test Class Role_map----------------------
class TestRoleMap(unittest.TestCase):
    def test_class_role_map_suceess(self):
        role_map1 = Role_Map(1, 1)
        self.assertEqual(role_map1.rm_fk_job_role_id, 1)
        self.assertEqual(role_map1.rm_fk_skill_id, 1)

    def test_class_role_map_fail(self):
        try:
            Role_Map("1", 1)
        except Exception as e:
            self.assertEqual(str(e), 'rm_fk_job_role_id must be a integer')

    def test_class_role_map_fail1(self):
        try:
            Role_Map(1, "1")
        except Exception as e:
            self.assertEqual(str(e), 'rm_fk_skill_id must be a integer')

#----------------------test Class course_map----------------------
class TestCourseMap(unittest.TestCase):
    def test_class_course_map_suceess(self):
        course_map1 = Course_Map('1', 1)
        self.assertEqual(course_map1.cm_fk_course_id, '1')
        self.assertEqual(course_map1.cm_fk_skill_id, 1)
    def test_course_map_fail(self):
        try:
            Course_Map(1, 1)
        except Exception as e:
            self.assertEqual(str(e), 'cm_fk_course_id must be a String')
    def test_course_map_fail1(self):
        try:
            Course_Map('1', "1")
        except Exception as e:
            self.assertEqual(str(e), 'cm_fk_skill_id must be a integer')

#----------------------test Class Course----------------------
class TestCourseMap(unittest.TestCase):
    def test_class_course_suceess(self):
        course1 = Course('1', 'Human Resource', 'HR', '0', '1', '1')
        self.assertEqual(course1.course_id, '1')
        self.assertEqual(course1.course_name, 'Human Resource')
        self.assertEqual(course1.course_desc, 'HR')
        self.assertEqual(course1.course_status, '0')
        self.assertEqual(course1.course_type, '1')
        self.assertEqual(course1.course_category, '1')
    def test_course_fail(self):
        try:
            Course(1, 'Human Resource', 'HR', '0', '1', '1')
        except Exception as e:
            self.assertEqual(str(e), 'course_id must be a String')
    def test_course_fail1(self):
        try:
            Course('1', 1, 'HR', '0', '1', '1')
        except Exception as e:
            self.assertEqual(str(e), 'course_name must be a String')
    def test_course_fail2(self):
        try:
            Course('1', 'Human Resource', 1, '0', '1', '1')
        except Exception as e:
            self.assertEqual(str(e), 'course_desc must be a String')
    def test_course_fail3(self):
        try:
            Course('1', 'Human Resource', 'HR', 1, '1', '1')
        except Exception as e:
            self.assertEqual(str(e), 'course_status must be a String')
    def test_course_fail4(self):
        try:
            Course('1', 'Human Resource', 'HR', '0', 1, '1')
        except Exception as e:
            self.assertEqual(str(e), 'course_type must be a String')
    def test_course_fail5(self):
        try:
            Course('1', 'Human Resource', 'HR', '0', '1', 1)
        except Exception as e:
            self.assertEqual(str(e), 'course_category must be a String')

#-------------------------test class Skill-----------------------------------
class TestSkill(unittest.TestCase):
    def test_class_skill_suceess(self):
        skill1 = Skill('Human Resource', 'HR', 1)
        self.assertEqual(skill1.skill_name, 'Human Resource')
        self.assertEqual(skill1.skill_desc, 'HR')
        self.assertEqual(skill1.skill_status, 1)
    def test_skill_fail(self):
        try:
            Skill(1, 'HR', 1)
        except Exception as e:
            self.assertEqual(str(e), 'skill_name must be a string')
    def test_skill_fail1(self):
        try:
            Skill('Human Resource', 1, 1)
        except Exception as e:
            self.assertEqual(str(e), 'skill_desc must be a string')
    def test_skill_fail2(self):
        try:
            Skill('Human Resource', 'HR', "1")
        except Exception as e:
            self.assertEqual(str(e), 'skill_status must be an integer')

#-------------------------test class Journey-----------------------------------
class TestJourney(unittest.TestCase):
    def test_class_journey_suceess(self):
        journey = Journey(journey_name = "1",journey_status="1", j_fk_staff_id=1, j_fk_job_role_id=1)
        self.assertEqual(journey.journey_name, "1")
        self.assertEqual(journey.journey_status, "1")
        self.assertEqual(journey.j_fk_staff_id, 1)
        self.assertEqual(journey.j_fk_job_role_id, 1)
    def test_journey_fail(self):
        try:
            Journey(journey_name = 1,journey_status="1", j_fk_staff_id=1, j_fk_job_role_id=1)
        except Exception as e:
            self.assertEqual(str(e), 'journey_name must be a string')
    def test_journey_fail1(self):
        try:
            Journey(journey_name = "1",journey_status=1, j_fk_staff_id=1, j_fk_job_role_id=1)
        except Exception as e:
            self.assertEqual(str(e), 'journey_status must be a string')
    def test_journey_fail2(self):
        try:
            Journey(journey_name = "1",journey_status="1", j_fk_staff_id="1", j_fk_job_role_id=1)
        except Exception as e:
            self.assertEqual(str(e), 'j_fk_staff_id must be an integer')
    def test_journey_fail3(self):
        try:
            Journey(journey_name = "1",journey_status="1", j_fk_staff_id=1, j_fk_job_role_id="1")
        except Exception as e:
            self.assertEqual(str(e), 'j_fk_job_role_id must be an integer')

#-------------------------test class Journey_Map---------------------------
class TestJourneyMap(unittest.TestCase):
    def test_class_journey_map_suceess(self):
        journey_map = Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")
        self.assertEqual(journey_map.jm_fk_journey_id, 1)
        self.assertEqual(journey_map.jm_fk_course_id, "1")
    def test_journey_map_fail(self):
        try:
            Journey_Map(jm_fk_journey_id="1", jm_fk_course_id=1)
        except Exception as e:
            self.assertEqual(str(e), 'jm_fk_journey_id must be an Integer')
    def test_journey_map_fail1(self):
        try:
            Journey_Map(jm_fk_journey_id=1, jm_fk_course_id="1")
        except Exception as e:
            self.assertEqual(str(e), 'jm_fk_course_id must be an integer')


#-------------------------test class Registration-----------------------------------
class TestRegistration(unittest.TestCase):
    def test_class_registration_suceess(self):
        registration = Registration(course_id="1", staff_id=1, reg_status="1", completion_status="1")
        self.assertEqual(registration.course_id, "1")
        self.assertEqual(registration.staff_id, 1)
        self.assertEqual(registration.reg_status, "1")
        self.assertEqual(registration.completion_status, "1")
    def test_registration_fail(self):
        try:
            Registration(course_id=1, staff_id=1, reg_status="1", completion_status="1")
        except Exception as e:
            self.assertEqual(str(e), 'course_id must be a string')
    def test_registration_fail1(self):
        try:
            Registration(course_id="1", staff_id="1", reg_status="1", completion_status="1")
        except Exception as e:
            self.assertEqual(str(e), 'staff_id must be an integer')
    def test_registration_fail2(self):
        try:
            Registration(course_id="1", staff_id=1, reg_status=1, completion_status="1")
        except Exception as e:
            self.assertEqual(str(e), 'reg_status must be a string')
    def test_registration_fail3(self):
        try:
            Registration(course_id="1", staff_id=1, reg_status="1", completion_status=1)
        except Exception as e:
            self.assertEqual(str(e), 'completion_status must be a string')

#-------------------------test class Skill_Map-----------------------------------
class TestSkillMap(unittest.TestCase):
    def test_class_skill_map_suceess(self):
        skill_map = Skill_Map(sm_fk_skill_id=1, sm_fk_staff_id=1)
        self.assertEqual(skill_map.sm_fk_skill_id, 1)
        self.assertEqual(skill_map.sm_fk_staff_id, 1)
    def test_skill_map_fail(self):
        try:
            Skill_Map(sm_fk_skill_id="1", sm_fk_staff_id=1)
        except Exception as e:
            self.assertEqual(str(e), 'sm_fk_skill_id must be a integer')
    def test_skill_map_fail1(self):
        try:
            Skill_Map(sm_fk_skill_id=1, sm_fk_staff_id="1")
        except Exception as e:
            self.assertEqual(str(e), 'sm_fk_staff_id must be a integer')