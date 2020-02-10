class Group:

    # Group info, only name is required.
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.units = []

    def showGroupInfo(self):
        return str(self.name) +  ' ' + str(len(self.students)) + ' students'

class Course:

    # Course info.
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.units = []
        group.courses.append(self)  # Assign a this course to its group.

    # Agregar unidades nuevas con lista de tasks
    def addUnit(self):
        unit = []
        self.units.append(unit)

    # Agregar tarea y su puntaje
    def addAssigment(self, unit, assignment):
        self.units[unit].append(assignment)

    def showCourseInfo(self):
        return str(self.name) + ' ' + str(len(self.units)) + ' units'


# Main flow of the script
def main():

    # Create a group.
    tenth = Group("Tenth grade")
    print(tenth.showGroupInfo())

    # Create a course.
    robotics = Course("Robotics", tenth)
    print(robotics.showCourseInfo())

    a = {
        "title": "Arduino variables",
        "points": 1.5
    }


    for key in a:
        print(a[key])

#Call main() function.
if __name__ == '__main__':
  main()