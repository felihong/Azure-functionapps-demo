# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
import azure.functions as func
import azure.durable_functions as df


"""
Implementation of an orchestrator that signals and then calls a counter Durable Entity;
Returns the state after applying the operation on the durable entity
"""
def orchestrator_function(context: df.DurableOrchestrationContext):
    # Get entity by name
    entityId = df.EntityId("counter", "myCounter")

    # Orchestration can either signal or call durable entity
    # Here depending on input operation either increase the counter by 3 or reset to 0
    operation = context.get_input()
    if operation == "add":
        context.signal_entity(entityId, "add", 3)
    else:
        context.signal_entity(entityId, "reset")

    state = yield context.call_entity(entityId, "get")
    return state


main = df.Orchestrator.create(orchestrator_function)