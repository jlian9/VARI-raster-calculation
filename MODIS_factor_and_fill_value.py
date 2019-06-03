import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
#arcpy.env.workspace = r"D:\Fire data\ET Factor and fill value"

#flist = [f for f in os.listdir(r'D:\Fire data\NDVI Factor and fill value') if f.endswith('.tif')]

###########NDVI 
#inConstant = 0.0001
#for i in flist:
#    print ('Working on:', i, '\n')
#    ExtractByAttributes(i,'VALUE>= -2000 and VALUE<=10000' ) 
#    outTimes = Times(i,inConstant)
#    outTimes.save('MOD13Q1.006__250m_16_days_NDVI_doy'+i[34:41]+'_aid0001_update.tif')
#    print (i + '  is done!\n')



###########ET
##arcpy.env.workspace = r"D:\Fire data\ET Factor and fill value"
##flist = [f for f in os.listdir(r'D:\Fire data\ET Factor and fill value') if f.endswith('.tif')]
##inConstant = 0.1
##for i in flist:
##    print('working on: '+i[23:30])
##    inRaster = ExtractByAttributes(i,'VALUE>= -32767 and VALUE<=32700' ) 
##    outTimes = Times(inRaster,inConstant)
##    outTimes.save('MOD16A2.006_ET_500m_doy'+i[23:30]+'_aid0001_update.tif')
    

##############EVI
#arcpy.env.workspace = r"D:\Fire data\LAI Factor and fill value"
#flist = [f for f in os.listdir(r'D:\Fire data\EVI Factor and fill value') if f.endswith('.tif')]

#inConstant = 0.0001
#for i in flist:
#    print('working on: '+i[33:40])
#    inRaster = ExtractByAttributes(i,'VALUE>= -2000 and VALUE<=10000' ) 
#    outTimes = Times(inRaster,inConstant)
#    outTimes.save('MOD13Q1.006__250m_16_days_EVI_doy'+i[33:40]+'_aid0001_update.tif')





################LAI
#arcpy.env.workspace = r"D:\Fire data\LAI Factor and fill value"

#flist = [f for f in os.listdir(r'D:\Fire data\LAI Factor and fill value') if f.endswith('.tif')]
#inConstant = 0.01
#for i in flist:
#    print('working on: '+i[25:32])
#    inRaster = ExtractByAttributes(i,'VALUE>= 0 and VALUE<=100' ) 
#    outTimes = Times(inRaster,inConstant)
#    outTimes.save('MCD15A2H.006_Lai_500m_doy'+i[25:32]+'_aid0001_update.tif')


################VARI
##inConstant = 0.1
##for i in flist:
##    print('working on: '+i[33:40])
##    inRaster = ExtractByAttributes(i,'VALUE>= -32767 and VALUE<=32700' ) 
##    outTimes = Times(inRaster,inConstant)
##    outTimes.save('MOD13Q1.006__250m_16_days_EVI_doy'+i[33:40]+'_aid0001_update.tif')


#############MODIS RC band 1
#arcpy.env.workspace = r"D:\Fire data\MODIS Band1"
#flist = [f for f in os.listdir(r'D:\Fire data\MODIS Band1') if f.endswith('.tif')]

#inConstant = 0.0001
#for i in flist:
#    print('working on: '+i[28:35])
#    inRaster = ExtractByAttributes(i,'VALUE>= -100 and VALUE<=16000' ) 
#    outTimes = Times(inRaster,inConstant)
#    outTimes.save('MYD09A1.006_sur_refl_b01_doy'+i[28:35]+'_aid0001_update.tif')



################MODIS RC band 3
#arcpy.env.workspace = r"D:\Fire data\MODIS Band3"
#flist = [f for f in os.listdir(r'D:\Fire data\MODIS Band3') if f.endswith('.tif')]

#inConstant = 0.0001
#for i in flist:
#    print('working on: '+i[28:35])
#    inRaster = ExtractByAttributes(i,'VALUE>= -100 and VALUE<=16000' ) 
#    outTimes = Times(inRaster,inConstant)
#    outTimes.save('MYD09A1.006_sur_refl_b03_doy'+i[28:35]+'_aid0001_update.tif')

################MODIS RC band 4
#arcpy.env.workspace = r"D:\Fire data\MODIS Band4"
#flist = [f for f in os.listdir(r'D:\Fire data\MODIS Band4') if f.endswith('.tif')]

#inConstant = 0.0001
#for i in flist:
#    print('working on: '+i[28:35])
#    inRaster = ExtractByAttributes(i,'VALUE>= -100 and VALUE<=16000' ) 
#    outTimes = Times(inRaster,inConstant)
#    outTimes.save('MYD09A1.006_sur_refl_b04_doy'+i[28:35]+'_aid0001_update.tif')


print(int(15/30))