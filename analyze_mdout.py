# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:00:06 2021

@author: Morgan
"""

import argparse,os

if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description="This script analyzes a user-given outfile from Amber and outputs all Etot values.") #turns on parser
    parser.add_argument('out_file',help='The filepath of the Amber output file to analyze.') #tells parser what the arguments will be
    args = parser.parse_args() #tells parser to get the arguments from the command line 
    file_location = args.out_file

#filename = os.path.join('data','03_Prod.mdout')
with open(file_location) as f: #automatically closes file when done. default is to read
    data = f.readlines()

basename = os.path.basename(file_location).split('.')[0]

with open(F'{basename}_Etot.txt','w') as output: #opening file for writing
    output.write('Homework3\n\n')

all_ener = [] #grabbing all Etot values and putting in list
for line in data:
    if 'Etot' in line:
        all_ener.append(line.split()[2])

ener = all_ener[0:len(all_ener)-2] #slice data, remove last two statistical values (not needed)
        
count = 1
for val in ener:
    with open(F'{basename}_Etot.txt','a') as output:
        output.write(F'{count:3} : {val}\n')
    count += 1