import json
from csv import*


def registra_avis(ruta_json):
    with open(ruta_json, 'r') as archivo_json:
       contenido_json=json.load(archivo_json)
       
    numero_avis=input("Ingrese el número de avistamiento: ")
    fecha=input("Ingrese fecha del avistamiento(DD-MM-AAAA): ")
    distancia=input("Ingrese distancia del avistamiento: ")
    ubicacion=input("Ingrese ubicacion del avistamiento: ")
    autor=input("Ingrese Autor del avistamiento: ")
    print(" ")
    print(" ")
    with open ("clasificacion.csv", "r") as clasi_csv:
        datos_clasi=reader(clasi_csv)
        for clasifi in datos_clasi:
            print(clasifi[0])
    print(" ")
    print(" ")      
    clasificacion=input("Ingrese a que clasificacion pertenece: ")
    if clasificacion =="Estrellas":
        clasificacion="Estrellas,E01,Esfera de gas que emite luz y calor por fusion nuclear"
    elif clasificacion=="Planetas":
        clasificacion="Planetas,P02,Cuerpos que orbitan una estrella, con forma esférica y órbita despejada"
    elif clasificacion=="Satelites":
        clasificacion="Satelites,S03,Objetos que orbitan planetas; pueden ser naturales o artificiales"
    elif clasificacion=="Meteoritos":
        clasificacion="Meteoritos,M04,Fragmento de roca o metal que alcanza la superficie terrestre desde el espacion"
    else:
        clasificacion="Cometas,C05,Cuerpos de hielo  y polvo que orbitan  el sol y desarrollan  una coma  y cola al acercase a él"
    descripcion=input("Ingrese una descripcion del avistamiento: ")


    nuevo_avis={
    
        numero_avis:{
            "Fecha":fecha,
            "Distancia":f"{distancia} km",
            "Ubicacion":ubicacion,
            "Autor":autor,
            "Clasificacion":clasificacion,
            "Descripcion":descripcion
            
        }
    }
    
    contenido_json["avistamientos"].append(nuevo_avis)

    with open(ruta_json, 'w') as archivo_json:
        json.dump(contenido_json, archivo_json, indent=4)
    print("Registro exitoso")
