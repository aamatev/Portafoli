# Als comentaris que posa "..." es perque es repeteix el mateix que el codi anterior
# Començarem amb una frase, preguntant al usuari el seu nom
print ("Hola, bon dia, com es el teu nom?")
nom = input() # Crearem una variable per que l'usuari posi el seu nom
print (f"Benvingut/uda a \"Yesterday And Today Restaurant\" {nom}, esperem que mengis bé i que no et quedis amb gana. \n")

# Fem un print oferint els menús
print ("Aquí tens la llista de menús amb els respectius preus que oferim a \"Yesterday And Today Restaurant\":") 
plat1 = (" 1. Broqueta de carabassó i pollastre a la llimona (10,25€) \n") # Crearem una variable per a cada plat
plat2 = ("2. Vedella guisada amb bolets (14,90€) \n") # ...
plat3 = ("3. Salmó a la planxa amb arròs (16,50€) \n") # ...
plat4 = ("4. Llom a la brasa amb verdures (15,75€) \n") # ...
plat5 = ("5. Sushi variat (20,00€) \n") # ...
print (plat1, plat2, plat3, plat4, plat5) # Amb un print executem totes les variables

# Col·locarem un while per poder fer un bucle dels menús i el posem en True (no es trencarà fins que no sigui veritat)
while True:
    print ("Quan sàpigues el menú que vols em dius, només m'has de dir el seu número identificatiu.") # Aquí amb l'ajuda d'un print indiquem a l'usuari que ens indiqui el menú
    platescollit = int(input()) # Crearem una variable per a que l'usuari ens indiqui el número identificatiu del plat
    
    # Començem l'estructura del while comparant el plat escollit de l'usuari amb el número identificatiu
    if platescollit == 1:
        print (f"El teu plat escollit es: {plat1}? (s/n)") # Aquí preguntem a l'usuari si realment aquest és el plat escollit, amb la resposta de s/n
        siono = input() # Crearem la variable amb l'input per que l'usuari contesti a la pregunta anterior
        if siono.lower() == "s": 
            persones = int(input("Per a quantes persones vols el menú: ")) # Si la resposta es "s", preguntarem a l'usuari la quantitat de persones que volen el menú
            preu = persones * 10.25 # Multiplicarem el nombre de persones per el preu del menú
            print (f"El preu total per a {persones} persones és de: {preu}€") # Fem un print amb el preu total del menú
        else:
            continue # Si el plat escollit no era l'1, es tornarà a repetir el codi
    # ...
    elif platescollit == 2: 
        print (f"El teu plat escollit es: {plat2}? (s/n)")
        siono = input()
        if siono.lower() == "s":
            persones = int(input("Per a quantes persones vols el menú:"))
            preu = persones * 14.90
            print (f"El preu total per a {persones} persones és de: {preu} euros.")
        else:
            continue
    # ...
    elif platescollit == 3:
        print (f"El teu plat escollit es: {plat3}? (s/n)")
        siono = input()
        if siono.lower() == "s":
            persones = int(input("Per a quantes persones vols el menú:"))
            preu = persones * 16.50
            print (f"El preu total per a {persones} persones és de: {preu} euros.")
        else:
            continue
    # ...
    elif platescollit == 4:
        print (f"El teu plat escollit es: {plat4}? (s/n)")
        siono = input()
        if siono.lower() == "s":
            persones = int(input("Per a quantes persones vols el menú:"))
            preu = persones * 15.75
            print (f"El preu total per a {persones} persones és de: {preu} euros.")
        else:
            continue
    # ...
    elif platescollit == 5:
        print (f"El teu plat escollit es: {plat5}? (s/n)")
        siono = input()
        if siono.lower() == "s":
            persones = int(input("Per a quantes persones vols el menú:"))
            preu = persones * 20
            print (f"El preu total per a {persones} persones és de: {preu} euros.")
        else:
            continue
    else:
        print ("Opció de plat no vàlida. Torna a introduir el número identificatiu.") # Acabem amb un else i un print, així si l'usuari posa qualsevol altre número que no estigui al menú
    break # Aquí posem un break per tallar el while i que de aquesta forma acabi el bucle
    
