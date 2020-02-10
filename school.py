class Group:

    # Group info, only name is required.
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.total_scores = {}

    def updateCourses(self, course):
        if course.name not in self.total_scores:
            self.total_scores[course.name] = []
        else:
            pass

    def __str__(self):
        return str(self.name) +  ' ' + str(len(self.students)) + ' students'

class Course:

    # Course info.
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.units = []
        group.courses.append(self)  # Assign this course to a group.
        group.updateCourses(self)

    # Add unit.
    def addUnit(self, name):
        unit = (name, [])
        self.units.append(unit)
        self.group.total_scores[self.name].append(unit[1])

    # Add assigment.
    def addAssignment(self, unit, assignment):
        new_assignment = {
            "title": assignment.title,
            "points": assignment.points
        }

        self.units[unit][1].append(new_assignment)

    def __str__(self):
        return str(self.name) + ' ' + str(len(self.units)) + ' units'

class Assignment:

    def __init__(self, title, points):
        self.title = title
        self.points = points

    def __str__(self):
        return str(self.title) + ' ' + str(self.points)

class Student:

        # Student info.
        def __init__(self, name, lastname, group):
            self.name = name
            self.lastname = lastname
            self.group = group
            self.courses = group.courses
            self.total_scores = group.total_scores
            group.students.append(self)  # Assign this student to a group.
        
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

    # Create a unit and assign to a course.
    robotics.addUnit("First")
    print('New unit created in {} course'.format(robotics.name))

    # Create an assigment for a unit.
    assignment_1 = Assignment("Arduino variables", 1.5)

    robotics.addAssignment(0, assignment_1)
    print('{} assignment added to {} unit of {} course'.format(assignment_1.title, robotics.units[0][0], robotics.name))

    # Create a student.
    ricardo = Student("Ricardo", "Varela", tenth)
    print('Student {} was added to {} group'.format(ricardo.name, ricardo.group))
    

    # Check if assignmnets of a student update.
    print('Ricardo´s assignments {}'.format(ricardo.total_scores))

    assignment_2 = Assignment("Arduino conditionals", 1)

    robotics.addAssignment(0, assignment_2)

    print('Ricardo´s assignments {}'.format(ricardo.total_scores))

    # Create a new course, check if update works.
    Math = Course("Math", tenth)

    # Create a unit and assign to a course, check if update works.
    robotics.addUnit("Second")
    print('New unit created in {} course'.format(robotics.name))

    Math.addUnit("First")
    print('New unit created in {} course'.format(Math.name))

    # Create an assigment for a unit, check if update works.
    assignment_3 = Assignment("Solve equations", 1.2)

    Math.addAssignment(0, assignment_3)
    print('{} assignment added to {} unit of {} course'.format(assignment_3.title, Math.units[0][0], Math.name))

    print(tenth.total_scores)

    # Update assigmnets of a student, check if update works.
    print('Ricardo´s assigments {}'.format(ricardo.total_scores))

"""
    # Find the index of a assigment(dict) in the assigments array.
    print(ricardo.assigments.index(assigment_1))

    first_score = Score(ricardo, assigment_2, 10)
    print('Student {} was assigned {} to {} assigment'.format(ricardo.name, first_score.total, assigment_2['title']))
"""

#Call main() function.
if __name__ == '__main__':
  main()