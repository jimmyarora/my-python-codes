''' make a list of drug'''
''' take input for searching the drug from the list'''
''' Give the result of use, side efects of the dtrug'''
'''drug_list = ["paracetamol", "citrazine", "amoxicillin"]
print(drug_list)'''

Colors = ["Red", "Orange", "Yellow", "Green", "Blue"]
ColorSelect = input("Please type a color name: ")
if (ColorSelect) in (Colors):
    print(yes)

'''if (Colors.count(ColorSelect) >= 1):
  print("The color exists in the list!")
elif (str.upper(ColorSelect) != "QUIT"):
  print("The list doesn't contain the color.")
