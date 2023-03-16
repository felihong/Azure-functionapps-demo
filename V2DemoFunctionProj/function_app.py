import azure.functions as func 
from http_blueprint import bp


# Import the blueprint object 
# Register the functions from blueprint instances to get them indexed
app = func.FunctionApp() 
app.register_functions(bp)