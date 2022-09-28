import csv
import os

rows = []
with open("metadata.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
# print(rows)


covid_19 = []
other_viral = []
bacteria = []
healthy = []

for row in rows:
    # print(row[4])
    if 'Pneumonia/Viral' in row[4]:
        if row[4] == 'Pneumonia/Viral/COVID-19':
            # print(row[23])
            covid_19.append(row[23])
        else:
            other_viral.append(row[23])
    elif 'Pneumonia/Bacterial' in row[4]:
        bacteria.append(row[23])
    elif 'No Finding' in row[4]:
        healthy.append(row[23])

# print(len(covid_19))
# print(len(other_viral))
# print(len(bacteria))
# print(len(healthy))

os.system('mkdir -p images_ok/viral/covid-19')
os.system('mkdir -p images_ok/viral/other')
os.system('mkdir -p images_ok/bacteria')
os.system('mkdir -p images_ok/healthy')

for img in covid_19:
    # print(img)
    os.system(f'cp images/{img} images_ok/viral/covid-19')

for img in other_viral:
    os.system(f'cp images/{img} images_ok/viral/other')

for img in bacteria:
    os.system(f'cp images/{img} images_ok/bacteria')

for img in healthy:
    os.system(f'cp images/{img} images_ok/healthy')

