
# Punto 1

def pto1 (aut):
    car_amarilla = 0
    car_rosa = 0
    car_roja = 0
    car_verde = 0
    car_azul = 0

    for auto in aut:
        if auto == 1 or auto == 2:
            car_amarilla += 1
        elif auto == 3 or auto == 4:
            car_rosa += 1
        elif auto == 5 or auto == 6:
            car_roja += 1
        elif auto == 7 or auto == 8:
            car_verde += 1
        elif auto == 9 or auto == 0:
            car_azul += 1

    return {
        "Autos amarillos": car_amarilla,
        "Autos rosa": car_rosa,
        "Autos rojos": car_roja,
        "Autos verdes": car_verde,
        "Autos azules": car_azul
    }

# Punto 2

def pto2 (animal):
    edad_animales = []
    if animal.lower() == 'elefante':
        for i in range(20):
            elefante = int(input('Digite la edad del elefante:'))
            edad_animales.append(elefante)
    if animal.lower() == 'jirafa':
        for i in range(15):
            jirafa = int(input('Digite edad de la jirafa:'))
            edad_animales.append(jirafa)
    if animal.lower() == 'chimpance':
        for i in range(40):
            chimpance = int(input('Digite la edad del chimpance:'))
            edad_animales.append(chimpance)
    
    c1 = c2 = c3 = 0
    for edad in edad_animales:
        if edad >= 0 and edad <= 1:
            c1 += 1
        elif edad > 1 and edad < 3:
            c2 += 1
        elif edad >= 3:
            c3 += 1
    
    if animal.lower() == 'elefante':
        c1 = (c1 * 100) / 20 
        c2 = (c2 * 100) / 20
        c3 = (c3 * 100) / 20
        
    if animal.lower() == 'jirafa':
        c1 = (c1 * 100) / 15 
        c2 = (c2 * 100) / 15
        c3 = (c3 * 100) / 15
        
    if animal.lower() == 'chimpance':
        c1 = (c1 * 100) / 40
        c2 = (c2 * 100) / 40
        c3 = (c3 * 100) / 40


    return {
        "animal": animal,
        "Entre 0 y 1 año": c1,
        "Entre 1 y 3 años": c2,
        "Mayor o igual a 3 años": c3
    }

# Punto 3

def pto3 (h_obr):
    for obr in h_obr:
        if obr <= 40:
            print(f'Pago por 40 horas o menos: {obr * 20}')
        elif obr > 40:
            print(f'Pago por cada una de las primeras horas: {40 * 20 + ((obr - 40) * 25)} ')

# Punto 4

def pto4 (ed_hom, ed_muj):
    acu_hom = acu_muj = total = 0
    for edad in ed_hom:
        acu_hom += edad
        total += edad
    for edad in ed_muj:
        acu_muj += edad
        total += edad
    
    return {
        "Promedio edad hombres": acu_hom / len(ed_hom),
        "Promedio edad mujeres": acu_muj / len(ed_muj),
        "Promedio edad general": total / (len(ed_hom) + len(ed_muj))
    }

