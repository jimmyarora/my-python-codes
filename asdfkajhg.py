Drugs = ["paracetamol", "citrazine", "amoxicillin", "azithromycin", "omperazole"]

i = 1
while i<=5:
    DrugSelect = input("Please type a DRUG name: ")
    if (DrugSelect) == ("Quit"):
        print("Program is closed")
        exit()
    
        

    
    if (DrugSelect) in (Drugs):
        print((DrugSelect) + "_info")
        print()
   
        

    else:
        print("This Drug Does Not Excist")
    

    if (DrugSelect)==(Drugs[0]):
        print ("Use---> Antipyretic and Antiinflamtory")
        print ("Side Effects---> heart burn and ulcer")
    

    if (DrugSelect)==(Drugs[1]):
        print ("Use---> Antihistamine")
        print ("Side Effects---> Sedation")


    if (DrugSelect)==(Drugs[2]):
        print ("Use---> Antibectirial")
        print ("Side Effects---> Joint Pain")


    if (DrugSelect)==(Drugs[3]):
        print ("Use---> Antibectirial")
        print ("Side Effects---> Becterial_Resistance")


    if (DrugSelect)==(Drugs[4]):
        print ("Use---> Antigastric")
        print ("Side Effects---> Digestion Problem")

    


    
 






    
