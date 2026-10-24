from abc import ABC, abstractmethod
#书籍类
class Book:
    def __init__(self,id,name,author,total_num):
        self.name = name
        self.author = author
        self.id = id
        self.total_num = total_num
        self.available_num = total_num
    def borrow(self):
        if self.available_num > 0:
            self.available_num -= 1
            return True
        else:
            return False
    def return_book(self):
        self.available_num += 1

    def get_available_num(self):
        return self.available_num

#会员类

class Member(ABC):
    def __init__(self,id,name,password):
        self.id = id
        self.name = name
        self.__password = password
        self.borrowed_books = []
    def borrow(self,book:Book):
        if len(self.borrowed_books)>=self.max_borrow_num():
            print("借阅失败,借阅数量已达上限")
            return False
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name}成功借阅了{book.name}")
            return True
        else:
            print(f"{self.name}借阅失败,没有此书或书已借完")
            return False
    @abstractmethod
    def max_borrow_num(self):
        pass
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name}成功还了{book.name}")
        else:
            print(f"{self.name}没有借过此书")

    def get_password(self):
        return self.__password
    
class NormalMember(Member):
    def max_borrow_num(self):
        return 3

class VipMember(Member):
    def __init__(self,id,name,password,vip_level):
        super().__init__(id,name,password)
        self.vip_level = vip_level

    def max_borrow_num(self):
        return 6+self.vip_level


#创建图书管理系统
class Librarysystem:
    def __init__(self):
        self.books={}
        self.members={}
        self.current_member=None
        self.load_books()
        self.load_members()

    def load_books(self):
        self.books["01"]=Book("01","Python","Guido",5)
        self.books["02"]=Book("02","Java","James",3)
        self.books["03"]=Book("03","C++","Bjarne",2)
        self.books["04"]=Book("04","C","Dennis",1)
        self.books["05"]=Book("05","Go","Robert",4)
        self.books["06"]=Book("06","Ruby","Yukihiro",5)
        print("图书加载完成")

    def load_members(self):
        self.members["N001"]=NormalMember("N001","张三","123456")
        self.members["N002"]=NormalMember("N002","李四","123456")
        self.members["V001"]=VipMember("V001","王五","123456",2)
        self.members["V002"]=VipMember("V002","赵六","123456",3)
        print("会员加载完成")

    def login(self):
        while True:
            print("-------登录界面---------")
            id=input("请输入会员ID:")
            password=input("请输入密码:")
            if id in self.members and self.members[id].get_password()==password:
                self.current_member=self.members[id]
                print(f"{self.current_member.name}登录成功")
                return True
            else:
                print("会员ID或密码错误,请重新输入")

    def borrow_book(self):
        print("-------借阅图书---------")
        for book in self.books.values():
            print(f"编号:{book.id},书名:{book.name},作者:{book.author},总数:{book.total_num},可借数量:{book.get_available_num()}")
        id=input("请输入图书ID:")
        if id not in self.books.keys():
            print("图书不存在")
            return
        self.current_member.borrow(self.books[id])

    def return_book(self):
        print("-------归还图书--------")
        borrowed_books=self.current_member.borrowed_books()
        for book in borrowed_books.values():
            print(f"编号:{book.id},书名:{book.name}")
        book_id=input("请输入图书ID:")
        if book_id  not in self.books:
            print("还书失败,不存在该图书编号")
            return
        self.current_member.return_book(self.books[book_id])

    def query_borrow(self):
        borrowed_books=self.current_member.borrowed_books
        if len(borrowed_books)>0:
            for book in borrowed_books.values():
                print(f"编号:{book.id},书名:{book.name}")
        else:
            print("没有借阅图书")



    def run(self):
        if self.login():
            while True:
                print("-------图书管理系统---------")
                print("1.借阅图书")
                print("2.归还图书")
                print("3.查询借阅")
                print("4.退出系统")
                choice=input("请选择操作:")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.query_borrow()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效的选择,请重新输入")
if __name__=="__main__":
    ls=Librarysystem()
    ls.run()
    

