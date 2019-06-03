import arcpy
import os
import matplotlib.pyplot as plt
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import statistics



arcpy.CheckOutExtension("Spatial")




###############Band calculate#####################################################################################################

arcpy.env.workspace = r"D:\Fire data\MODIS Band 134"

VARIlist = [f for f in os.listdir(r'D:\Fire data\MODIS Band 134') if f.endswith('update.tif')]

#print(VARIlist)

#flist=['MYD09A1.006_sur_refl_b01_doy2016361_aid0001.tif','MYD09A1.006_sur_refl_b01_doy2017001_aid0001.tif','MYD09A1.006_sur_refl_b01_doy2017009_aid0001.tif',
#       'MYD09A1.006_sur_refl_b03_doy2016361_aid0001.tif','MYD09A1.006_sur_refl_b03_doy2017001_aid0001.tif','MYD09A1.006_sur_refl_b03_doy2017009_aid0001.tif',
#       'MYD09A1.006_sur_refl_b04_doy2016361_aid0001.tif','MYD09A1.006_sur_refl_b04_doy2017001_aid0001.tif','MYD09A1.006_sur_refl_b04_doy2017009_aid0001.tif']

##find unique id 1
print(VARIlist[0][23])


###use raster b01 as the indicator and then excute the corespond b03 and b04

Band1 = [ ]
Band3 = [ ]
Band4 = [ ] 




for b1 in VARIlist:
    if b1[23] == "1":
        Band1.append(b1)
        b3=b1.replace('b01','b03')
        
        b4=b1.replace('b01','b04')

        Band3.append(b3)
        Band4.append(b4)

#print(Band1)
#print('=======================\n')
#print(Band3)
#print('=======================\n')
#print(Band4)
fileNum = len(Band1)
print(fileNum)

for i in range(fileNum):
    print('now is working on: '+ Band1[i])
    outVARI= (Raster(Band4[i])-Raster(Band1[i]))/(Raster(Band4[i])+Raster(Band1[i])-Raster(Band3[i]))
    outVARI.save('MYD09A1.006_sur_refl_doy'+Band1[i][28:35]+'_VARI.tif')

