# -*- coding: utf-8 -*-
import arcpy 

arcpy.env.overwriteOutput = True
points = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'
countries = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\Users\NITRO 5\Documents\SIG Projet\Data'
arcpy.MakeFeatureLayer_management(points, 'points_layer4')
with arcpy.da.UpdateCursor('points_layer4', ['NAMEALT']) as city_cursor:
    for x in city_cursor:
        print(x[0])
        x[0]= 'WE_JUST_UPDATED_THIS'
        city_cursor.updateRow(x)
        print('We updated this value to {}'.format(x[0]))