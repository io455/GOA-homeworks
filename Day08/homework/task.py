from turtle import*

v1 = 5
v2 = 10
v3 = 15
v4 = 20
v5 = 25

def new_price(price, dis_percent):
    dis_amount = price * dis_percent/100
    fin_price = price - dis_amount
    return price - fin_price

final_price = new_price(v1, 20)
final_price2 =  new_price(v2, 20)
final_price3 = new_price(v3, 20)
final_price4 = new_price(v4, 20)
final_price5 = new_price(v5, 20)

print(final_price, final_price2, final_price3, final_price4, final_price5)