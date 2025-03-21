apes = ["POngo pygameus", "Gorilla gorilla", "Pan paniscus"]

for ape in apes: 
    print(f"{ape} is an ape. Its name starts with {first_letter}") #f se usa para concatenar las cadenas
    print(f"Its name has {name_length} letters")
    
    
  #otra forma de ver este código 
    #name_length = len(ape) #aqui se calcula la longitud del nombre
    #first_letter = ape[0] #aqui se obtiene la primera letra del nombre
    # print(ape + " is an ape. Its name starts with " + first_letter) # el + se usa para concatenar las cadenas 
    # print("Its name has " + str(name_length) + " letters") #str se usa para convertir un numero en un string 