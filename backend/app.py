# Function Files
import Job_Role as jr
import Role_Map as rm
import Courses as c
import Course_Map as cm
import Registration as r
import Skills as s
import Skill_Map as sm
import Journey as j
import Journey_Map as jm

from db_connector import app, db

# ================================================================== Routes ==================================================================
@app.route("/")
def home():
    pass

# ********************************* Job Role Related ******************************************************************
# This segment of code is to do creation of roles. Only used by HR/admin.
# Create Job Role
@app.route("/createJobRole", methods=['POST'])
def create_job_role():
    return jr.create_job_role()

# This segment of code is to do retrieval of all the existing roles. Used by both HR and Learner.
# Get All Job Role
@app.route("/getAllJobRole", methods=['GET'])
def get_all_job_role():
    return jr.get_all_job_role()

# This segment of code is to get a specific job role. Used by both HR and Learner.
# Get Job Role details by job_role_id
@app.route("/getSpecificJobRole/<int:job_role_id>", methods=['GET'])
def get_specific_job_role_by_id(job_role_id):
    return jr.get_specific_job_role_by_id(job_role_id)

# This segment of code is to do update of roles. Only used by HR/admin.
# Update All Job Role
@app.route("/updateJobRole/<int:job_role_id>", methods=['PUT'])
def update_job_role_by_id(job_role_id):
    return jr.update_job_role_by_id(job_role_id)

# This segment of code is delete a selected role
# Delete Role details by job_role_id
@app.route("/deleteRole/<int:job_role_id>", methods=['DELETE'])
def delete_job_role_by_id(job_role_id):
    return jr.delete_job_role_by_id(job_role_id)


# ********************************* Role Map Related ******************************************************************
# Create job to role mapping
# Used when updating role information, or mapping role information. Used in assign skill to role and update.
@app.route("/createRoleMap/<int:rm_fk_job_role_id>/<int:rm_fk_skill_id>", methods=['POST'])
def create_role_map(rm_fk_job_role_id, rm_fk_skill_id):
    return rm.create_role_map(rm_fk_job_role_id, rm_fk_skill_id)

# Get skills required for the selected job role using job_role_id
@app.route("/getSkillsForJob/<int:job_role_id>", methods=['GET'])
def get_skills_for_job(job_role_id):
    return rm.get_skills_for_job(job_role_id)

# Remove a skill from a job role
@app.route("/removeSkillFromJobRole/<int:job_role_id>/<int:skill_id>", methods=['DELETE'])
def delete_skill_from_job_role(job_role_id, skill_id):
    return rm.delete_skill_from_job_role(job_role_id, skill_id)


# ********************************* Courses Related ******************************************************************
# Get all courses
@app.route("/getAllCourses", methods=['GET'])
def get_all_courses(test_data=""):
    return c.get_all_courses(test_data)


# ********************************* Course Map Related ******************************************************************
# Create course to skill mapping
# Used when updating course information, or mapping course information to skill. Used in assign skill to course
@app.route("/createSkillMap/<string:cm_fk_course_id>/<int:cm_fk_skill_id>", methods=['POST'])
def create_course_skill_map(cm_fk_course_id, cm_fk_skill_id, test_data=""):
    return cm.create_course_skill_map(cm_fk_course_id, cm_fk_skill_id, test_data)

# Get skills required for the course using course id
@app.route("/getSkillsForCourse/<string:cm_fk_course_id>", methods=['GET'])
def get_skills_for_course(cm_fk_course_id, test_data_course_map="", test_data_skill=""):
    return cm.get_skills_for_course(cm_fk_course_id, test_data_course_map, test_data_skill)

# Get courses available for the selected skill using skill_id
@app.route("/getCoursesForSkill/<int:skill_id>", methods=['GET'])
def get_courses_for_skill(skill_id, test_data_course_map="", test_data_course="", test_data_skill=""):
    return cm.get_courses_for_skill(skill_id, test_data_course_map, test_data_course, test_data_skill)

# Remove a skill from a course
@app.route("/removeSkillFromCourse/<string:course_id>/<int:skill_id>", methods=['DELETE'])
def delete_skill_from_course(course_id, skill_id, test_data="", existing_data=""):
    return cm.delete_skill_from_course(course_id, skill_id, test_data, existing_data)


# ********************************* Registration Related ******************************************************************
#Get courses of each staff
#Andy add test case
@app.route("/getCourseReg/<int:staff_id>", methods=['GET'])
def get_courses_registration(staff_id):
    return r.get_courses_registration(staff_id)


# ********************************* Skills Related ******************************************************************
# This segment of code is to create skill
# Create skill
@app.route("/createSkills", methods=['POST'])
def create_skills():
    return s.create_skills()

# Get a list of skills
@app.route("/getskills" , methods=['GET'])
def get_skills():
    return s.get_skills()

# Get skill ID using skill name
@app.route("/getSkillID/<string:skill_name>", methods=['GET'])
def get_skill_id(skill_name):
    return s.get_skill_id(skill_name)

# Get skill ID using skill id
@app.route("/getSkillById/<int:skill_id>", methods=['GET'])
def get_skill_by_id(skill_id):
    return s.get_skill_by_id(skill_id)

# This segment of code is update details of a selected skill
# Update Skill details by skill_id
@app.route("/updateSkill/<int:skill_id>", methods=['PUT'])
def update_skill(skill_id):
    return s.update_skill(skill_id)

# This segment of code is delete a selected skill
# Delete Skill details by skill_id
@app.route("/deleteSkill/<int:skill_id>", methods=['DELETE'])
def delete_skill(skill_id):
    return s.delete_skill(skill_id)


# ********************************* Skill Map Related ******************************************************************
#Get skills of each staff
#Andy add test case
@app.route("/getSkillStaff/<int:sm_fk_staff_id>", methods=['GET'])
def get_staff_skills(sm_fk_staff_id):
    return sm.get_staff_skills(sm_fk_staff_id)


# ********************************* Journey Related ******************************************************************
# Create Learning Journey
@app.route("/createJourney", methods=['POST'])
def create_journey(test_data=""):
    return j.create_journey(test_data)

# Retrieve Learning Journey
# Andy add test case
@app.route("/getJourney/<int:j_fk_staff_id>", methods=['GET'])
def get_journey(j_fk_staff_id):
    return j.get_journey(j_fk_staff_id)

# Delete Learning Journey
@app.route("/deleteJourney/<int:journey_id>", methods=['DELETE'])
def delete_journey(journey_id, test_data=""):
    return j.delete_journey(journey_id, test_data)


# ********************************* Journey Map Related ******************************************************************
# Create Journey Map
@app.route("/createJourneyMap/<int:jm_fk_journey_id>/<string:jm_fk_course_id>", methods=['POST'])
def create_journey_map(jm_fk_journey_id, jm_fk_course_id, test_data=""):
    return jm.create_journey_map(jm_fk_journey_id, jm_fk_course_id, test_data)

# Get a list of journey maps
@app.route("/getJourneyMaps", methods=['GET'])
def get_journey_maps(test_data=""):
    return jm.get_journey_maps(test_data)

# delete a journey map
@app.route("/deleteJourneyMap/<int:jm_fk_journey_id>/<string:jm_fk_course_id>", methods=['DELETE'])
def delete_journey_map(jm_fk_journey_id,jm_fk_course_id, test_data=""):
    return jm.delete_journey_map(jm_fk_journey_id,jm_fk_course_id, test_data)


#  ********************************* Flask ******************************************************************
# Run flask app
if __name__ == "__main__":
    app.run(debug=True)