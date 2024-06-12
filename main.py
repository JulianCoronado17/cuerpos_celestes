import json
from csv import*
import os
from Modulos.hacer_registro import*

menu="""
1.Registrar avistamiento
2.Ver avistamientos registrados
"""
ruta_json='registro_avis.json'


while True:
    print(menu)
    opc=input("Escoja una opcion: ")
    if opc=="1":
        registra_avis(ruta_json)
        
        
    
        
        
        