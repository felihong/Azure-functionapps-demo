import json
import logging 
import azure.functions as func 


# Helper function calculate fibonacci number 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

# Instantiate function blueprint class
# Using blueprints provides the benefits that:
#   - Break up the function app into modular components, which enables defining functions 
#     in multiple Python files and divide them into different components per file
#   - Provides extensible public function app interfaces to build and reuse the APIs
bp = func.Blueprint() 


# Function definition using HTTP trigger, and queue output binding
# Trigger and binding definitions are done via decorators
# Register the defined funtions to the blueprint object
# The functions registered in blueprint instances aren't indexed directly by the function runtime
@bp.function_name(name="FuncCalFibonacci")
@bp.route(route="calcFibonacci") 
@bp.queue_output(arg_name="msg", queue_name="webhookmsg",connection="AzureWebJobsStorage")
def call_fibonacci(
    req: func.HttpRequest,
    msg: func.Out[str]
): 
    # Get http request details including header, params and route params
    logging.info(dict(req.headers))
    logging.info(dict(req.params))
    logging.info(dict(req.route_params))
   
    # Function execution
    seed = int(req.params.get('seed'))
    if not seed:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            seed = int(req_body.get('seed'))
    if seed and seed > 0:
        result = fibonacci(seed)
        print(result)
        queue_msg = json.dumps({
            'seed': seed,
            'seed_fibonacci': result
        })
        msg.set(queue_msg)
        return func.HttpResponse(f"The Fibonacci number of {seed} is {result}")
    else:
        return func.HttpResponse(
            "Please pass a non-negative seed number",
            status_code=400
        )
    

@bp.function_name(name="FuncWebhook")
@bp.route(route="webhook") 
def call_webhook(
    req: func.HttpRequest
): 
    name = req.params.get('name')
    return func.HttpResponse(f"Say Hello to {name}")
