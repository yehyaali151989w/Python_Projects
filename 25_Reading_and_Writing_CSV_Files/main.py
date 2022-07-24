# writing a csv file
import csv
import pandas as pd

data = {"Name": ["Aman", "Diksha", "Akanksha", "Sajid", "Akshit"],
        "Age": [23, 21, 25, 23, 22]}

data = pd.DataFrame(data)
data.to_csv(
    r"D:\Python_Prpjects\25_Reading_and_Writing_CSV_Files\age_data.csv", index=False)
print(data.head())

# reading a csv file
data = pd.read_csv(
    r"D:\Python_Prpjects\25_Reading_and_Writing_CSV_Files\age_data.csv")
print(data.head())
