# -*- coding: utf-8 -*-

import arcpy 

table = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.dbf'

feature_class = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp'

join_field_table = "NAME"
join_field_feature_class = "NAME"

output_feature_class = 'C:\Users\NITRO 5\Documents\SIG Projet\Data'

#faire la jointure:

arcpy.JoinField_management(feature_class, join_field_feature_class, table,join_field_table)

#afficher le resultat:

with arcpy.da.SearchCursor(feature_class, ["NAME", "TYPE"] ) as cursor:
    for row in cursor:
        feature_id = row[0]
        table_name = row[1]
       