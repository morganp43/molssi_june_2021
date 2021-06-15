# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 14:04:16 2021

@author: Morgan
"""

import os,numpy,argparse

def dist(coords1,coords2): #when designing functions, aim for simple inputs and simple outputs
    value = numpy.sqrt( (coords1[0]-coords2[0])**2 + (coords1[1]-coords2[1])**2 + (coords1[2]-coords2[2])**2 )
    return value

def bond_check(atom_distance,mind=0.0,maxd=1.5): #variables with default values MUST come after those with no defaults
    """
    This function checks if a distance is a bond based on a minimum and maximum.
    Inputs: distance, minimum length, maximum length
    Defaults: minimum: 0.0 angstroms, maximum: 1.5 angstroms
    """
    if atom_distance <= maxd and atom_distance > mind:
        return True
    else:
        return False
    
def open_xyz(file_path):
    """
    Opens a standard xyz file.
    Returns the symbols as a 1D array of strings and the coords as a 2D array of floats.
    """
    all_data = numpy.genfromtxt(fname=file_path,dtype='unicode',skip_header=2) #don't need delimiter, because breaking on blank space is the default
    atom_label = all_data[:,0] #all rows, first col
    atom_coords = all_data[:,1:4].astype(float) #get float array of coords
    return atom_label,atom_coords

if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description="This script analyzes a user-given xyz file and outputs the length of all relevant bonds.") #turns on parser
    parser.add_argument('xyz_file',help='The filepath of the xyz file to analyze.') #tells parser what the arguments will be
    args = parser.parse_args() #tells parser to get the arguments from the command line
    
    file_location = args.xyz_file
    label,coords = open_xyz(file_location)
    
    num_atoms = len(label)
    
    for i in range(0,num_atoms):
        for j in range(0,i):
            dist_val = dist(coords[i],coords[j])
            if bond_check(dist_val) is True: 
                print(F'{label[j]}-{label[i]:4} : {dist_val:.3f}')