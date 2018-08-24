import geopandas as gpd

shape= gpd.read_file("input.dwg")
shape.head()
shape['Layer'].value_counts()
arr=shape['Layer'].unique()
arr

for i in arr:
    export=shape[(shape.Layer == i)]
    export.to_file(driver = 'ESRI Shapefile', filename= i+".shp")
