from sis.repos import RepoWithHistory, ObjectWithValidity
from abc import ABC
from enum import Enum


class CourseComponent(ABC):
    def __init__(self, name, hours, period, **kwargs):
        super().__init__(**kwargs)

        self._course = None
        self._hours = hours
        self._period = period
        self._name = name

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        self._course = value

    @property
    def hours(self):
        return self._hours

    @property
    def period(self):
        return self._period

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f'{self._course} ({self._name})'


class LabComponent(CourseComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'LabComponent(name={self.name}, course={self.course}, hours={self.hours}, period={self.period})'


class LectureComponent(CourseComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'LectureComponent(name={self.name}, course={self.course}, hours={self.hours}, period={self.period})'


class Semester(Enum):
    FALL = 'Fall'
    SPRING = 'Spring'


class Course(ObjectWithValidity):
    def __init__(self, name, code, e_credits, semester, guarantor, course_components, **kwargs):
        super().__init__(**kwargs)

        self._name = name
        self._code = code
        self._e_credits = e_credits
        self._semester = semester
        self._guarantor = guarantor

        self._course_components = course_components
        for comp in course_components:
            comp.course = self

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def e_credits(self):
        return self._e_credits

    @property
    def semester(self):
        return self._semester

    @property
    def guarantor(self):
        return self._guarantor

    @property
    def course_components(self):
        return self._course_components

    def __repr__(self):
        return f'Course(name="{self._name}", code="{self._code}", e_credits={self._e_credits}, semester={self._semester}, guarantor={self._guarantor}, course_components={self._course_components}'

    def __str__(self):
        return f'{self._name}'


class CourseDB(RepoWithHistory):
    def __init__(self, **kwargs):
        super().__init__(key_attr='code', **kwargs)


course_db = CourseDB()
