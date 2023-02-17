import json
import azure.functions as func
import logging


"""
Entry function triggered by HTTP request. Given a product ID the product information is retrieved from Table storage.
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
    req: func.HttpRequest, 
    productsJSON
):
    message = json.loads(productsJSON)
    return func.HttpResponse(f"Product table row: {productsJSON}")