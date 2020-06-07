#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# FEATURES write csv file
import csv

# Prepare some data, table of second powers
data = []
for i in range(0, 21):
    data.append((i, i*i))

# Print the table
print(data)

# Write to file
with open("out.csv", "w", newline="") as file:
    # Attach writer to file
    writer = csv.writer(file, delimiter=",")

    # Write header
    writer.writerow(["number", "second power"])

    # Write data
    writer.writerows(data)
