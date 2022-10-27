class Student(object):
    def __init__(self, name, age, sno) -> None:
        self.name = name
        self.age = age
        self.sno = sno

    def __repr__(self):
        return 'Student [name: %s, age: %d, sno: %d]' % (self.name, self.age, self.sno)

    def object_hook(self):
        return Student(self['name'], self['age'], self['sno'])
