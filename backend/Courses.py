from flask import  request, jsonify
from db_connector import db

# Course  Table
class Course(db.Model):
    __tablename__ = 'Courses'
    course_id = db.Column(db.String(20), primary_key=True, nullable=False)
    course_name = db.Column(db.String(50), nullable=False)
    course_desc = db.Column(db.String(255), nullable=False)
    course_status = db.Column(db.String(15), nullable=False)
    course_type = db.Column(db.String(10), nullable=False)
    course_category = db.Column(db.String(50), nullable=False)

    def __init__(self, course_id, course_name, course_desc, course_status, course_type, course_category):
        if not isinstance(course_id, str):
            raise TypeError("course_id must be a String")
        if not isinstance(course_name, str):
            raise TypeError("course_name must be a String")
        if not isinstance(course_desc, str):
            raise TypeError("course_desc must be a String")
        if not isinstance(course_status, str):
            raise TypeError("course_status must be a String")
        if not isinstance(course_type, str):
            raise TypeError("course_type must be a String")
        if not isinstance(course_category, str):
            raise TypeError("course_category must be a String")
        self.course_id = course_id
        self.course_name = course_name
        self.course_desc = course_desc
        self.course_status = course_status
        self.course_type = course_type
        self.course_category = course_category

    def json(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "course_desc": self.course_desc,
            "course_status": self.course_status,
            "course_type": self.course_type,
            "course_category": self.course_category
        }


#Functions (CRUD)
# ********************************* Create ********************************* 


# ********************************* Retrieve ********************************* 
# Get all courses
def get_all_courses(test_data=""):
    courses = None
    if test_data == "":
        courses = Course.query.all()
        db.session.remove()
        return jsonify(
            {
                "code": 200,
                "data":
                [course.json() for course in courses]
            }
        )
    if test_data != "":
        return jsonify(
            {
                "code": 200,
                "data":
                    [course.json() for course in test_data]
            }
        )
    elif courses != None:
        return jsonify(
            {
                "code": 200,
                "data":
                    [course.json() for course in courses]
            }
        )


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 
