# -*- coding: utf-8 -*-
import arcpy 

arcpy.env.overwriteOutput = True
points = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'
countries = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp'
outpath = r'C:\Users\NITRO 5\Documents\SIG Projet\Data'

fields = ['NAME', 'POP_MAX', 'TIMEZONE']

arcpy.MakeFeatureLayer_management(points, 'points_layer2')
with arcpy.da.SearchCursor('points_layer2', fields) as cursor:
    for i in cursor:
        print(i[0].encode('utf-8'))
        print(i[1])
        print(i[2].encode('utf-8') + '\n') 