# Preguntarem al usuari si vol postres amb l'ajuda del print i una varibale per a que respongui
print ("Voldries postres? El seu preu es de 3€ per persona. (s/n)") 
postres = input()
if postres.lower() == "s": # Crearem un if amb la variable "postres" i un .lower, que serveix per a que detecti la resposta amb majúscules i minúscules
    postrespreu = 3 * persones # Multiplicarem el preu dels postres per el nombre de persones que volen postres
    print (f"Doncs serien {postrespreu} € per els postres") # Fem un print per veure quant costarien els posres
else:
    print ("Doncs serien 0€ per els postres") # Si no volen postres, posarem 0€ als postres

# ...
print ("Voldries cafè? El seu preu es de 1€ per persona. (s/n)")
cafes = input() 
if cafes.lower() == "s":
    cafespreu = 1 * persones
    print (f"Doncs serien {cafespreu} € per els cafè")
else:
    print ("Doncs serien 0€ per els cafè")

# Editarem les variables dels menús per poder posar els plats al codi final sense els números identificatius
plat1 = ("Broqueta de carabassó i pollastre a la llimona")
plat2 = ("Vedella guisada amb bolets") 
plat3 = ("Salmó a la planxa amb arròs") 
plat4 = ("Llom a la brasa amb verdures")
plat5 = ("Sushi variat") 

# Farem ifs depenent el que l'usuari hagi escollit
if postres.lower() and cafes.lower() == "s": # Fem el primer if amb les variables postres i cafè, el .lower i el and, si son iguals a s
    preutotal = preu + postrespreu + cafespreu # Crearem una nova variable amb el preu total del menú, el cafè i els postres
    if platescollit == 1: # Aquí posarem la mateixa frase només canviant el nom del plat
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat1}\", també {persones} unitats de \"postres\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotal} €")
    elif platescollit == 2: # ...
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat2}\", també {persones} unitats de \"postres\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotal} €")
    elif platescollit == 3: # ...
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat3}\", també {persones} unitats de \"postres\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotal} €")
    elif platescollit == 4: # ...
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat4}\", també {persones} unitats de \"postres\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotal} €")
    elif platescollit == 5: # ...
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat5}\", també {persones} unitats de \"postres\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotal} €")
elif postres.lower() == "n" and cafes.lower() == "s": # ...
    preutotca = preu + cafespreu # Crearem una nova variable amb el preu total del menú i el cafè, sense els postres
    if platescollit == 1:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat1}\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotca} €")
    elif platescollit == 2:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat2}\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotca} €")
    elif platescollit == 3:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat3}\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotca} €")
    elif platescollit == 4:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat4}\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotca} €")
    elif platescollit == 5:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat5}\" i també {persones} unitats de \"cafè\". El total a pagar és de: {preutotca} €")
elif  postres.lower() == "s" and cafes.lower() == "n": # ...
    preutotpos = preu + postrespreu # Crearem una nova variable amb el preu total del menú i els postres, sense el cafè
    if platescollit == 1:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat1}\", també {persones} unitats de \"postres\". El total a pagar és de: {preutotpos} €")
    elif platescollit == 2:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat2}\", també {persones} unitats de \"postres\". El total a pagar és de: {preutotpos} €")
    elif platescollit == 3:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat3}\", també {persones} unitats de \"postres\". El total a pagar és de: {preutotpos} €")
    elif platescollit == 4:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat4}\", també {persones} unitats de \"postres\". El total a pagar és de: {preutotpos} €")
    elif platescollit == 5:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat5}\", també {persones} unitats de \"postres\". El total a pagar és de: {preutotpos} €")
elif postres.lower() == "n" and cafes.lower() == "n": # ...
    if platescollit == 1:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat1}\". El total a pagar és de: {preu} €")
    elif platescollit == 2:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat2}\". El total a pagar és de: {preu} €")
    elif platescollit == 3:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat3}\". El total a pagar és de: {preu} €")
    elif platescollit == 4:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat4}\". El total a pagar és de: {preu} €")
    elif platescollit == 5:
        print (f"{nom}, has consumit {persones} unitats del menú \"{plat5}\". El total a pagar és de: {preu} €")