from datetime import date
from collections import defaultdict


class Repo:
    def __init__(self, key_attr, **kwargs):
        super().__init__(**kwargs)

        self.__db = dict()
        self.__key_attr = key_attr

    def add(self, obj):
        key = getattr(obj, self.__key_attr)
        assert key not in self.__db
        self.__db[key] = obj

    def get(self, key):
        return self.__db[key]

    def get_all(self):
        return self.__db.values()


# --------------------------------------------------------------------------------------------


class ObjectWithValidity:
    def __init__(self, valid_from_year, valid_till_year, **kwargs):
        super().__init__(**kwargs)

        self._valid_from_year = valid_from_year
        self._valid_till_year = valid_till_year

    def is_valid_at(self, year):
        return self._valid_from_year <= year <= self._valid_till_year

    def validity_overlaps(self, obj):
        return self._valid_from_year <= obj.valid_from_year <= self._valid_till_year or \
               obj.valid_from_year <= self._valid_from_year <= obj.valid_till_year


class RepoWithHistory:
    def __init__(self, key_attr, **kwargs):
        super().__init__(**kwargs)

        self.__db = defaultdict(list)
        self.__key_attr = key_attr

    class Slice:
        def __init__(self, db_self, year):
            self._year = year
            self._db_self = db_self

        def get(self, key):
            objs = self._db_self.get(key)
            return next((obj for obj in objs if obj.is_valid_at(self._year)), None)

        def get_all(self):
            objs = self._db_self.get_all()
            return [obj for obj in objs if obj.is_valid_at(self._year)]

    def get(self, key):
        return self.__db[key]

    def get_all(self):
        return [item for sublist in self.__db.values() for item in sublist]

    def add(self, obj):
        key = getattr(obj, self.__key_attr)
        contained_objs = self.__db[key]

        assert all(not obj.validity_overlaps(obj) for obj in contained_objs)

        contained_objs.append(obj)

    @property
    def current(self):
        return RepoWithHistory.Slice(self, date.today().year)




