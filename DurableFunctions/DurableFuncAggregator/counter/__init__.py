import logging
import json
import azure.functions as func
import azure.durable_functions as df


def entity_function(context: df.DurableEntityContext):
    current_value = context.get_state(lambda: 0)
    
    # Support user defined operations
    operation = context.operation_name
    if operation == "add":
        amount = context.get_input()
        current_value += amount
    elif operation == "reset":
        current_value = 0
    elif operation == "get":
        pass
    
    context.set_state(current_value)
    context.set_result(current_value)


main = df.Entity.create(entity_function)