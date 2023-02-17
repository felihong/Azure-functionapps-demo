import logging
import json
import azure.functions as func


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Entry function triggered by HTTP request. Based on seed number parameter the Fibonacci value is calculated.
Configuration details:
{
    "name": the variable name used in function code for the request or request body
    "type": type of the trigger, here is httpTrigger
    "direction": must be set as in
    "authLevel": determines what keys, if any, need to be present on the request in order to invoke the function, including
                - anonymous: no API key is required
                - function: function-specific API key is required, is the default value
                - admin: master key is required.
    "methods": array of the HTTP methods to which the function responds. If not specified, the function responds to all HTTP methods
    "route": the route template, controlling to which request URLs the function responds. The default value if none is provided is <functionname>
}
"""
def reqHandler(
    # Input binding HTTP request
    req: func.HttpRequest, 
    # Output binding queue message
    msg: func.Out[str]
):
    # Get request headers
    logging.info(dict(req.headers))
    # Get request parameters
    logging.info(dict(req.params))
    # Get route parameters
    logging.info(dict(req.route_params))
    # Get request body, in not None
    try:
        logging.info(req.get_json())
    except ValueError: 
        pass
   
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
