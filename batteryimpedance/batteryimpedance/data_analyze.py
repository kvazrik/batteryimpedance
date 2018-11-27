#!/usr/bin/env python3
"""
data_proc.py
Demo including:
 - calculating the value of resistance from real and imaginary impedance

"""

from __future__ import print_function

import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import unittest
import sys
import argparse
import csv

def parse_cmdline(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-csvx','--cy',help="CSV for x",default='./examplex.csv')
    parser.add_argument('-csvy','--cx',help="CSV for y",default='./exampley.csv')
    args = parser.parse_args(argv)
    return args







def main(argv=None):

    args = parse_cmdline(argv)

    with open(args.cx) as csv_file:
        x = csv.reader(csv_file, delimiter=',')
        with open(args.cy) as csv_file:
            y = csv.reader(csv_file, delimiter=',')

    x=np.array([433.423,562.348,741.577,970.963,1250.75,1627.3,2112.36,2737.54,3505.53,4402.29,5407.68,6595.4,7903.34,9288.42,10595.9,11875.2,13051.2,14095.9,14996.1,15751.2,16399.8,
                16953.2,17545.1,17890,18174.1,18406.4,18601.5,18762.8])

    y=np.array([2016.51,2379.17,2794.77,3274.21,3741.11,4300.92,4914.52,5567.32,6191.53,6836.66,7332.8,7738.45,8006.77,8153.99,8146.8,7912.64,7530.77,7038.14,6480.49,5872.9,5252.28,
                4671.26,4101.98,3632.87,3203.64,2815.86,2472.12,2166.68])

    xx=np.multiply(x, x)
    yy=np.multiply(y, y)
    xy=np.multiply(x, y)
    n=x.size
    A=np.array([[np.sum(x),np.sum(y),n],[np.sum(xy),np.sum(yy),np.sum(y)],[np.sum(xx),np.sum(xy),np.sum(x)]])
    B=np.array([[np.sum(xx+yy)],[np.sum(xx*y+yy*y)],[np.sum(xx*x+xy*y)]])
    a=np.linalg.solve(A, B)
    R=np.sqrt((a.item(0)**2 + a.item(1)**2)*0.25 - a.item(2))
    plt.plot(x, y)
    plt.xlabel('Z (ohms)')
    plt.ylabel('Z''(ohms)')
    plt.title('Nyquist plot of the impedance spectra')
    plt.grid(True)
    plt.show()
    print("R=", R)

    return R




if __name__ == "__main__":
    status = main()



