#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES reading CSV file using csv package, direct iteration, store data, access as dictionary
import csv

###########################################
# A. Read data directly using an iterator #
###########################################
# Open source CSV file
with open("sample.csv") as file:
    # Attach CSV reader to it
    reader = csv.reader(file, delimiter=',', dialect=csv.excel)

    # Access all rows
    # csv is an iterator, cannot access n-th line directly
    for row in reader:
        print(row)


############################################
# B. Read data into list, process it later #
############################################
# Open source CSV file
with open("sample.csv") as file:
    # Attach CSV reader to it
    reader = csv.reader(file, delimiter=',', dialect=csv.excel)

    # Store data in list, this consumes possibly lot of RAM to store the data
    data = list(reader)

    # Access the data as list of lists
    print(data)

    # Access data at particular position, [row][column]
    print(data[5][1])

    # Re-order data so that columns are contained in separated lists
    tdata = list(zip(*data))
    print(tdata)

    # Access column
    print(tdata[1])

    # Access data at particular position [column][row]
    print(tdata[1][5])


##############################
# C. Read data as dictionary #
##############################
# Open source CSV file
with open("sample.csv") as file:
    # Attach CSV dictionary reader to it
    # As "fieldnames" are not defined, first line will be used as filed names
    reader = csv.DictReader(file, delimiter=',', dialect="excel")

    # Iterate over lines represented as ordered dictionaries
    for row in reader:
        print("Row:")
        for key, value in row.items():
            print(f" {key}:{value}")
