from flask import  request, jsonify
import db_connector
db = db_connector.db_connector()
from Courses import Course
from Skills import Skill

# Course Map Table
class Course_Map(db.Model):
    __tablename__ = 'Course_Map'
    cm_fk_course_id = db.Column(
        db.String(20), primary_key=True, nullable=False)
    cm_fk_skill_id = db.Column(db.Integer, primary_key=True, nullable=False)

    def __init__(self, cm_fk_course_id, cm_fk_skill_id):
        if not isinstance(cm_fk_course_id, str):
            raise TypeError("cm_fk_course_id must be a String")
        if not isinstance(cm_fk_skill_id, int):
            raise TypeError("cm_fk_skill_id must be a integer")
        self.cm_fk_course_id = cm_fk_course_id
        self.cm_fk_skill_id = cm_fk_skill_id

    def json(self):
        return {
            "cm_fk_course_id": self.cm_fk_course_id,
            "cm_fk_skill_id": self.cm_fk_skill_id
        }

#Functions (CRUD)
# ********************************* Create ********************************* 
# Add a course skill map
def create_course_skill_map(cm_fk_course_id, cm_fk_skill_id, test_data=""):
    if test_data == "":
        data = request.get_json()
        new_map = Course_Map(data['cm_fk_course_id'], data['cm_fk_skill_id'])
    else:
        new_map = test_data

    if test_data == "":
        try:
            db.session.add(new_map)
            db.session.commit()
        except Exception as e:
            print(e)
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred creating the record."
                }
            ), 500

        return jsonify(
            {
                "code": 201,
                "data": new_map.json(),
                "message": "Success"
            }
        ), 201
    else:
        return jsonify(
            {
                "code": 201,
                "data": new_map.json(),
                "message": "Success"
            }
        )

# ********************************* Retrieve ********************************* 
# Get all skills for courses
def get_skills_for_course(cm_fk_course_id, test_data_course_map="", test_data_skill=""):
    # Get a list of skill for the course
    coursemapping = None
    if test_data_course_map == "" and test_data_skill == "":
        coursemapping = Course_Map.query.filter_by(
            cm_fk_course_id=cm_fk_course_id).all()
        db.session.remove()
    else:
        coursemapping = test_data_course_map
    if coursemapping:
        role = [r.json() for r in coursemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['cm_fk_skill_id'])
        skillName = []
        # For each skill_id, find the name of skill
        skill = None
        if test_data_skill == "":
            skill = Skill.query.all()
            db.session.remove()
        else:
            skill = test_data_skill
        if skill:
            skill_list = [s.json() for s in skill]

            for i in skill_list:
                if i['skill_id'] in list_of_skill:
                    skillName.append(
                        [i['skill_name'], i['skill_desc'], i['skill_id']])
            return jsonify(
                {
                    "code": 200,
                    "data": skillName
                }, 200

            )
    else:
        return jsonify(
            {
                "code": 404,
                "data": "No records found"
            }, 404)

    return jsonify(
        {
            "code": 404,
            "message": "No records found."
        }
    ), 404

# Get all courses for skills
def get_courses_for_skill(skill_id, test_data_course_map="", test_data_course="", test_data_skill=""):
    # Get a list of courses related to this job
    coursemapping = None
    if test_data_course_map == "" and test_data_course == "" and test_data_skill == "":
        coursemapping = Course_Map.query.filter_by(
            cm_fk_skill_id=skill_id).all()
        db.session.remove()
    else:
        coursemapping = test_data_course_map
    if coursemapping:
        c = [c.json() for c in coursemapping]
        list_of_course = []
        for i in (c):
            list_of_course.append(i['cm_fk_course_id'])
        skillName = []

        # For each course_id, find the name of course
        course = None
        if test_data_course == "":
            course = Course.query.all()
            db.session.remove()
        else:
            course = test_data_course
        if course:
            course_list = [course.json() for course in course]
            for i in course_list:
                if i['course_id'] in list_of_course:
                    # skillName.append([i['skill_name'], i['skill_desc']])
                    skillName.append(i)
            return jsonify(
                {
                    "code": 200,
                    "data": skillName
                }, 200

            )

    return jsonify(
        {
            "code": 404,
            "data": "No records found."
        }, 404
    )


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 
# Delete a course skill map
def delete_skill_from_course(course_id, skill_id, test_data="", existing_data=""):
    all_courses = None
    course = None
    if test_data == "":
        course = Course_Map.query.filter_by(
            cm_fk_course_id=course_id, cm_fk_skill_id=skill_id).first()
    else:
        course = test_data
        all_courses = existing_data
    if course and test_data == "":
        db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": "Course removed successfully"
            }
        )
    elif role and test_data != "":
        for role in all_courses:
            if course.cm_fk_course_id == course_id and course.cm_fk_skill_id == skill_id:
                all_courses.remove(course)
                return jsonify(
                    {
                        "code": 200,
                        "message": "Course removed successfully"
                    }
                )
    return jsonify(
        {
            "code": 404,
            "message": "Course and Skill not found."
        }
    ), 404








