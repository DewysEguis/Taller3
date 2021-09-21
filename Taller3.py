
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

# Punto 5

def pto5 (num):
    men = num[len(num) - 1]
    for n in num:
        if n < men:
            men = n
    return men

# Punto 6

def ejercicio6():
    for i in range(5):
        ultimo_peso = int(input('Digite su ultimo peso:'))
        promedio_pesos = 0
        for i in range(10):
            promedio_pesos += int(input(f'Digite el peso de la bascula {i}:'))

        promedio_pesos = promedio_pesos / 10

        if promedio_pesos > ultimo_peso:
            print(f'SUBIÓ {promedio_pesos - ultimo_peso}')
        else:
            print(f'BAJÓ {ultimo_peso - promedio_pesos}')

# Punto 7

def pto7(n_prod):
    
    tot = 0
    for _ in range(n_prod):
        val = int(input('Digite el precio del producto: '))
        cant = int(input('Cantidad del producto: '))

        tot += val * cant
    return tot

# Punto 8

def pto8 (nu_entr, valor):
    edad1 = edad2 = edad3 = edad4 = edad5 = 0
    for i in range(nu_entr):

        edad = int(input('Digite su edad: '))
        if edad < 5:
            print('No puede ingresar')
        if edad >= 5 and edad <= 14:
            edad1 += valor * 0.35
        if edad >= 15 and edad <= 19:
            edad2 += valor * 0.25
        if edad >= 20 and edad <= 45:
            edad3 += valor * 0.1 
        if edad >= 46 and edad <= 65:
            edad4 += valor * 0.25
        if edad > 65:
            edad5 += valor * 0.35

    return {
        "Categoria 1": edad1,
        "Categoria 2": edad2,
        "Categoria 3": edad3,
        "Categoria 4": edad4,
        "Categoria 5": edad5,
        }

# Punto 9

def pto9():
    for i in range(1):
        ven = int(input(f'{i} Valor vendido: '))

        if ven <= 20000000:
            print(f'Total vendido: {ven}')
            print(f'Comision: {ven * 0.1}')
        elif ven > 20000000 and ven < 40000000:
            print(f'Total vendido: {ven}')
            print(f'Comision: {ven * 0.15}')
        elif ven >= 40000000 and ven < 80000000:
            print(f'Total vendido: {ven}')
            print(f'Comision: {ven * 0.2}')
        elif ven >= 80000000 and ven < 160000000:
            print(f'Total vendido: {ven}')
            print(f'Comision: {ven * 0.25}')
        elif ven > 160000000:
            print(f'Total vendido: {ven}')
            print(f'Comision: {ven * 0.3}')
 
# Punto 10

def pto10():
    votos1 = votos2 = votos3 = 0
    for i in range(5):
        voto = int(input('Digite el numero del participante (1, 2, 3): '))

        if voto == 1:
            votos1 += 1
        if voto == 2:
            votos2 += 1
        if voto == 3:
            votos3 += 1
        
    if votos1 > votos2 and votos1 > votos3:
        return f'Participante 1 ganó... # de votos: {votos1}'
    elif votos3 > votos1 and votos3 > votos2:
        return f'Participante 3 ganó... # de votos: {votos3}'
    elif votos2 > votos1 and votos2 > votos3:
        return f'Participante 2 ganó... # de votos: {votos2}'
    elif votos1 == votos2 or votos1 == votos3 or votos2 == votos3:
        return f'Empate... total de votos: 50000'

 