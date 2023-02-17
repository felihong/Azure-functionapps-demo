import logging
import azure.functions as func
from custom_pkg.user_management import userManager


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        umanager = userManager()
        rev_name = umanager.reverse_name(name)
        return func.HttpResponse(f"Hello, {name}. The reversed version of your name is {rev_name}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
