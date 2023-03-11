from utils.porcentajes import porcentajes_dict

def revisar_grasa(new_data_dict):

    actual = float(new_data_dict["grasa"])
    sexo = new_data_dict["sexo"]
    sex_dict = porcentajes_dict["grasa"][sexo]
    edad = int(new_data_dict["edad"])

    for edades in sex_dict:
        _, edad_superior = edades.split("-")
        if edad <= int(edad_superior):
            edad_dict = sex_dict[edades]
            break

    for porcentajes in edad_dict:
        if actual >= edad_dict["elevado"]:
            porcentaje_actual = "muy elevado"
        if actual <= edad_dict[porcentajes]:
            porcentaje_actual = porcentajes
            break

    grasa_dict = {
        "sexo" : sexo, 
        "edad" : edades,
        "estado" : porcentaje_actual,
        "cantidad" : actual
        }

    if porcentaje_actual != "normal":
        if porcentaje_actual  == "bajo":
            valor_normal = porcentajes_dict["grasa"][sexo][edades]["bajo"]
        else:
            valor_normal = porcentajes_dict["grasa"][sexo][edades]["normal"]
        grasa_dict["faltante"] = -(float(actual) - float(valor_normal))
        if grasa_dict["faltante"] > 0:
            grasa_dict[""] = "subir"
        if grasa_dict["faltante"] < 0:
            grasa_dict["direccion"] = "bajar"
        grasa_dict["faltante_kg"] = abs(float(actual) - float(valor_normal))/100 * float(new_data_dict["peso"])

    return grasa_dict


def revisar_musculo(new_data_dict):

    actual = float(new_data_dict["musculo"])
    sexo = new_data_dict["sexo"]
    sex_dict = porcentajes_dict["musculo"][sexo]
    edad = int(new_data_dict["edad"])

    for edades in sex_dict:
        _, edad_superior = edades.split("-")
        if edad <= int(edad_superior):
            edad_dict = sex_dict[edades]
            break

    for porcentajes in edad_dict:
        if actual >= edad_dict["elevado"]:
            porcentaje_actual = "muy elevado"
        if actual <= edad_dict[porcentajes]:
            porcentaje_actual = porcentajes
            break

    musculo_dict = {
        "sexo" : sexo, 
        "edad" : edades,
        "estado" : porcentaje_actual,
        "cantidad" : actual
        }

    if porcentaje_actual != "normal":
        if porcentaje_actual  == "bajo":
            valor_normal = porcentajes_dict["musculo"][sexo][edades]["bajo"]
        else:
            valor_normal = porcentajes_dict["musculo"][sexo][edades]["normal"]
        musculo_dict["faltante"] = -(float(actual) - float(valor_normal))
        if musculo_dict["faltante"] > 0:
            musculo_dict["direccion"] = "subir"
        else:
            musculo_dict["direccion"] = "bajar"
        musculo_dict["faltante_kg"] = abs(float(actual) - float(valor_normal))/100 * float(new_data_dict["peso"])

    return musculo_dict

def revisar_IMC(new_data_dict):

    actual = float(new_data_dict["IMC"])
    sexo = new_data_dict["sexo"]
    sex_dict = porcentajes_dict["IMC"][sexo]

    for porcentajes in sex_dict:
        if actual >= sex_dict["Obesidad grado 2"]:
            porcentaje_actual = "Obesidad grado 3"
        if actual <= sex_dict[porcentajes]:
            porcentaje_actual = porcentajes
            break

    IMC_dict = {
        "sexo" : sexo, 
        "estado" : porcentaje_actual,
        "cantidad" : actual
        }

    if actual < porcentajes_dict["IMC"][sexo]["bajo"]:
        IMC_dict["faltante"] = abs(float(new_data_dict["peso"]) - float(new_data_dict["altura"]) ** 2 * porcentajes_dict["IMC"][sexo]["bajo"])

        IMC_dict["direccion"] = "subir"
    elif actual > porcentajes_dict["IMC"][sexo]["normal"]:
        IMC_dict["faltante"] = abs(float(new_data_dict["peso"]) - float(new_data_dict["altura"]) ** 2 * porcentajes_dict["IMC"][sexo]["normal"])

        IMC_dict["direccion"] = "bajar"

    return IMC_dict