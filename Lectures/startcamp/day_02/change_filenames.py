#change_filenames.py
import os

os.chdir(r'C:\Users\multicampus\Desktop\startcamp\day_02\dummy')

filenames= os.listdir('.')

for filename in filenames:
    os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))
