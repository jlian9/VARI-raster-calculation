########################Search by Name##########################################################################################


import arcpy
import os
import matplotlib.pyplot as plt
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True
import statistics


#import skimage



arcpy.CheckOutExtension("Spatial")
#arcpy.env.workspace = r"E:\MODIS TEST\NDVI2017test"




###ET_List = [f for f in os.listdir(r'C:\Users\jw\Desktop\code test\Indices for real\ET projected') if f.endswith('Update.tif')]
####fileList = os.listdir(r"E:\MODIS TEST\NDVI2017test")
####outputFile = r"C:\Users\yzhong49\Desktop\NDVI_updated"

###print(ET_List)


###'''
######extract and convert the year(fireY) and day(fireD) to int type
####fireDate = '2017'+'159'
####fireY = int(fireDate[0:4])
####fireD = int(fireDate[4:7])
####print('the fire event is '+fireDate)




#####extract date and rename the output
####datecharacter = fileList[0][34:41]
####outputraster = 'updated_ndvi_'+ datecharacter
####print(outputraster)
###'''
###'''
###    #test fileList
###fileList= ['MOD13Q1.006__250m_16_days_NDVI_doy2017001_aid0001.tif',
###           'MOD13Q1.006__250m_16_days_NDVI_doy2017110_aid0001.tif',
###           'MOD13Q1.006__250m_16_days_NDVI_doy2017090_aid0001.tif',
###           'MOD13Q1.006__250m_16_days_NDVI_doy2017095_aid0001.tif',
###           'MOD13Q1.006__250m_16_days_NDVI_doy2017125_aid0001.tif',
###           'MOD13Q1.006__250m_16_days_NDVI_doy2017225_aid0001.tif']
###'''

###fireD = 24
###fireY = 2017
###tempET = []
####arcpy.env.workspace(r'C:\Users\jw\Desktop\code test\Indices for real\ET projected')

###for i in ET_List:  #loop through the ETfile list 
###    fileDateStr = i[23:30] # when i =0: "2016353"     '2017001'
###    fileDateNum = int(fileDateStr) #2016353           '2017001'
###    fileY = int(fileDateStr[0:4])#2016                '2017'
###    fileD = int(fileDateStr[4:7])#353                 '1'
   
#####get precondition period: 32 DAYS ahead of fire   
####no need to worry about leap year situation                  
###    if fireD > 32:                                              
###        day = fireD -32
###        year = fireY
###        #fireRange = str(year)+str(day)
###        #print(timePeriod)
###        #use file date comepare with timePeriod to get file fall into 32 range but 7 day(ET in this case) before fire date
###        if fileD > day and fileD <fireD-7:
###                print('This is the file within the range: ' + fileDateStr)
###                tempET.append(i)



####if the fire day is less than 32 it will deal with the leap year situation 
###    elif fireD < 32:
        
###        if fireY == 2001 or 2005 or 2009 or 2013 or 2017:                     #if the day is less than 32 and it is the next year of a leap year
###            rangeY = fireY -1                                                   #set the year back 1 year 
###            rangeD  = 366 - (32-fireD)                                           #leap year 366 days 
###            fireRange=str(rangeY)+str(rangeD )                                     #get 32 day ahead of fire date and creat new julian date
###        else:
###           rangeY = fireY -1                                        
###           rangeD = 365 - (32-fireD)                               
###           #fireRange = str(rangeY)+str(rangeD )      
           
                                   
###        if (fileY <= fireY) and (fileY >= rangeY):
###    #files 
###            if (fileY < fireY) and (fileY == rangeY):
###                if fileD > rangeD:
###                    print("this file is within the range, the file date is "+ fileDateStr)
###                    tempET.append(i)
###    #files that has the same year of fire                                               
###            elif (fileY == fireY) and (fileY > rangeY):
###                if fileD < fireD-7:
###                    print("this file is within the range and has the same year number of the fire event, file date is "+ fileDateStr)
###                    tempET.append(i)
###print(tempET)          
           
             
             
###'''

#####get precondition period: 30 DAYS ahead of filename                    
###    if fileD > 30:                                              
###        day = fileD -30
###        year = fileY
###        timePeriod = str(year)+str(day)
###    elif fileD < 30:

###        if fileY == 2001 or 2005 or 2009 or 2013 or 2017:                #if the day is less than 30 and it is the next year of a leap year
###            year = fileY -1                                              #set the year back 1 year 
###            day  = 366 - (30-fileD)                                      #leap year 366 days 
###            print(str(year)+str(day))                               #get 30 day ahead of fire date and creat new julian date
###        else:
###           year = fileY -1                                        
###           day = 365 - (30-fileD)                               
###           timePeriod = str(year)+str(day)                
###'''
####load files when data collection date is within that period
####fileY = 2016 (int)
####fireY = 2017 (str)
####timePeriod = 2016353 (str)






###########Scale Factor###############################################################################################################################
#import arcpy
#from arcpy import env
#from arcpy.sa import *
#import os

#arcpy.CheckOutExtension("Spatial")
#arcpy.env.workspace = r"C:\Users\jlian9\Desktop\2017NDVI RAW"

#flist = [f for f in os.listdir(r'D:\Fire data\parameter for real\2017NDVI') if f.endswith('.tif')]
##flist = os.listdir(r"C:\Users\jlian9\Desktop\2017NDVI RAW")

##print(flist, '\n')
#inConstant = 0.0001

#for i in flist:
#    print ('Working on:', i, '\n')
#    outTimes = Times(i,inConstant)
#    outTimes.save('MOD13Q1.006__250m_16_days_NDVI_doy'+i[34:41]+'_aid0001_Update.tif')
#    print (i + '  is done!\n')







###############Band calculate#####################################################################################################
import arcpy
from arcpy import env
from arcpy.sa import *
import os

arcpy.CheckOutExtension("Spatial")
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

