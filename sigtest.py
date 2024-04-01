# -*- coding: utf-8 -*-

import arcpy 

# Chemin de la géodatabase world 
geodatabase_world2 = r"C:\Users\NITRO 5\Documents\SIG Projet\Data\geodatabase_world2.gdb"

# Création d'une liste qui va contenir toutes les classes d'entité
feature_classes = [r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp', 
                   r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_1_states_provinces.shp', 
                   r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp']

# Création de la base de données à partir des classes
arcpy.CreateFileGDB_management(r'C:\Users\NITRO 5\Documents\SIG Projet\Data', "geodatabase_world2.gdb")

for i in feature_classes:
    arcpy.FeatureClassToGeodatabase_conversion(i, geodatabase_world2)

print("Géodatabase créée avec succès : {}".format(geodatabase_world2))  

