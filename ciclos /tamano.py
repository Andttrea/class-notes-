with open("genes.gff") as file:
    for line in file:
       columnas = line.strip (). split ("\t") #strip quita los espacios y el split separa las columnas por tabulador
       tamano = int(columnas[4]) - int(columnas[3]) + 1 # el +1 es para que no se coma el último digito
       print (f"El tamaño del gen es {tamano} pb")