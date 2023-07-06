from trading_ig import IGService
from config import IG_SERVICE_USERNAME, IG_SERVICE_PASSWORD, IG_SERVICE_API_KEY, IG_SERVICE_ACC_TYPE, IG_SERVICE_ACC_NUMBER
import time
from flask import jsonify

ig_service = IGService(IG_SERVICE_USERNAME, IG_SERVICE_PASSWORD, IG_SERVICE_API_KEY, IG_SERVICE_ACC_TYPE, IG_SERVICE_ACC_NUMBER)
ig_service.create_session()

def stream_candle_data(query):
    if isinstance(query, dict):  # Check if query is a dictionary
        epic = 'CS.D.' + query['instruments'] + '.MINI.IP'
        resolution = 'S'
        num_points = 1
        response = ig_service.fetch_historical_prices_by_epic_and_num_points(epic, resolution, num_points)
        df_ask = response['prices'][query['type']]
        data = df_ask.to_dict(orient='records')  # Convert DataFrame to dictionary
        print(data)
        return jsonify({"data": data})
    else:
        return jsonify({"error": "Invalid query"})

def run_stream_candle_data(query):
    while True:
        stream_candle_data(query)
        time.sleep(3)  # Delay for 3 seconds
