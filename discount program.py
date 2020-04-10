actual_Price = int(input("what is the actual price??"))
print(actual_Price)
discount= int(input("how much discount you wanna giv?"))
print(discount)
discount_in_numbrs = actual_Price* discount/100
final_charge= actual_Price - discount_in_numbrs
print("final charge is" ,final_charge)
