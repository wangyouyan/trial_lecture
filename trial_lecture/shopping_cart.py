# /usr/bin/env python
# -*- coding: utf-8 -*-

# 定义商品价格
product_list = [{"number": 1,"name": "电脑", "price": 1999},{"number":2,"name": "鼠标", "price": 10},
         {"number":3,"name": "游艇", "price": 20}, {"number":4,"name": "美女", "price": 998}]
# 定义商品清单
display_shopping_list = """
+--------------商品清单如下------------------+
+-----------—+----------------+-------------+
| 商品编号: 1 | 商品名称: 电脑  | 价格: 1999  |
+-----------—+----------------+-------------+
| 商品编号: 2 | 商品名称: 鼠标  | 价格: 10    |
+-----------—+----------------+-------------+
| 商品编号: 3 | 商品名称: 游艇  | 价格: 20    |
+-----------—+----------------+-------------+
| 商品编号: 4 | 商品名称: 美女  | 价格: 998   |
+-----------—+----------------+-------------+
"""
# 按照价格大小从左到右排序
for n in range(1, len(product_list)):
    for m in range(len(product_list)-n):
        num1 = product_list[m]
        num2 = product_list[m+1]
        if num1['price'] > num2['price']:
            temp = product_list[m]
            product_list[m] = num2
            product_list[m+1] = temp
print(display_shopping_list)
while True:
    enough_shopping_list = []
    salary = input("输入你有多少钱:")
    if not isinstance(salary, int):
        print("金额必须输入整数")
        continue
    if salary < product_list[0]['price']:
        print("你输入的金额不足以购买任何商品")
        break
    for item in product_list:
        if salary < item['price']:
            continue
        else:
            available_goods = ("| 商品编号:\033[1;35m %s \033[0m, | 名称: \033[1;43m %s \033[0m, | 价格: "
                               "\033[1;42m %d \033[0m |" % (item['number'], item['name'], item['price']))
            enough_shopping_list.append(available_goods)
    print("+------你可以购买的商品清单如下:------+")
    print "\n".join(enough_shopping_list)
    # 输入需要购买产品的编号与个数
    sum_price = 0
    shopping_list = []
    while True:
        product_num = input("输入产品编号:")
        if not isinstance(product_num, int):
            print("编号必须大于0的数字")
            continue
        if product_num > 4:
            print("不能超过商品编号的长度4")
        product_amount = input("输入产品个数:")
        if not isinstance(product_amount, int):
            print("个数必须大于0")
        for goods in product_list:
            if goods['number'] == product_num:
                sum_price += goods['price'] * product_amount
                if sum_price > salary:
                    print("当前输入的产品价格和数量超过你的承受范围......")
                else:
                    salary = salary - sum_price
                    shopping_cart = ("| 商品编号:\033[1;35m %s, | 名称:\033[1;36m %s \033[0m, | 价格:\033[1;37m "
                                     "%d \033[0m |数量: \033[1;38m %d \033[0m" % (goods['number'],
                                                                    goods['name'], goods['price'], product_amount))
                    shopping_list.append(shopping_cart)
        result = raw_input("是否继续购买? 如果继续输入y, 退出输入n:\n")
        if result == "y":
            continue
        elif result == "n":
            break
        else:
            print("必须输入合法的字符串,y或n")
    print("+---------------购买商品列表如下-------------------+")
    print "\n".join(shopping_list)
    print("你本次购物一共消费金额为: \033[1;42m %d \033[0m" % sum_price)
    break

