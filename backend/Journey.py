from flask import  request, jsonify
import db_connector
db = db_connector.db_connector()

# Journey Table
class Journey(db.Model):
    __tablename__ = 'Journey'
    journey_id = db.Column(db.Integer, primary_key=True, nullable=False)
    journey_name = db.Column(db.String(100), nullable=False)
    journey_status = db.Column(db.String(100), nullable=False)
    j_fk_staff_id = db.Column(db.Integer, nullable=False)
    j_fk_job_role_id = db.Column(db.Integer, nullable=False)

    def __init__(self, journey_name, journey_status, j_fk_staff_id, j_fk_job_role_id):
        if not isinstance(journey_name, str):
            raise TypeError("journey_name must be a string")
        if not isinstance(journey_status, str):
            raise TypeError("journey_status must be a string")
        if not isinstance(j_fk_staff_id, int):
            raise TypeError("j_fk_staff_id must be an integer")
        if not isinstance(j_fk_job_role_id, int):
            raise TypeError("j_fk_job_role_id must be an integer")
        self.journey_name = journey_name
        self.journey_status = journey_status
        self.j_fk_staff_id = j_fk_staff_id
        self.j_fk_job_role_id = j_fk_job_role_id

    def json(self):
        return {
            "journey_id": self.journey_id,
            "journey_name": self.journey_name,
            "journey_status": self.journey_status,
            "j_fk_staff_id": self.j_fk_staff_id,
            "j_fk_job_role_id": self.j_fk_job_role_id
        }


#Functions (CRUD)
# ********************************* Create ********************************* 
# Create a new journey
def create_journey(test_data=""):
    data = None
    if test_data == "":
        data = request.get_json()
    else:
        data = test_data
    journey_name, journey_status, j_fk_staff_id, j_fk_job_role_id = "", "", "", ""
    journey = None
    if test_data == "":
        journey = Journey.query.filter_by(
            j_fk_staff_id=data['j_fk_staff_id'], j_fk_job_role_id=data['j_fk_job_role_id']).first()
    else:
        return jsonify(
            {
                "code": 200,
                "data": test_data
            }
        )
    if journey:  # if exist
        return jsonify(
            {
                "code": 404
            }
        )

    if data['journey_name']:
        journey_name = data['journey_name']
    if data['journey_status']:
        journey_status = data['journey_status']
    if data['j_fk_staff_id']:
        j_fk_staff_id = data['j_fk_staff_id']
    if data['j_fk_job_role_id']:
        j_fk_job_role_id = data['j_fk_job_role_id']

    journey = Journey(journey_name=journey_name, journey_status=journey_status,
                      j_fk_staff_id=j_fk_staff_id, j_fk_job_role_id=j_fk_job_role_id)
    if test_data == "":
        try:
            db.session.add(journey)
            db.session.commit()
            db.session.remove()
        except Exception as e:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred updating the journey."
                }
            ), 500
        return jsonify(
            {
                "code": 211,
                "data": journey.json()
            }
        )

# ********************************* Retrieve ********************************* 
# Retrieve all journeys
def get_journey(j_fk_staff_id):
    journeys = Journey.query.filter_by(j_fk_staff_id=j_fk_staff_id).all()
    if journeys:
        return jsonify(
            {
                "code": 200,
                "data": [jn.json() for jn in journeys]
            }
        )
    else:
        return jsonify(
            {
                "code": 404,
                "message": "There are no journey found."
            }
        )

# ********************************* Update ********************************* 

# ********************************* Delete ********************************* 
# Delete a journey
def delete_journey(journey_id, test_data=""):
    del_lj = None
    if test_data == "":
        del_lj = Journey.query.filter_by(journey_id = journey_id).first()
    else:
        del_lj = test_data
    if del_lj and test_data == "":
        db.session.delete(del_lj)
        db.session.commit()
        db.session.remove()
        return jsonify(
            {
                "code": 200,
                "message" : "Journey removed successfully"
            }
        )
    elif del_lj and test_data != "":
        for i in del_lj:
            if i.journey_id == journey_id:
                del_lj.remove(i)
                break
        return jsonify(
            {
                "code": 200,
                "message" : "Journey removed successfully"
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Journey not found."
        }
    ), 404
