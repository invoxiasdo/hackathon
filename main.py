#! /usr/bin/env python3

"""
Script extract infos from data/lwt1.csv or data/lwt2.csv
"""

import pandas as pd
import argparse





if __name__ == "__main__":
    # run as command line
    parser = argparse.ArgumentParser(description='''Projet of the winning team''', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", "--data-file", required=True, help = 'data file => data/lwt1.csv or data/lwt2.csv')
    args = parser.parse_args()

    dtf = pd.read_csv(args.data_file, sep=';')
    print(dtf)
