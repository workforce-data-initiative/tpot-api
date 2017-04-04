import itertools
from etp_api import db

def get_all_providers():
    r = db.engine.execute("SELECT DISTINCT provider_id, provider_name, provider_type FROM scorecard")
    vals = r.fetchall()
    return list(map(dict, vals))

def get_provider(id):
    r = db.engine.execute("SELECT DISTINCT provider_id, provider_name, provider_type FROM scorecard WHERE provider_id=%d" % provider_id)
    vals = r.fetchall()
    return list(map(dict, vals))

def get_programs_for_provider(provider_id):
    r = db.engine.execute("SELECT DISTINCT program_cip, program_type FROM scorecard WHERE provider_id=%d" % provider_id)
    vals = r.fetchall()
    return list(itertools.chain(*vals))

def get_outcomes_for_program(provider_id, program_id):
    r = db.engine.execute("SELECT * FROM scorecard WHERE provider_id=%d and program_cip=program_id" % (provider_id, program_id))
    vals = r.fetchall()
    return list(map(dict, vals))
