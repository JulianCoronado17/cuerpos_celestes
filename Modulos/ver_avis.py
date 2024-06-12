import json

def ver_avis_registrados(ruta_json):
    with open(ruta_json, 'r') as archivo_json:
       contenido_json=json.load(archivo_json)
    
    if contenido_json["avistamientos"]==None:
        pass
        