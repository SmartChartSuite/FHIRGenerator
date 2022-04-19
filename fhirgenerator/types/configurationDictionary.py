'''Model for Configuration Dictionary'''

import datetime

configuration_dictionary_template = {
    'numberPatients': 10,
    'ageMin': 0,
    'ageMax': 99,
    'genderMFOU': [47, 47, 1, 5],
    'startDate': datetime.datetime.today(),
    'days': 365,
    'outputFolder': 'output',
    'resourceDetails': {
        'fhirResource': 'Resource',
        'codesystem': '',
        'codes': '',
        'codesetURL': '',
        'minValue': 0,
        'maxValue': 10,
        'decimalValue': 1,
        'enumSetList': '',
        'minOccurancesPerCycle': 1,
        'maxOccurancesPerCycle': 1,
        'cycleLengthInDays': 365
    }
}
