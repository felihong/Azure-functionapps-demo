import logging
import json
import time
import azure.functions as func
import requests


def blocking_call(name):
    time.sleep(5)
    return name


# Simple entry function using timer
def returnName(req: func.HttpRequest):
    name = req.params.get('name')
    return func.HttpResponse(f"Say Hello to {blocking_call(name)}")


# Entry function for webpage parsing
def parsePage(req: func.HttpRequest):
    response = requests.get('https://www.microsoft.com')
    if response:
        return func.HttpResponse(response.text)
    else:
        return func.HttpResponse(body='NotFound', status_code=404)