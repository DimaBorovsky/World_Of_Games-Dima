import zipfile
import os


files_to_zip = ['Utils.py','Scores.py','Main_Scores.py',]
zip_fileName = "World_of_Games_Level_3_.zip"


with zipfile.ZipFile(zip_fileName, 'w') as zipf:
    for file in files_to_zip:
        zipf.write(file)

print(f' Created {zip_fileName} with files :{files_to_zip}')