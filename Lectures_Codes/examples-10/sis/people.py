from abc import ABC
from sis.repos import Repo
from sis.courses import course_db
from sis.schedule import schedule_db

class LdapUser(ABC):
    def __init__(self, ldap_id, name, **kwargs):
        super().__init__(**kwargs)

        self._ldap_id = ldap_id
        self._name = name

    @property
    def ldap_id(self):
        return self._ldap_id

    @property
    def name(self):
        return self._name


class Student(LdapUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_attended_courses(self):
        return [scheduled_course.course for scheduled_course in schedule_db.current.scheduled_courses if scheduled_course.is_student_registered_for_course(self)]


class Teacher(LdapUser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_guaranteed_courses(self):
        return [course for course in course_db.current.get_all() if course.guarantor is self]

    def get_taught_courses(self):
        return [scheduled_course.course for scheduled_course in schedule_db.current.scheduled_courses if scheduled_course.is_taught_by(self)]

    def get_taught_course_components(self):
        return [scheduled_course_component for scheduled_course in schedule_db.current.scheduled_courses for scheduled_course_component in scheduled_course.scheduled_components if self in scheduled_course_component.teachers]

    def print_teaching_statistics(self):
        for comp in self.get_taught_course_components():
            students_count = len(comp.registered_students)
            print(f'{comp} - {students_count}')


class User(Student, Teacher):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f'User(ldap_id={self.ldap_id}, name={self.name})'


class UserDB(Repo):
    def __init__(self, **kwargs):
        super().__init__(key_attr='_ldap_id', **kwargs)


user_db = UserDB()