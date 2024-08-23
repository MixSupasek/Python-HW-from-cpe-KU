class ClassRoom:
    def __init__(self,grade = 0,homeRoomTeacher = "",studentList = [],numStudents = 0):
        self.grade = grade
        self.homeRoomTeacher = homeRoomTeacher
        self.studentList = studentList
        self.numStudents = numStudents
    def get_student_no(self,n):
        return self.studentList[n-1]
    def add_student(self,student_name):
        if len(self.studentList) < 10:
            self.studentList.append(student_name)
            return True
        return False
    def change_student(self,n,new_name):
        if n <= len(self.studentList):
            if n <= 0:
                return False
            elif n > 0:
                self.studentList[n-1] = new_name
                return True
        return False
    def remove_student(self,student_name):
        for i in range(len(self.studentList)):
            if self.studentList[i] == student_name:
                self.studentList.pop(i)
                return True
                break
        return False
    def remove_student_no(self,n):
        if n <= len(self.studentList):
            if n <= 0:
                return False
            elif n > 0:
                self.studentList.pop(n-1)
                return True
    def set_grade(self,grade):
        self.grade = grade
    def set_homeroom_teacher(self,name):
        self.homeRoomTeacher = name
    def set_student_list(self,list):
        self.studentList = list
    def set_num_student(self,num):
        pass
    def get_grade(self):
        return self.grade
    def get_homeroom_teacher(self):
        return self.homeRoomTeacher
    def get_student_list(self):
        return self.studentList
    def get_num_student(self):
        return len(self.studentList)
        
    def __str__(self):
        a = f"Grade: {grade}\nHomeroom Teacher: {homeRoomTeacher}\nStudents: "
        b = ', '.join(map(str, self.studentList))
        a = a+b
        return a