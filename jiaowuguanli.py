#教务管理系统
print("欢迎来到教务管理系统!")
t="""
#############################################
#1.添加学生信息  2.修改学生信息  3.删除学生信息#
#4.查询学生信息  5.列出所有学生  6.统计班级成绩#
#               7.退出教务系统               #
#############################################
"""
date={}
while True:
    operation=int(input("请输入您要执行的操作(1-7):"))
    match operation:
        case 1:
            name=input("请输入要添加的学生姓名:")
            if name in date.keys():
                print("该学生姓名已存在,请重新输入")
            else:
                chinese=float(input("请输入该学生的语文成绩:"))
                math=float(input("请输入该学生的数学成绩:"))
                english=float(input("请输入该学生的英语成绩:"))
                date[name]={"chinese":chinese,"math":math,"english":english}
                print("添加成功")
        case 2:
            name=input("请输入要修改的学生的姓名:")
            if name not in date.keys():
                print("教务系统中不存在该学生，请重新输入")
            else:
                while True:
                    option=int(input("请输入要修改的科目(语文-1,数学-2,英语-3,退出-4):"))
                    match option:
                        case 1:
                            chinese=float(input("请输入语文成绩:"))
                            i=date[name]
                            i["chinese"]=chinese
                        case 2:
                            math=float(input("请输入数学成绩:"))
                            i=date[name]
                            i["math"]=math
                        case 3:
                            english=float(input("请输入英语成绩:"))
                            i=date[name]
                            i["english"]=english
                        case 4:
                            print("退出学生成绩修改")
                            break
                        case _:
                            print("操作错误,请重新输入")
        case 3:
            name=input("请输入要删除的学生的姓名:")
            if name not in date.keys():
                print("教务系统中不存在该学生,请重新输入")
            else:
                del date[name]
        case 4:
            name=input("请输入要查询的学生的姓名:")
            if name in date.keys():
                print(date[name])
            else:
                print("教务系统中不存在该学生")
        case 5:
            for name in date.keys():
                print(f"{name}的成绩为{date[name]}")
        case 6:
            chinese_=[i["chinese"] for i in date.values()]
            english_=[i["english"] for i in date.values()]
            math_=[i["math"] for i in date.values()]
            chinese_.sort()
            english_.sort()
            math_.sort()
            print(f"语文最高分为{chinese_[-1]},最低分为{chinese_[0]},平均分为{sum(chinese_)/len(chinese_)}")
            print(f"数学最高分为{math_[-1]},最低分为{math_[0]},平均分为{sum(math_)/len(math_)}")
            print(f"英语最高分为{english_[-1]},最低分为{english_[0]},平均分为{sum(english_)/len(english_)}")
            max_chinese=[name for name in date.keys() if date[name]["chinese"]==chinese_[-1]]
            max_math=[name for name in date.keys() if date[name]["math"]==math_[-1]]
            max_english=[name for name in date.keys() if date[name]["english"]==english_[-1]]
            min_chinese=[name for name in date.keys() if date[name]["chinese"]==chinese_[0]]
            min_math=[name for name in date.keys() if date[name]["math"]==math_[0]]
            min_english=[name for name in date.keys() if date[name]["english"]==english_[0]]
            print(f"语文最高分为{max_chinese},最低分为{min_chinese}")
            print(f"数学最高分为{max_math},最低分为{min_math}")
            print(f"英语最高分为{max_english},最低分为{min_english}")
        case 7:
            print("退出教务管理系统")
            break
        case _:
            print("操作错误,请重新输入")

