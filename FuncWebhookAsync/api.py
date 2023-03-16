import logging
import json
import azure.functions as func
import asyncio
import aiohttp


async def blocking_call(name):
    return await asyncio.sleep(5, result=name)


# Simple entry function using async timer
async def returnName(req: func.HttpRequest):
    name = req.params.get('name')
    return func.HttpResponse(f"Say Hello to {await blocking_call(name)}")


# Entry function for webpage parsing
async def parsePage(req: func.HttpRequest):
    async with aiohttp.ClientSession() as client:
        async with client.get('https://www.microsoft.com') as response:
            return func.HttpResponse(await response.text())
        
    return func.HttpResponse(body='NotFound', status_code=404)