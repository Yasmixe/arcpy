import arcpy


states = r"C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp"
countries = r"C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp"

outpath = r"C:\Users\NITRO 5\Documents\SIG Projet\Data"

arcpy.MakeFeatureLayer_management(states, 'points_layer')
# In  2021, the United States "Name" value has changed from 'United States' to 'United States of America'
arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = 'France' """)

arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')

arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'states_france')
