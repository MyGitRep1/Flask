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

# Process unhandled zero division error
#    [log]: ERROR in app: Here's traceback for zero division error
#        Traceback (most recent call last):
#          File "/usr/lib/python3.9/site-packages/flask/app.py", line 1950, in
# full_dispatch_request
#            rv = self.dispatch_request()
#          File "/usr/lib/python3.9/site-packages/flask/app.py", line 1936, in
# dispatch_request
#            return self.view_functions[rule.endpoint](**req.view_args)
#         File "/apps/flask-lesson/blog/app.py", line 155, in do_zero_division
#           return 1 / 0
#        ZeroDivisionError: division by zero
