# -*- coding: utf-8 -*-

import arcpy 

arcpy.env.overwriteOutput = True

couche = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'

nom_champ = "NAME_HI"

if nom_champ in [field.name for field in arcpy.ListFields(couche)]:
    arcpy.DeleteField_management(couche, nom_champ)
    print("Le champ a ete supprime")
else:
    print("Le champ nexiste pas dans la table attributaire")
