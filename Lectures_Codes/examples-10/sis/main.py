from sis.courses import course_db, Course, LectureComponent, LabComponent, Semester
from sis.people import user_db, User
from sis.schedule import ScheduledCourse, ScheduledCourseComponent, Schedule, schedule_db
from datetime import time

# -----------------------------------------------------------------------------------------
# Teachers & teaching assistants
# -----------------------------------------------------------------------------------------
tbures = User(ldap_id='89380248', name='Tomas Bures')
user_db.add(tbures)

phnetynka = User(ldap_id='58387711', name='Petr Hnetynka')
user_db.add(phnetynka)

dcepelik = User(ldap_id='68817733', name='David Cepelik')
user_db.add(dcepelik)

vaschenbrenner = User(ldap_id='77361808', name='Vojtech Aschenbrenner')
user_db.add(vaschenbrenner)

pstemberova = User(ldap_id='29201523', name='Petra Štemberová')
user_db.add(pstemberova)

anovotny = User(ldap_id='70158753', name='Aleš ﻿Novotný')
user_db.add(anovotny)

mverner = User(ldap_id='27172598', name='Miroslav Verner')
user_db.add(mverner)


# -----------------------------------------------------------------------------------------
# Courses
# -----------------------------------------------------------------------------------------
python_lecture = LectureComponent(name="Lecture", hours=2, period=1)
python_lab = LabComponent(name="Lab", hours=2, period=1)
python = Course(
    name='Programming in Python',
    code='NPRG065',
    valid_from_year=2016,
    valid_till_year=2020,
    e_credits=5,
    semester=Semester.SPRING,
    guarantor=tbures,
    course_components=[python_lecture, python_lab]
)

course_db.add(python)


seds_lab = LabComponent(name="Lab", hours=4, period=2)
seds = Course(
    name='Software Engineering for Dependable Systems',
    code='NSWI054',
    valid_from_year=2016,
    valid_till_year=2020,
    e_credits=3,
    semester=Semester.SPRING,
    guarantor=tbures,
    course_components=[seds_lab]
)

course_db.add(seds)


dependability_lecture1 = LectureComponent(name="Lecture 1", hours=2, period=1)
dependability_lecture2 = LectureComponent(name="Lecture 1", hours=2, period=1)
dependability_lab = LabComponent(name="Lab", hours=2, period=1)
dependability = Course(
    name='Dependability and Security',
    code='NSWE009',
    valid_from_year=2016,
    valid_till_year=2020,
    e_credits=9,
    semester=Semester.FALL,
    guarantor=pstemberova,
    course_components=[dependability_lecture1, dependability_lecture2, dependability_lab]
)

course_db.add(dependability)


# -----------------------------------------------------------------------------------------
# Schedule for 2020
# -----------------------------------------------------------------------------------------
schedule_2020 = Schedule(year=2020)
schedule_db.add(schedule_2020)

python_2020_lecture = ScheduledCourseComponent(course_component=python_lecture, start_week=0, day='Monday', time=time(15, 40), teachers=[tbures, phnetynka])
python_2020_lab_1 = ScheduledCourseComponent(course_component=python_lab, start_week=0, day='Monday', time=time(14, 0), teachers=[dcepelik])
python_2020_lab_2 = ScheduledCourseComponent(course_component=python_lab, start_week=0, day='Tuesday', time=time(15, 40), teachers=[vaschenbrenner])
python_2020 = ScheduledCourse(course=python, scheduled_components=[python_2020_lecture, python_2020_lab_1, python_2020_lab_2])
schedule_2020.add(python_2020)

seds_2020_lab = ScheduledCourseComponent(course_component=seds_lab, start_week=1, day="Monday", time=time(9, 0), teachers=[tbures])
seds_2020 = ScheduledCourse(course=seds, scheduled_components=[seds_2020_lab])
schedule_2020.add(seds_2020)

dependability_2020_lecture1 = ScheduledCourseComponent(course_component=dependability_lecture1, start_week=0, day='Tuesday', time=time(10, 40), teachers=[pstemberova])
dependability_2020_lecture2 = ScheduledCourseComponent(course_component=dependability_lecture2, start_week=0, day='Thursday', time=time(12, 20), teachers=[pstemberova])
dependability_2020_lab_1 = ScheduledCourseComponent(course_component=dependability_lab, start_week=0, day='Monday', time=time(15, 40), teachers=[anovotny])
dependability_2020_lab_2 = ScheduledCourseComponent(course_component=dependability_lab, start_week=0, day='Thursday', time=time(14, 0), teachers=[mverner])
dependability_2020 = ScheduledCourse(
    course=dependability,
    scheduled_components=[dependability_2020_lecture1, dependability_2020_lecture2, dependability_2020_lab_1, dependability_2020_lab_2]
)
schedule_2020.add(dependability_2020)


# -----------------------------------------------------------------------------------------
# Students
# -----------------------------------------------------------------------------------------
jviktorin = User(ldap_id='97189976', name='Jiří Viktorin')
user_db.add(jviktorin)

rzoubkova = User(ldap_id='47854772', name='Renáta Zoubková')
user_db.add(rzoubkova)

smedkova = User(ldap_id='14052212', name='Soňa Medková')
user_db.add(smedkova)

okolisek = User(ldap_id='64049942', name='Ondřej Kolísek')
user_db.add(okolisek)

dhruba = User(ldap_id='48174418', name='Dagmar Hrubá')
user_db.add(dhruba)

lkremen = User(ldap_id='23639766', name='Lukáš Křemen')
user_db.add(lkremen)

jpetr = User(ldap_id='77438394', name='Jozef Petr')
user_db.add(jpetr)

msevera = User(ldap_id='91233219', name='Miroslav Severa')
user_db.add(msevera)


# -----------------------------------------------------------------------------------------
# Registration of students to lectures
# -----------------------------------------------------------------------------------------
python_2020.register_student(jviktorin)
python_2020_lecture.register_student(jviktorin)
python_2020_lab_1.register_student(jviktorin)

dependability_2020.register_student(jviktorin)
dependability_2020_lecture1.register_student(jviktorin)
dependability_2020_lecture2.register_student(jviktorin)
dependability_2020_lab_1.register_student(jviktorin)

python_2020.register_student(msevera)
python_2020_lecture.register_student(msevera)
python_2020_lab_2.register_student(msevera)

print(jviktorin.get_attended_courses())
print(tbures.get_guaranteed_courses())

print()

print(f'Statistics for {tbures.name}:')
print('--------------------------------')
tbures.print_teaching_statistics()