# import pydevd_pycharm
# pydevd_pycharm.settrace('localhost', port=9000, stdoutToServer=True, stderrToServer=True)

import azure.functions as func
import logging


app = func.FunctionApp()


@app.function_name(name="hello_world")
@app.route(route="hello", methods=["POST"])
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    input = req.get_json()
    name = input.get("name", "Anonymous")
    return func.HttpResponse(f"Hello {name}")


@app.function_name(name="hello_world_2")
@app.route(route="hi")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("Hi there")