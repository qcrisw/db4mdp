import csv
from dictionary import referencesdict
with open('references.csv', mode = 'w', newline = '') as file:
    csv_write = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for key, value in referencesdict.items():
        csv_write.writerow([value])
        
