# -*- coding: utf-8 -*-

import arcpy 

arcpy.env.overwriteOutput = True
couche_shp = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'
# Définir le chemin vers le fichier shapefile

# Utiliser la fonction ListFields pour obtenir la liste des champs
liste_fields = arcpy.ListFields(couche_shp)

# Parcourir la liste des champs et les afficher
print("Liste des champs de la couche shapefile :")
for field in liste_fields:
    print(field.name)
