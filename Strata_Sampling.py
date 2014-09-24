##Strata_Sampling=name
##IFWPPS=group
##Input_Strata=raster
##Number_of_Samples=number 100
##Output_Samples=output vector 

import processing
from osgeo import gdal
from osgeo import ogr
from osgeo import osr
import numpy as np
from scipy.stats import itemfreq
progress.setText("Import complete")

def random_stratified(image, classes, counts):
    """
    Return pixel strata, row, column from within image from a random stratified
    sample of classes specified

    Args:
        image (ndarray)         input map image
        classes (ndarray)       map image classes to be sampled
        counts (ndarray)        map image class sample counts

    Return:
        (strata, col, row)      tuple of ndarrays
    """
    # Initialize outputs
    strata = np.array([])
    rows = np.array([])
    cols = np.array([])

    progress.setText('Performing sampling')

    for c, n in zip(classes, counts):
        progress.setText('Sampling class {c}'.format(c=c))

        # Find pixels containing class c
        row, col = np.where(image == c)

        # Check for sample size > population size
        if n > col.size:
            progress.setText(
                'Class {0} sample size larger than population'.format(c))
            progress.setText('Reducing sample count to size of population')

            n = col.size

        # Randomly sample x / y without replacement
        # NOTE: np.random.choice new to 1.7.0...
        # TODO: check requirement and provide replacement
        samples = np.random.choice(col.size, n, replace=False)

        progress.setText('    collected samples')

        strata = np.append(strata, np.repeat(c, n))
        rows = np.append(rows, row[samples])
        cols = np.append(cols, col[samples])

    return (strata, cols, rows)
    
    
def write_vector_output(strata, cols, rows, map_ds, output,
                        ogr_frmt='ESRI Shapefile'):
    """
    """
    # Corners of pixel in pixel coordinates
    corners = [(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]

    # Raster geo-transform
    gt = map_ds.GetGeoTransform()
    # Get OSR spatial reference from raster to give to OGR dataset
    map_sr = osr.SpatialReference()
    map_sr.ImportFromWkt(map_ds.GetProjectionRef())

    # Get OGR driver
    driver = ogr.GetDriverByName(ogr_frmt)
    # Create OGR dataset and layer
    sample_ds = driver.CreateDataSource(output)
    layer = sample_ds.CreateLayer('sample', map_sr, geom_type=ogr.wkbPolygon)

    # Add fields for layer
    # Sample ID field
    layer.CreateField(ogr.FieldDefn('ID', ogr.OFTInteger))
    # Row/Col fields
    layer.CreateField(ogr.FieldDefn('ROW', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('COL', ogr.OFTInteger))
    # Strata field
    layer.CreateField(ogr.FieldDefn('STRATUM', ogr.OFTInteger))

    # Loop through samples adding to layer
    for i, (stratum, col, row) in enumerate(zip(strata, cols, rows)):
        # Feature
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetField('ID', i)
        feature.SetField('ROW', row)
        feature.SetField('COL', col)
        feature.SetField('STRATUM', stratum)

        # Geometry
        ring = ogr.Geometry(type=ogr.wkbLinearRing)

        for corner in corners:
            ring.AddPoint(
                gt[0] + (col + corner[0]) * gt[1] + (row + corner[1]) * gt[2],
                gt[3] + (col + corner[1]) * gt[4] + (row + corner[1]) * gt[5])
        square = ogr.Geometry(type=ogr.wkbPolygon)
        square.AddGeometry(ring)

        feature.SetGeometry(square)

        layer.CreateFeature(feature)

        feature.Destroy()

    sample_ds = None    



map_ds = gdal.Open(Input_Strata)
band = map_ds.GetRasterBand(1)
data = band.ReadAsArray()
freq = itemfreq(data)
classes = freq[1:,0]

#have to allot 5 samples to each class
#hence reducing number of samples 
Final_Number_of_Samples = Number_of_Samples - 5*len(classes)
sample_pts = np.zeros(len(classes))+5
if Final_Number_of_Samples > 0:
	sample_pts += np.floor(freq[1:,1] * Final_Number_of_Samples / np.sum(freq[1:,1]))

#will create atleast 5 samples for each class 
#might compensate due to over crowding	
strata, cols, rows = random_stratified(data, classes, sample_pts)
progress.setText("Sampling complete")
write_vector_output(strata, cols, rows, map_ds, Output_Samples)
progress.setText("Write complete")

