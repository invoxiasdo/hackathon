#! /usr/bin/env python3

"""
Script extract infos from data/lwt1_data.csv or data/lwt2_data.csv
"""

import pandas as pd
import argparse





if __name__ == "__main__":
    # run as command line
    parser = argparse.ArgumentParser(description='''Projet of the winning team''', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-f", "--data-file", required=True, help = 'data file => data/lwt1_data.csv or data/lwt2_data.csv')
    args = parser.parse_args()

    cols = ['serial', 'date', 'latitude', 'longitude', 'accuracy', 'method', 'battery']
    dtf = pd.read_csv(args.data_file, sep=';', names=cols, header=0)
    dtf.date = pd.to_datetime(dtf.date)
    print(dtf)
