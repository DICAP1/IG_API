from flask import jsonify, request
from config import SYMBOLS_IGAPI


# ########################---IG API arguments ---####################



def get_igapiprice_query():
    """Check the price arguments"""

    types = ['bid', 'ask']
    query = {}

    # Get the instruments parameter from the request
    instruments = request.args.get('instruments')

    # Check if all instruments are included in the supported symbols
    if  'instruments' in request.args:
        if request.args.get('instruments') in SYMBOLS_IGAPI:
            query['instruments'] = instruments
    else:
        return {"error": "No instruments provided"}
    
    # Check if all instruments are included in the supported types
    if  'type' in request.args:
        if request.args.get('type') in types:
            query['type'] = request.args.get('type')  
            
    return query
