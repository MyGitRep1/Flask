from datetime import time
from flask import Flask, g


app = Flask(__name__)

@app.before_request
def process_before_request():
    """
    Sets start_time to `g` object
    """
    g.start_time = time()
@app.after_request
def process_after_request(response):
    """
    adds process time in headers
    """
    if hasattr(g, "start_time"):
        response.headers["process-time"] = time() - g.start_time
    return response