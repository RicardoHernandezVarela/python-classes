import copy

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
    def addAssignment(self, assignment):
        new_assignment = {
            "title": assignment.title,
            "points": assignment.points
        }

        self.units[assignment.unit][1].append(new_assignment)

    def __str__(self):
        return str(self.name) + ' ' + str(len(self.units)) + ' units'

class Assignment:

    def __init__(self, title, points, unit):
        self.title = title
        self.points = points
        self.unit = unit

    def __str__(self):
        return str(self.title) + ' ' + str(self.points)

class Student:

        # Student info.
        def __init__(self, name, lastname, group):
            self.name = name
            self.lastname = lastname
            self.group = group
            self.courses = group.courses
            self.total_scores = self.group.total_scores
            self.student_scores = {}
            group.students.append(self)  # Assign this student to a group.
        
        def addScore(self, score):

            query = {
                "title": score.assignment.title,
                "points": score.assignment.points
            }

            if score.course.name not in self.student_scores:

                self.student_scores[score.course.name] = copy.deepcopy(self.total_scores[score.course.name])
                print(self.student_scores)

                unitSelected = self.student_scores[score.course.name][score.unit]
                
                if query in unitSelected:
                    # Find the index of a assigment(dict) in the assigments array.
                    index = unitSelected.index(query)
                    unitSelected[index]["points"] = score.total
                    print(unitSelected[index]["points"])

        def __str__(self):
            return str(self.name) + ' ' + str(self.lastname)

class Score:

    def __init__(self, student, course, unit, assignment, score):
        self.student = student
        self.course = course
        self.unit = unit
        self.assignment = assignment
        self.score = score

        self.total = assignment.points * score
        student.addScore(self)
        #self.index = student.assignments.index(assignment)

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
    assignment_1 = Assignment("Arduino variables", 1.5, 0)

    robotics.addAssignment(assignment_1)
    print('{} assignment added to {} unit of {} course'.format(assignment_1.title, robotics.units[0][0], robotics.name))

    # Create a student.
    ricardo = Student("Ricardo", "Varela", tenth)
    print('Student {} was added to {} group'.format(ricardo.name, ricardo.group))
    

    # Check if assignmnets of a student update.
    print('Ricardo´s assignments {}'.format(ricardo.total_scores))

    assignment_2 = Assignment("Arduino conditionals", 1, 0)

    robotics.addAssignment(assignment_2)

    print('Ricardo´s assignments {}'.format(ricardo.total_scores))

    # Create a new course, check if update works.
    Math = Course("Math", tenth)

    # Create a unit and assign to a course, check if update works.
    robotics.addUnit("Second")
    print('New unit created in {} course'.format(robotics.name))

    Math.addUnit("First")
    print('New unit created in {} course'.format(Math.name))

    # Create an assignment for a unit, check if update works.
    assignment_3 = Assignment("Solve equations", 1.2, 0)

    Math.addAssignment(assignment_3)
    print('{} assignment added to {} unit of {} course'.format(assignment_3.title, Math.units[0][0], Math.name))

    print(tenth.total_scores)

    # Update assignmnets of a student, check if update works.
    print('Ricardo´s assigments {}'.format(ricardo.total_scores))

    # Create a ne student, check assignments.
    laura = Student("Laura", "Juarez", tenth)
    print('Student {} was added to {} group'.format(laura.name, laura.group))

    print('Laura assigments {}'.format(laura.total_scores))

    # Create a new course, check if update works.
    Music = Course("Music", tenth)

    print(' ')
    print('Ricardo´s assigments {}'.format(ricardo.total_scores))
    print('Laura assigments {}'.format(laura.total_scores))

    # Provitional function to create scores and check if updates correctly.
    def createScore(one, two):
        score_1 = Score(one[0], one[1], one[2], one[3], one[4])
        score_2 = Score(two[0], two[1], two[2], two[3], two[4])
        

        print(' ')
        print('Ricardo´s assigments {}'.format(two[0].student_scores))
        print('Laura assigments {}'.format(one[0].student_scores))

        print(' ')
        print('Ricardo´s assigments {}'.format(two[0].total_scores))
        print('Laura assigments {}'.format(one[0].total_scores))


    createScore([laura, Math, 0, assignment_3, 9], [ricardo, Math, 0, assignment_3, 8])
    createScore([laura, robotics, 0, assignment_1, 10], [ricardo, robotics, 0, assignment_2, 8])

#Call main() function.
if __name__ == '__main__':
  main()