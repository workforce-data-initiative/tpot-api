from __future__ import division

import random
from collections import OrderedDict

import numpy as np
import pandas as pd
from faker import Faker

def generate(n):
    """
    generates at least "n" of entries
    """
    fake = Faker()

    d = OrderedDict()
    d['provider_name'] = []
    d['provider_id'] = []
    d['provider_type'] = []
    d['program_type'] = []
    d['program_cip'] = []
    d['reporting_period'] = []
    d['all_served'] = []
    d['all_exited'] = []
    d['wioa_served'] = []
    d['wioa_exited'] = []
    d['wioa_ita_served'] = []
    d['wioa_ita_exited'] = []
    d['all_completed'] = []
    d['wioa_completed'] = []
    d['all_employed_2q'] = []
    d['all_employed_4q'] = []
    d['all_median_earnings'] = []
    d['all_obtained_credential'] = []
    d['wioa_obtained_credential'] = []
    d['nonwioa_employed_2q'] = []
    d['nonwioa_employed_4q'] = []
    d['nonwioa_median_earnings'] = []
    d['nonwioa_credential_rate_num'] = []
    d['nonwioa_credential_rate_den'] = []
    d['cost_per_wioa_participant'] = []
    # TODO: Total # of WIOA participants served disaggregated by characteristics 
    # TODO: Total # of WIOA participants served disaggregated by barriers to employment 
    
    total = 0
    id = 1
    while total < n:
        name = (fake.last_name() + " " + 
                np.random.choice(["School","Institute","College","University"]))
        provider_id = id
        id += 1
        typ = random.randint(0,8)
        # Generate a random number of programs for the school
        for _ in range(int(random.expovariate(1/10)+1)):
            prog = random.randint(0,9)
            cip = random.randint(1000,9999)
            # And a random number of reporting periods for the given program:
            for year in np.unique(np.random.choice(range(2014,2017), 3)):
                total = total+1
                d['provider_name'].append(name)
                d['provider_id'].append(id)
                d['provider_type'].append(typ)
                d['program_type'].append(prog)
                d['program_cip'].append(cip)
                d['reporting_period'].append(year)

                d['all_served'].append(int(random.expovariate(1/100)+1))
                d['all_exited'].append(int(d['all_served'][-1] * (random.random()+1)/2))
                
                d['wioa_served'].append(int(d['all_served'][-1] * (random.random()+1)/2))
                d['wioa_exited'].append(int(min(d['wioa_served'][-1],d['all_exited'][-1]) * (random.random()+1)/2))
                d['wioa_ita_served'].append(int(d['wioa_served'][-1] * (random.random()+1)/2))
                d['wioa_ita_exited'].append(int(min(d['wioa_ita_served'][-1],d['wioa_exited'][-1]) * (random.random()+1)/2))
                d['all_completed'].append(int(d['all_exited'][-1] * (random.random()+1)/2))
                d['wioa_completed'].append(int(d['wioa_exited'][-1] * (random.random()+1)/2))

                d['all_employed_2q'].append(int(d['all_served'][-1] * (random.random()+1)/2))
                d['all_employed_4q'].append(int(d['all_served'][-1] * (random.random()+1)/2))
                d['all_median_earnings'].append(random.randint(10000,100000))

                d['all_obtained_credential'].append(int(d['all_completed'][-1] * (random.random()+1)/2))
                d['wioa_obtained_credential'].append(int(d['wioa_completed'][-1] * (random.random()+1)/2))
                d['nonwioa_employed_2q'].append(int((d['all_exited'][-1]-d['wioa_exited'][-1]) * (random.random()+1)/2))
                d['nonwioa_employed_4q'].append(int((d['all_exited'][-1]-d['wioa_exited'][-1]) * (random.random()+1)/2))
                d['nonwioa_median_earnings'].append(random.randint(10000,100000))
                d['nonwioa_credential_rate_den'].append(int((d['all_exited'][-1]-d['wioa_exited'][-1]) * (random.random()+1)/2))
                d['nonwioa_credential_rate_num'].append(int(d['nonwioa_credential_rate_den'][-1] * (random.random()+1)/2))
                d['cost_per_wioa_participant'].append(random.randint(200,20000))
    return pd.DataFrame(d)

if __name__ == '__main__':
    df = generate(200)
    df.to_csv('example_data.csv', index=False)
