from flask import Flask
from .APIs.check import get_igapiprice_query
from .APIs.ig_api import run_stream_candle_data

app = Flask(__name__)

##################################-----IG API-------#######################################################

# candle chart data
@app.route('/igapicandlechart', methods=['GET'])
def igapicandlechart(): 
    if "error" in get_igapiprice_query():
        return get_igapiprice_query()
    else:
        run_stream_candle_data(get_igapiprice_query())


# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()
