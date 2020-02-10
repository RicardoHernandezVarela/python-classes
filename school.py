class Group:

    # Group info, only name is required.
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def __str__(self):
        return str(self.name) +  ' ' + str(len(self.students)) + ' students'

class Course:

    # Course info.
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.units = []
        group.courses.append(self)  # Assign this course to a group.

    # Add unit.
    def addUnit(self, name):
        unit = (name, [])
        self.units.append(unit)

    # Add assigment.
    def addAssigment(self, unit, assignment):
        self.units[unit][1].append(assignment)

    def __str__(self):
        return str(self.name) + ' ' + str(len(self.units)) + ' units'

class Student:

        # Student info.
        def __init__(self, name, lastname, group):
            self.name = name
            self.lastname = lastname
            self.group = group
            self.courses = group.courses
            self.assigments = []
            self.scores = []
            group.students.append(self)  # Assign this student to a group.
            
        def updateAssigments(self):
            # Get all student's assigments.
            for course in self.courses:
                for unit in course.units:
                    for assigment in unit[1]:
                        if assigment not in self.assigments:
                            self.assigments.append(assigment)
                            self.scores.append(0)
                        else:
                            pass
                
                print("Assigments list updated", self.assigments)

        def addScore(self, index, score):
            self.scores[index] = (score)

        def __str__(self):
            return str(self.name) + ' ' + str(self.lastname)

class Score:

    def __init__(self, student, assigment, score):
        self.studen = student
        self.assigment = assigment
        self.score = score
        self.total = assigment["points"] * score
        self.index = student.assigments.index(assigment)
        student.addScore(self.index, self.total)

    def __str__(self):
        return str(self.total)



# Main flow of the script
def main():

    # Create a group.
    tenth = Group("Tenth grade")
    print("New Group created:", tenth)

    # Create a course.
    robotics = Course("Robotics", tenth)
    print('New Course created {} in {}'.format(robotics.name, tenth.name))

    # Create a unit and assign it a course.
    robotics.addUnit("First")
    print('New unit created in {} course'.format(robotics.name))

    # Create an assigment for a unit.
    assigment_1 = {
        "title": "Arduino variables",
        "points": 1.5
    }

    robotics.addAssigment(0, assigment_1)
    print('{} assigment added to {} unit of {} course'.format(assigment_1['title'], robotics.units[0][0], robotics.name))

    # Create a student.
    ricardo = Student("Ricardo", "Varela", tenth)
    
    # Update assigmnets of a student.
    ricardo.updateAssigments()

    assigment_2 = {
        "title": "Arduino conditionals",
        "points": 1
    }

    robotics.addAssigment(0, assigment_2)

    ricardo.updateAssigments()

    # Find the index of a assigment(dict) in the assigments array.
    print(ricardo.assigments.index(assigment_1))

    a = Score(ricardo, assigment_2, 10)
    print(a.index)
    print(ricardo.scores)

#Call main() function.
if __name__ == '__main__':
  main()