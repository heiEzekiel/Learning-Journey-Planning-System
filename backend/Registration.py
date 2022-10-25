from flask import  request, jsonify
import db_connector
db = db_connector.db_connector()

# Registration Table
class Registration(db.Model):
    #Andy test case
    __tablename__ = 'Registration'
    reg_id = db.Column(db.Integer, primary_key=True, nullable=False)
    course_id = db.Column(db.String(20), nullable=False)
    staff_id = db.Column(db.Integer, nullable=False)
    reg_status = db.Column(db.String(20), nullable=False)
    completion_status = db.Column(db.String(20), nullable=False)

    def __init__(self, course_id, staff_id, reg_status,completion_status):
        if not isinstance (course_id, str):
            raise TypeError('course_id must be a string')
        if not isinstance (staff_id, int):
            raise TypeError('staff_id must be an integer')
        if not isinstance (reg_status, str):
            raise TypeError('reg_status must be a string')
        if not isinstance (completion_status, str):
            raise TypeError('completion_status must be a string')
        self.course_id = course_id
        self.staff_id = staff_id
        self.reg_status = reg_status
        self.completion_status = completion_status

    def json(self):
        return {
            "course_id": self.course_id,
            "staff_id": self.staff_id,
            "reg_status": self.reg_status,
            "completion_status": self.completion_status
        }


#Functions (CRUD)
# ********************************* Create ********************************* 


# ********************************* Retrieve ********************************* 
# Get Courses Registered by Staff
def get_courses_registration(staff_id):
    cs_reg = Registration.query.filter_by(staff_id=staff_id).all()
    db.session.remove()
    if cs_reg:
        return jsonify(
            {
                "code": 200,
                "data": [jn.json() for jn in cs_reg]
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no records found."
            }
        )


# ********************************* Update ********************************* 


# ********************************* Delete ********************************* 

