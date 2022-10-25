from flask import  request, jsonify
from db_connector import db
from Courses import Course
from Skills import Skill

# Course Map Table
class Course_Map(db.Model):
    __tablename__ = 'Course_Map'
    __table_args__ = {'extend_existing': True}
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
def create_course_skill_map(cm_fk_course_id, cm_fk_skill_id):
    data = request.get_json()
    new_map = Course_Map(data['cm_fk_course_id'], data['cm_fk_skill_id'])
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

# ********************************* Retrieve ********************************* 
# Get all skills for courses
def get_skills_for_course(cm_fk_course_id):
    # Get a list of skill for the course
    coursemapping = Course_Map.query.filter_by(
        cm_fk_course_id=cm_fk_course_id).all()
    if coursemapping:
        role = [r.json() for r in coursemapping]
        list_of_skill = []
        for i in (role):
            list_of_skill.append(i['cm_fk_skill_id'])
        skillName = []
        # For each skill_id, find the name of skill
        skill = Skill.query.all()
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
def get_courses_for_skill(skill_id):
    # Get a list of courses related to this job
    coursemapping = Course_Map.query.filter_by(
        cm_fk_skill_id=skill_id).all()
    if coursemapping:
        c = [c.json() for c in coursemapping]
        list_of_course = []
        for i in (c):
            list_of_course.append(i['cm_fk_course_id'])
        skillName = []

        # For each course_id, find the name of course
        course = Course.query.all()
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
    course = Course_Map.query.filter_by(
        cm_fk_course_id=course_id, cm_fk_skill_id=skill_id).first()

    try:
        db.session.delete(course)
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "message": "Course removed successfully"
            }
        )
    except Exception as e:
        print(e)
        return jsonify(
            {
                "code": 404,
                "message": "Course and Skill not found."
            }
        ), 404








