menu='''
     1.idli               rs 30           
     2.wada               rs 35
     3.plain dosa         rs 50
     4.masala dosa        rs 75
     5.onion dosa         rs 85
     6.panner dosa        rs 100
     7.butter masala dosa rs 90
     8.uttpam             rs 50
     9.onion uttpam       rs 60
     10.panner uttpam     rs 70
     '''
#great
print (20*"=","WELCOME TO JAI HANUMAN HOTEL",20*"=")
print(20*" ","Malkapet,Rajanna sircilla")
items=({'idli':30,'wada':35,'plain dosa':50,'masala dosa':75,
'onion dosa':85,'panner dosa':100,'butter masala dosa':90,
'uttpam':50,'onion uttpam':60,'panner uttpam':70})
order_total=0
#60+70=130
item_1=input("enter the name of item you want to order:")
if item_1 in menu:
     # order_total+=menu(item_1) #order_total=order_total+menu 
                                 #0+50=50
   print({"your item {item_1} has been added to your order"})
else:
     print("ordered the item [item_1] is not available yet")
another_order=(input("do you want to add another item? (yes/no)"))
if another_order=="yes":
     item_2=(input("enter the neme of second item:"))
     if item_2 in menu:
          # order_total+=menu(item_2)
          print("item[item_2] has been added to order")
     else:
          print("ordered item[item_2]is not availalable")
print("the total amount of items to pay is [order_total]")






