DROP DATABASE IF EXISTS school;
CREATE DATABASE school;
USE school;

-- CREATE TABLES --
CREATE TABLE institution (
    institutionID INT NOT NULL AUTO_INCREMENT,
    id INT NOT NULL,
    address VARCHAR(100) NOT NULL,
    tittle VARCHAR(100) NOT NULL,

    CONSTRAINT institution_pk PRIMARY KEY (institutionID)
);

CREATE TABLE student (
    studentID INT NOT NULL AUTO_INCREMENT,
    firstName VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    phoneNumber VARCHAR(12) NOT NULL,
    institution INT NOT NULL,

    CONSTRAINT student_pk PRIMARY KEY (studentID),
    CONSTRAINT student_fk FOREIGN KEY (institution) REFERENCES institution(id)
);

CREATE TABLE subject (
    subjectID INT NOT NULL AUTO_INCREMENT,
    id INT NOT NULL,
    marks INT NOT NULL,
    tittle VARCHAR(100) NOT NULL,

    CONSTRAINT subject_pk PRIMARY KEY (subjectID)
);

-- INSERT DATA --
INSERT INTO  student(firstName, lastName, phoneNumber, institution) VALUES("John", "Doe", "111-111-1111", 1000);
INSERT INTO  student(firstName, lastName, phoneNumber, institution) VALUES("Tom", "Apple", "222-222-2222", 1001);
INSERT INTO  student(firstName, lastName, phoneNumber, institution) VALUES("Harry", "Orange", "333-333-3333", 1002);

INSERT INTO  institution(id, address, tittle) VALUES(1000, "Product Engineering", "St Teresa");
INSERT INTO  institution(id, address, tittle) VALUES(1001, "Product Engineering", "XYZ College");
INSERT INTO  institution(id, address, tittle) VALUES(1002, "Product Engineering", "Standford University");


INSERT INTO subject(id, marks, tittle) VALUES(2000, 98, "Physics");
INSERT INTO subject(id, marks, tittle) VALUES(2001, 90, "Chemistry");
INSERT INTO subject(id, marks, tittle) VALUES(2002, 29, "Maths");