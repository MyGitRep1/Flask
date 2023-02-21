from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route("/divide-by-zero/")
def do_zero_division():
    return 1 / 0
@app.errorhandler(ZeroDivisionError)
def handle_zero_division_error(error):
    print(error) # prints str version of error: 'division by zero'
    app.logger.exception("Here's traceback for zero division error")
    return "Never divide by zero!", 400


# < HTTP/1.0 400 BAD REQUEST
# - Never divide by zero!
