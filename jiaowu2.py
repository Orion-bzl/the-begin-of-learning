class student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f"学生姓名:{self.name}/语文:{self.chinese}/数学:{self.math}/英语:{self.english}/总成绩:{self.chinese+self.math+self.english}"
    def score_change(self,chinese=None,math=None,english=None):
        if chinese is not None:self.chinese=chinese
        if math is not None:self.math=math
        if english is not None:self.english=english
class edumanagement:
    version=1.0
    def __init__(self):
        self.student_list=[]
    def add_student(self):
        name=input("请输入学生的姓名:")
        for s in self.student_list:
            if s.name==name:
                print("该学生信息已录入")
                return
        chinese=int(input("请输入语文成绩:"))
        math=int(input("请输入数学成绩:"))
        english=int(input("请输入英语成绩:"))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu1=student(name,chinese,math,english)
            self.student_list.append(stu1)
            print("学生信息添加成功")
        else:
            print("学生成绩有误")
    def update_score(self):
        name=input("请输入你要修改成绩的学生姓名:")
        for s in self.student_list:
            if s.name==name:
                print(s)
                chinese=int(input("请输入修改后的语文成绩:"))
                math=int(input("请输入修改后的数学成绩:"))
                english=int(input("请输入修改后的英语成绩:"))
                if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
                    student.score_change(self,chinese,math,english)
                    print(s)
                    return 
                else:
                    print("修改的成绩有问题")
                    return
            else:
                print("该学生不存在")
                return 
    def del_student(self):
        name=input("请输入要删除的学生姓名:")
        for s in self.student_list:
            if name==s.name:
                self.student_list.remove(s)
                print("学生信息删除成功")
                return
            else:
                print("未找到该学生信息")
    def search_student(self):
        name=input("请输入要删除的学生姓名")
        for s in self.student_list:
            if name==s.name:
                print(s)
            else:
                print("该学生不存在")
    def  run(self):
        while True:
            print("####################################################")
            print("#1.添加学生 2.修改学生 3.删除学生 4.查询学生 5.退出系统#")
            print("####################################################")
            choice=input("请输入要执行的操作:")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_score()
                    case "3":
                        self.del_student()
                    case "4":
                        self.search_student()
                    case "5":
                        break
            except ValueError as e:
                print("输入的值有错误,请重新输入:",e)
            except Exception as e:
                print("输入有误,请重新输入")


edu_manage=edumanagement()
edu_manage.run()


        



        

