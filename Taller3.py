
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