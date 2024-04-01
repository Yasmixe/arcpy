import arcpy 

points = r"C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp"
countries = r"C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_admin_0_countries.shp"

outpath = r"C:\Users\NITRO 5\Documents\SIG Projet\Data"

countries_of_interest = [ 'Italy', 'Kenya', 'Jordan', 'Lebanon', 'Scotland', 'France']

arcpy.MakeFeatureLayer_management(points, 'points_layer')

for x in countries_of_interest:
    arcpy.Delete_management('countries_layer')  # Delete existing feature layer if it exists
    arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "NAME" = '{}' """.format(x))
    arcpy.SelectLayerByLocation_management('points_layer', 'WITHIN', 'countries_layer')
    arcpy.FeatureClassToFeatureClass_conversion('points_layer', outpath, 'cities_in_{}'.format(x))
