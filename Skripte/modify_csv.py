import os
import csv
import pandas as pd

columns = 15

input_path = "/home/nru/Documents/BMS/IDPA/Auto/Experiment/Messwerte/Original/"
output_path = "/home/nru/Documents/BMS/IDPA/Auto/Experiment/Messwerte/Angepasst/"

files = os.listdir(input_path)

for input_file in files:
    with open(input_path + input_file, newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open("temp.csv",'w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'])
        w.writerows(data)

    df = pd.read_csv("temp.csv")
    raw = pd.DataFrame()

    for x in range(1, columns+1):
        y = str(x)
        new_df = df[y].dropna(axis='index')
        new_df = new_df.reset_index(drop=bool)
        raw[y] = new_df

    raw.to_csv("temp.csv", index=False)

    with open("temp.csv") as f:
        lines = list(f)
        lines.pop(0)

        with open("temp.csv", "w") as f:
            for line in lines:
                f.write(line)

    with open("temp.csv", 'r', newline='') as in_file, open(output_path + "modified_" + input_file, 'w', newline='') as out_file:
            reader = csv.reader(in_file)
            writer = csv.writer(out_file)
            for row in reader:
                if row:
                    new_row = row[1:]
                    writer.writerow(new_row)

    os.remove("temp.csv")