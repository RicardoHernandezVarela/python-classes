class Group:

    # Group info, only name is required.
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []
        self.units = []

    def showGroupInfo(self):
        return str(self.name) +  ' ' + str(len(self.students)) + ' students'

def main():

    tenth = Group("Tenth grade")
    print(tenth.showGroupInfo())




#Call main() function.
if __name__ == '__main__':
  main()