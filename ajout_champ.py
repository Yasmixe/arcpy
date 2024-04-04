# -*- coding: utf-8 -*-

import arcpy 

arcpy.env.overwriteOutput = True

couche = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'
nom_nouveau_champ = "ABCD"
type_donnees = "TEXT"
if nom_nouveau_champ not in [field.name for field in arcpy.ListFields(couche)]:
    arcpy.AddField_management(couche, nom_nouveau_champ, type_donnees)
    print("Le champ a ete ajoute avec succes")
else:
    print("Le champ existe deja dans la table attributaire.")
