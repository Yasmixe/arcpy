import arcpy 

arcpy.env.overwriteOutput = True
points = r'C:\Users\NITRO 5\Documents\SIG Projet\Data\ne_10m_populated_places.shp'

field_list = arcpy.ListFields(points)
print(field_list)
list_field = []
arcpy.MakeFeatureLayer_management(points, 'points_layer5')

for x in field_list:
    print( x.name)
    print(x.type)
    if x.type == 'String':
        list_field.append(x.name)
    else:
        print('This is not a String, it is {}'.format(x.type))

for field in list_field:

    with arcpy.da.UpdateCursor('points_layer5', [field]) as city_cursor:
        for x in city_cursor:
            print(x[0].encode('utf-8'))
            if x[0] == ' ':
                x[0] = 'STARWARS'
                city_cursor.updateRow(x)
                print( 'We updated this value to {}'.format(x[0].encode('utf-8')))