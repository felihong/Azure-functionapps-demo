import azure.functions as func
import logging


def main(
    req: func.HttpRequest,
    obj: func.InputStream
):
    logging.info(f'Python HTTP-triggered function processed.')
    return func.HttpResponse(obj.read(), mimetype='image/png')