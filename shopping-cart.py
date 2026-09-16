#购物车系统
print("欢迎来到您的购物车!")
t="""
#################################
#     1.向购物车添加商品         #
#     2.修改购物车中的商品       #
#     3.删除购物车中的商品       #
#     4.查询购物商品信息         #
#     5.退出购物车系统           #
#################################
"""
print(t)
shopping_cart={}
while True:
    operation=int(input("请输入您要执行的操作(1——5):"))
    match operation:
        case 1:
            name=input("请输入要添加的商品名称:")
            price=float(input("请输入要添加商品的价格:"))
            amount=int(input("请输入要添加该商品的数量:"))
            if name in shopping_cart.keys():
                print("该商品已存在于购物车当中，请重新输入:")
            else:
                shopping_cart[name]={"shopping_price":price,"shopping_amount":amount}
        case 2:
            name=input("请输入要修改的商品名称:")
            if name in shopping_cart.keys():
                price=float(input("请输入要修改商品的价格:"))
                amount=int(input("请输入要修改该商品的数量:"))
                shopping_cart[name]={"shopping_price":price,"shopping_amount":amount}
            else:
                print("购物车中不存在该商品,请重新输入")
        case 3:
            name=input("请输入要删除的商品的名称:")
            if name in shopping_cart.keys():
                del shopping_cart[name]
            else:
                print("购物车中不存在该商品,请重新输入")
        case 4:
            for name in shopping_cart.keys():
                i=shopping_cart[name]
                print(f"商品名称:{name},价格:{i["shopping_price"]},数量:{i["shopping_amount"]}")
        case 5:
            print("退出购物车")
            break
        case _:
            print("操作非法，请重新输入")