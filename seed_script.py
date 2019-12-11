import csv
import json

from st_app1.models import Season, Episode, Company

# Seeding season from range to 0-7
for item in range(1,8):
    Season.objects.create(season_number=item)

# Seeding episode from range 1 to 30
for item in range(1,31):
    Episode.objects.create(episode_number=item)

CSV_PATH = 'data.csv'      # Csv file path

# script for dumping the data
with open(CSV_PATH, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if row[0] == "Row":
            continue
        else:
            Company.objects.create(season=Season.objects.get(season_number=int(row[1])),episode=Episode.objects.get(episode_number=int(row[2])),company=row[3].upper()
                                ,deal=row[4],industry=row[5],gender=row[6]
                                ,amount=row[7],equity=row[8], valuation=row[9])
