from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)
CORS(app)

class Institution(db.Model):

    __tablename__ = 'institution'

    institutionID = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    tittle = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Student(db.Model):

    __tablename__ = 'student'

    studentID = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    lastName = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(12), nullable=False)
    institution = db.Column(db.Integer, db.ForeignKey(Institution.id))

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

class Subject(db.Model):

    __tablename__ = 'subject'

    subjectID = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    marks = db.Column(db.Integer, nullable=False)
    tittle = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

@app.route("/student")
def student():
    student_list = Student.query.all()
    return jsonify(
        {
            "data": [student.to_dict()
                     for student in student_list]
        }
    ), 200

@app.route("/student/<int:studentID>")
def student_by_id(studentID):
    student = Student.query.filter_by(studentID=studentID).first()
    if student:
        return jsonify({
            "data": student.to_dict()
        }), 200
    else:
        return jsonify({
            "message": "Student not found."
        }), 404

@app.route("/institution")
def institution():
    institution_list = Institution.query.all()
    return jsonify(
        {
            "data": [institution.to_dict()
                     for institution in institution_list]
        }
    ), 200

@app.route("/institution/<int:id>")
def institution_by_id(id):
    institution = Institution.query.filter_by(id=id).first()
    if institution:
        return jsonify({
            "data": institution.to_dict() 
        }), 200
    else:
        return jsonify({
            "message": "No institution with that id."
        }), 404

@app.route("/subject")
def subject():
    subject_list = Subject.query.all()
    return jsonify(
        {
            "data": [subject.to_dict()
                     for subject in subject_list]
        }
    ), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)