import json
import pandas as pd
from etp_api import db

configobj = json.load(open("config/config.json"))

CSVPATH = configobj['dbpath']

df = pd.read_csv(CSVPATH)
df.to_sql(name='scorecard', index=False, if_exists='replace', con=db.engine)
