import json
import pandas as pd
import subprocess
import os

from sqlalchemy import create_engine

configobj = json.load(open("config/config.json"))

CSVPATH = configobj['dbpath']

command = 'heroku config:get DATABASE_URL'
heroku_pg = subprocess.check_output(command.split()).decode('utf-8')

engine = create_engine(heroku_pg)

df = pd.read_csv(CSVPATH)
df.to_sql(name='scorecard', index=False, if_exists='replace', con=engine)

