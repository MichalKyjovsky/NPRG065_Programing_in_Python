from sis.repos import Repo
from datetime import date


class ScheduledCourseComponent:
    def __init__(self, course_component, start_week, day, time, teachers, **kwargs):
        super().__init__(**kwargs)

        self._scheduled_course = None
        self._course_component = course_component

        self._start_week = start_week
        self._day = day
        self._time = time
        self._teachers = teachers
        self._registered_students = set()

    @property
    def scheduled_course(self):
        return self._scheduled_course

    @scheduled_course.setter
    def scheduled_course(self, value):
        self._scheduled_course = value

    @property
    def course_component(self):
        return self._course_component

    @property
    def teachers(self):
        return self._teachers

    @property
    def start_week(self):
        return self._start_week

    @property
    def day(self):
        return self._day

    @property
    def time(self):
        return self._time

    @property
    def registered_students(self):
        return self._registered_students

    def is_student_registered(self, student):
        return student in self._registered_students

    def register_student(self, student):
        assert self._scheduled_course.is_student_registered_for_course(student)
        assert not self._scheduled_course.is_student_registered_for_component(self._course_component, student)
        self._registered_students.add(student)

    def __str__(self):
        return f'{self._course_component} on {self._day} {self._time}'


class ScheduledCourse:
    def __init__(self, course, scheduled_components, **kwargs):
        super().__init__(**kwargs)

        self._schedule = None
        self._course = course

        self._scheduled_components = scheduled_components
        for comp in scheduled_components:
            comp.scheduled_course = self

        self._registered_students = set()

    def register_student(self, student):
        self._registered_students.add(student)

    def is_student_registered_for_component(self, course_component, student):
        for slot in self.get_slots_by_course_component(course_component):
            if slot.is_student_registered(student):
                return True

        return False

    def is_student_registered_for_course(self, student):
        return student in self._registered_students

    def get_slots_by_course_component(self, course_component):
        return filter(lambda x: x.course_component == course_component, self._scheduled_components)

    def is_taught_by(self, teacher):
        return any(teacher in comp.teachers for comp in self._scheduled_components)

    @property
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property
    def course(self):
        return self._course

    @property
    def scheduled_components(self):
        return self._scheduled_components

    @property
    def registered_students(self):
        return self._registered_students


class Schedule:
    def __init__(self, year, **kwargs):
        super().__init__(**kwargs)
        self._year = year
        self._scheduled_courses = dict()

    def add(self, scheduled_course):
        assert scheduled_course.schedule is None

        scheduled_course.schedule = self
        self._scheduled_courses[scheduled_course.course] = scheduled_course

    @property
    def scheduled_courses(self):
        return self._scheduled_courses.values()

    @property
    def year(self):
        return self._year


class ScheduleDB(Repo):
    def __init__(self, **kwargs):
        super().__init__(key_attr='_year', **kwargs)

    @property
    def current(self):
        return self.get(date.today().year)


schedule_db = ScheduleDB()
