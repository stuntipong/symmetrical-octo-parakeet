'''
A script to simulate a population of objects surroundig M31
'''

import math
import random

def get_radec():
    '''Determine Andromeda location in ra/dec degrees from wikipedia'''
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees

    d, m, s = DEC.split(':')
    DEC = int(d)+int(m)/60+float(s)/3600

    h, m, sec = RA.split(':')
    RA = 15*(int(h)+int(m)/60+float(sec)/3600)
    RA = RA/math.cos(DEC*math.pi/180)
    
    return (RA,DEC)

def make_stars(RA,DEC,num_stars):
    '''make 1000 stars within 1 degree of Andromeda'''
    #num_stars = 1_000_000
    RAS = []
    DECS = []
    for i in range(num_stars):
        RAS.append(RA + random.uniform(-1,1))
        DECS.append(DEC + random.uniform(-1,1))
    return (RAS,DECS,num_stars)

def main():
    RA,DEC = get_radec()
    RAS,DECS,num_stars = make_stars(RA,DEC,num_stars)

    # now write these to a csv file for use by my other program
    with open('catalog.csv','w',encoding='utf-8') as F:
        print('id,ra,dec', file=F)
        for i in range(num_stars):
            print(f'{i:07d}, {RAS[i]:12f}, {DECS[i]:12f}', file=F)       

if __name__=='__main__':
    main()
            