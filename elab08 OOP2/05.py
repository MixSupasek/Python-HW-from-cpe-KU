class Student:
    def __init__(self,id,firstname,lastname,num_course = 0,total_credit = 0,advisor ="",major =""):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = num_course
        self.total_credit = total_credit
        self.advisor = advisor
        self.major = major
    def add_course(self,course):
        if course.course_id not in self.courses and self.total_credit + course.credit <= 25:
            self.courses.append(course.course_id)
            self.total_credit += course.credit
            self.num_course += 1
            return True
        else:
            return False
    def drop_course(self,course):
        if course.course_id in self.courses:
            self.courses.remove(course.course_id)
            self.total_credit -= course.credit
            self.num_course -= 1
            if len(self.courses) == 0:
                pass
            return True
        else:
            return False
    def set_advisor(self,advisor):
        self.advisor = advisor
    def set_major(self,major):
        self.major = major
    def __str__(self):
        itemlist = ' '.join(self.courses)
        return f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major}\nAdvisor: {self.advisor}\nCourses: {itemlist}"