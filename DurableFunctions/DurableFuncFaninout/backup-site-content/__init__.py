import azure.functions as func
import azure.durable_functions as df
import logging


def orchestrator_function(context: df.DurableOrchestrationContext):

    root_directory = context.get_input()
    logging.info(root_directory)

    if not root_directory:
        raise Exception("A directory path is required as input")

    # Concurrent activity jobs
    files = yield context.call_activity("get-file-list", root_directory)
    tasks = []
    for file in files:
        tasks.append(context.call_activity("copy-file-to-blob", file))
    
    # Aggregation
    results = yield context.task_all(tasks)
    total_bytes = sum(results)
    
    return f"Total byte cound {total_bytes}"


main = df.Orchestrator.create(orchestrator_function)