secuencias = "ATGATGTACGTCC"

for i, base in enumerate(secuencias): #enumerate devuelve el indice y el valor de la secuencia
    print(f"Posicion {i} : {base}") 

# función zip va a iterar sobre multiples listas al mismo tiempo

bases = "ATGCGACAT" #si las listas no son del mismo tamano entonces zip se va a quedar con el tamano de la lista más corta
complemento = "TACG"

for base, complemento in zip(bases, complemento): # base no es una palabra reservada, se puede llamar como se quiera
    print(F" {base} le corresponde {complemento}") 


# otro funcion zip

genes = ["thrL", "thrA", "thrB"]
longitudes = [66, 2463]  # Lista más corta
for gen, tamaño in zip(genes, longitudes):
    print(f"Gen: {gen}, Tamaño: {tamaño} pb")