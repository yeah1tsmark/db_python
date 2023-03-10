# install peewee
from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "Mark.db"))


# create table
class User(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = db


User.create_table(fail_silently=True)


class Student(Model):
    student_name = CharField()
    student_id = CharField(unique=True)
    student_class = CharField()

    class Meta:
        database = db


Student.create_table(fail_silently=True)


class People(Model):
    person_name = CharField()
    person_number = CharField()
    person_email = CharField(unique=True)
    person_country = CharField()
    person_gender = CharField()
    person_religion = CharField()
    person_password = CharField()

    class Meta:
        database = db


People.create_table(fail_silently=True)