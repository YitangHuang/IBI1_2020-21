class Student(object):

    def __init__(self, first_name, last_name, programme):
        self.first_name = first_name
        self.last_name = last_name
        self.programme = programme
    def information(self):
        return('Name: ' + self.first_name + ' ' + self.last_name + '     ' + 'Programme: ' + self.programme)


# an example:
info1= Student('Yitang', 'Huang', 'BMS')
print(info1.information())

