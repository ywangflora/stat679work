#!/usr/bin/env python

import re
import time
import sys
'''
import these two modulus to handle with time
'''
def openfile(waterfile,energyfile):
    '''
    the function takes two file names as arguments and create
    a csv file called 'output_hw2.csv' with the merged data.
    In the csv file, it contains all of the information in the
    temperature file and create new columns which match the energy
    value in the second file with the nearest waterTemperature value
    in the first file.
    '''
    with open(energyfile,"r") as eg:
      linelist = eg.readlines()
      i = 0
      list_date = []
      list_energy = []
      for line in linelist:
          i += 1
          if line.strip() and i > 1 and i < len(linelist)-1:
              strip_line = line.strip('\n')
              split_line = strip_line.split('-0500,')
              if re.findall(r'\s00:00:00\s',split_line[0]):  # check whether the time is 00:00:00
                  list_date.append(split_line[0])
                  list_energy.append(split_line[1])
              else:
                print('the time is not all 00:00:00')
      for i in range(len(list_date)-1):
          ldate_sp = list_date[i].split('-')
          if int(ldate_sp[0]) > int(ldate_sp[0]) or (int(ldate_sp[0]) == int(ldate_sp[0]) and int(ldate_sp[1]) > int(ldate_sp[1])) or (int(ldate_sp[0]) == int(ldate_sp[0]) and int(ldate_sp[1]) == int(ldate_sp[1]) and int(ldate_sp[2][:2]) > int(ldate_sp[2][:2])): # check the data are ordered
              print('the date is not ordered')
      for i in range(len(list_date)):
          list_date[i] = time.strptime(list_date[i],'%Y-%m-%d %H:%M:%S ') # change the energy time to strptime with time modulus
    with open(waterfile,'r') as wt:
        linewater = wt.readlines()
        i=0   # initial start index
        water_time = []
        water_time_normal = []
        water_value = []
        index = []
        for line in linewater:
             i += 1
             if line.strip() and i > 3:
                 strip_water = line.strip('\n')
                 split_water = strip_water.split(',')
                 water_time_normal.append(split_water[1])
                 split_water[1] = time.strptime(split_water[1],'%m/%d/%y %I:%M:%S %p') # change the waterTemperature time to strptime with time modulus
                 water_time.append(split_water[1])
                 water_value.append(split_water[2])
                 index.append(int(split_water[0]))
    match = ['']*len(water_time)  # no match initially(divided by 1000)
    match_1000 = ['']*len(water_time) # no match initially
    for i in range(len(list_date)): # energy time
        list_match = []
        for k in range(len(water_time)):
            list_match.append((time.mktime(list_date[i])-time.mktime(water_time[k])))  # use the difference to illustriate which time is the nearest one
        if max(list_match) < 0: # means that all the energy time is less than waterTemperature time
            pass
        else:
            value = min(j for j in list_match if j > 0) # choose the minimal positive value as the nearest one
            index_match = list_match.index(value)  # find the corresponding index
            match[index_match] = int(list_energy[i])/1000
            match_1000[index_match] = int(list_energy[i])

    with open('output_hw2.csv','w') as fh:
        fh.write(",".join(['"#"','"Date Time, GMT-05:00"','"K-Type, °F (LGR S/N: 10679014, SEN S/N: 10679014, LBL: water pipe)"','"Energy Produced (kWh)"','"Energy Produced (kWh)"/1000']))
        fh.write('\n')
    with open("output_hw2.csv", 'a') as fh: # write the ouput file 'output_hw2.csv'
        for k in range(len(index)):
            fh.write(str(index[k])+','+str(water_time_normal[k])+','+str(water_value[k])+','+ str(match_1000[k])+','+str(match[k]))
            fh.write('\n')

if __name__ == '__main__':
    openfile(sys.argv[1],sys.argv[2])
