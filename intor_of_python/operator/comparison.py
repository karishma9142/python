name = input("enter your name : ")

if len(name) < 3 :
    print("name must be at least 3 charatres")
elif len(name) > 50 :
    print("name can be a maximum of 50 characters")  
else :
    print("name looks good")      