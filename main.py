import pandas as pd
import glob, os
 
os.chdir("data")
colnames = ["Trip Duration","Start Time","Stop Time", "Start Station ID","Start Station Name","Start Station Latitude", "Start Station Longitude", "End Station ID","End Station Name","End Station Latitude", "End Station Longitude","Bike ID", "User Type", "Birth Year", "Gender"]
results = pd.DataFrame([])

for counter, file in enumerate(glob.glob("*.csv")):
    namedf = pd.read_csv(file, skiprows=1, header=None)
    results = results.append(namedf)
results.columns = colnames
results.to_csv('../bike.csv',index=None)