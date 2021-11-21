resized_pole = processing.run("shapetools:geodesictransformations", {'INPUT':'D:/С диска C/Хакатон/Pole.dbf|layername=Pole','TransformRotation':0,'TransformScale':0.8,'TransformDistance':0,'TransformAzimuth':0,'TransformUnits':0,'OUTPUT':'TEMPORARY_OUTPUT'})

layer = resized_pole['OUTPUT']

line_layer = processing.run("native:polygonstolines", {'INPUT':layer,'OUTPUT':'TEMPORARY_OUTPUT'})
QgsProject.instance().addMapLayer(line_layer['OUTPUT'])

layer=processing.run("native:pointsalonglines", {'INPUT':line_layer['OUTPUT'],'DISTANCE':0.0005,'START_OFFSET':0,'END_OFFSET':0,'OUTPUT':'TEMPORARY_OUTPUT'})
QgsProject.instance().addMapLayer(layer['OUTPUT'])
layer = iface.activeLayer()
features = layer.getFeatures()
#start_point = QgsPointXY(float(input()),float(input()))
points = []
for i, feature in enumerate(features):
    geom = feature.geometry()
    x = geom.asPoint()
    points.append(x)
line = []
for i in range(points.__len__()//2-1):
    if i%2 == 0:
        line.append(points[i])
        line.append(points[-i-1])
    else:
        line.append(points[-i-1])
        line.append(points[i])
vl = QgsVectorLayer("MultiLineString", "path", "memory")
pr = vl.dataProvider()

f = QgsFeature()

f.setGeometry(QgsGeometry.fromPolylineXY(line))
pr.addFeature(f)
vl.updateExtents()
QgsProject.instance().addMapLayer(vl)