point_layers = []
for i in 0.8,0.6,0.4,0.2:
    resized_pole = processing.run("shapetools:geodesictransformations", {'INPUT':'D:/С диска C/Хакатон/Pole.dbf|layername=Pole','TransformRotation':0,'TransformScale':i,'TransformDistance':0,'TransformAzimuth':0,'TransformUnits':0,'OUTPUT':'TEMPORARY_OUTPUT'})
    layer = resized_pole['OUTPUT']
    line_layer = processing.run("native:polygonstolines", {'INPUT':layer,'OUTPUT':'TEMPORARY_OUTPUT'})
    point_layer = processing.run("native:extractvertices", {'INPUT':line_layer['OUTPUT'],'OUTPUT':'TEMPORARY_OUTPUT'})
    QgsProject.instance().addMapLayer(line_layer['OUTPUT'])

for point in point_layer['OUTPUT'].getFeatures():
    print(point.geometry().asPoint())