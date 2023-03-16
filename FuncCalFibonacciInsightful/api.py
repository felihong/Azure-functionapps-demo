import json
import azure.functions as func
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.extension.azure.functions import OpenCensusExtension
OpenCensusExtension.configure()


# Initizalie logger instance and instantiate the exporters 
# So that telemetry data are sent to Application Insights
# Set empty param force using default instrumentation key
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler())
# The root logger is configured with the level of warning
# All levels with less severity are ignored and won't be sent to Azure Monitor
# Levels include:
# - CRITICAL (4)
# - ERROR (3)
# - WARNING (2)
# - INFO (1)
# - DEBUG, Verbose(0)

# Can be overwritten like below
logger.setLevel(logging.INFO)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


"""
Loggings with different msgs to be processed and sent to Azure Monitor:
    - logger.info()
    - logger.exception()
    - logger.warning()
"""
def main(req: func.HttpRequest, msg: func.Out[str]):
    # Add custom properties log messages in the <extra> keyword argument using the custom_dimensions field
    # These properties appear as key-value pairs in customDimensions in Azure Monitor
    # Only dictionary data type is handled, any other types will be ignored by logger
    req_properties = {'custom_dimensions': {
        'method': req.method,
        'params': req.params,
        'body': req.get_body().decode()
    }}
    logger.info(f'HTTP request received', extra=req_properties)
   
    # Both get and post requests are supported
    # Retrieve input seed value either from param or body
    # Log exception message in case of ValueError for debugging purposes
    seed = req.params.get('seed')
    if not seed:
        try:
            req_body = req.get_json()
        except Exception:
            logger.exception('Captured an exception', extra=req_properties)
            return func.HttpResponse('Received non-valid JSON data', status_code=500)
        else:
            seed = req_body.get('seed')

    # Function execution, check whether valid input value is given
    if seed and int(seed) > 0:
        result = fibonacci(int(seed))
        queue_msg = json.dumps({
            'seed': seed,
            'seed_fibonacci': result
        })
        msg.set(queue_msg)
        return func.HttpResponse(f'The Fibonacci number of {seed} is {result}')
    else:
        logger.warning('Received negative seed value', extra=req_properties)
        return func.HttpResponse(
            "Please pass a non-negative seed number",
            status_code=400
        )
