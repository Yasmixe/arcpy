# -*- coding: utf-8 -*-

import arcpy 

arcpy.env.overwriteOutput = True

couche = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_1_states_provinces.shp'

# Liste pour stocker les noms des champs avec des cases vides
champs_vides = []
arcpy.MakeFeatureLayer_management(couche, 'points_layer8')
# Ouvrir un curseur de recherche pour parcourir les enregistrements
with arcpy.da.SearchCursor('points_layer8', "*") as curseur:
    # Parcourir chaque enregistrement
    for row in curseur:
        # Parcourir chaque champ dans l'enregistrement
        for index, value in enumerate(row):
            # Vérifier si la valeur du champ est vide
            if value == None or value == "":
                # Ajouter le nom du champ à la liste des champs vides
                champs_vides.append(curseur.fields[index].name)

# Supprimer les doublons de la liste des champs vides
champs_vides = list(set(champs_vides))

# Afficher les noms des champs avec des cases vides
if len(champs_vides) > 0:
    print("Les champs suivants ont des cases vides :")
    for champ in champs_vides:
        print(champ)
else:
    print("Aucun champ n'a de case vide dans la couche de données.")
