

def get_all_providers():
    return PROVIDERS

def get_provider(id):
    for p in PROVIDERS:
        if p['id'] == id:
            return p

def get_programs_for_provider(provider_id):
    return [11,12,13,14,15]

def get_outcomes_for_program(provider_id, program_id):
    return {'individuals': 123, 'grad_rate': .8, 'median_income': 32000}
