#!/usr/bin/python

import csv
import sys
import pandas as pd


def read_csv(fileName, data):
    with open(fileName, newline='') as f:
        newName = fileName.split("/")
        print(newName)
        reader = csv.reader(f)
        data = list(reader)

        headers = data.pop(0)
        headers.append("filename")
        for arr in data:
            arr.append(newName[2])
    return data, headers


def write_csv(data, col_names):
    df = pd.DataFrame(data, columns=col_names)
    df.to_csv('something.csv', index=False)


def combineCSV(csv_files, output_file):
    df_each_file = []
    for f in csv_files:
        file_name = f.split("/")[2]
        df = pd.read_csv(f, sep=',')
        df["filename"] = file_name
        df_each_file.append(df)

    frame = pd.concat(df_each_file, axis=0)
    frame.to_csv(output_file, index=False)


def main():
    csv_files = list(sys.argv)
    csv_files.pop(0)
    dest_file = csv_files.pop()
    combineCSV(csv_files, dest_file)

    # data = []
    # for f in csv_files:
    #     res = read_csv(f, data)
    #     write_csv(res[0], res[1])


if __name__ == "__main__":
    main()
