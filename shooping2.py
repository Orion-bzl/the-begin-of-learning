class goods:
    def __init__(self,name,price,amount):
        self.name=name
        self.price=price
        self.amount=amount
    def update_goods(self,price,amount):
        self.price=price
        self.amount=amount


class shoppingcart:
    def __init__(self):
        self.shoppinglist=[]

    def add_shopping(self):
        name=input("请输入要添加的商品名称:")
        for s in self.shoppinglist:
            if s.name==name:
                print("该商品已存在,请重新选择")
                return   
        price=int(input("请输入商品的价格:"))
        amount=int(input("请输入商品的数量:"))
        self.shoppinglist.append(goods(name,price,amount))
        print("添加成功")

    def updateshopping(self):
        name=input("请输入您要修改的商品名称:")
        for s in self.shoppinglist:
            if name==s.name:
                price=int(input("请输入修改后的商品价格:"))
                amount=int(input("请输入修改后的商品数量:"))
                goods.update_goods(self,price,amount)
                print("修改成功")
            else:
                print("该商品不存在,请重新输入")

    def delshopping(self):
        name=input("请输入您要删除的商品名称:")
        for s in self.shoppinglist:
            if s.name==name:
                self.shoppinglist.remove(s)
                print("删除成功")
            else:
                print("该商品不存在")

    def searchshopping(self):
        for s in self.shoppinglist:
            print(f"{s.name} {s.price} {s.amount}")


    def run(self):
        while True:
            print("###########################################################")
            print("#1.添加商品 2.修改商品 3.删除商品 4.查询购物车 5.退出购物车#")
            print("###########################################################")
            choice=input("请选择要执行的操作(1-5):")
            match choice:
                case "1":
                    self.add_shopping()
                case "2":
                    self.updateshopping()
                case "3":
                    self.delshopping()
                case "4":
                    self.searchshopping()
                case "5":
                    break
                case _:
                    print("输入有误,请重新选择")


shoppingcart1=shoppingcart()
shoppingcart1.run()

        
        