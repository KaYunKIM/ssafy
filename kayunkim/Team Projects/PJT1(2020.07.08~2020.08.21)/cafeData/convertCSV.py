import pandas as pd
import os

cafelist = pd.read_excel(os.path.join(os.getcwd(), 'outputcafelist.xlsx'), encoding = "EUC-KR")
cafelist.to_csv(os.path.join(os.getcwd(), 'outputcafelist.csv'), index=False)