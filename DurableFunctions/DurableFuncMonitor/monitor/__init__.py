import azure.durable_functions as df
from datetime import timedelta
from typing import Dict


def orchestrator_function(context: df.DurableOrchestrationContext):

    monitoring_request: Dict[str, str] = context.get_input()
    expiry_mins = monitoring_request["expiryMinutes"]
    polling_interval = monitoring_request["pollingInterval"]
    repo_url = monitoring_request["repo"]
    phone = monitoring_request["phone"]
    # Expiration of the repo monitoring
    expiry_time = context.current_utc_datetime + timedelta(minutes=expiry_mins)

    while context.current_utc_datetime < expiry_time:
        # Count the number of issues in the repo 
        too_many_issues = yield context.call_activity("check-open-issues", repo_url)

        # If we detect too many issues, text the provided phone number
        if too_many_issues:
            # Extract URLs of GitHub issues, and return them
            yield context.call_activity("send-alert", phone)
            break
        else:
            # Reporting the number of statuses found
            status = f"The repository does not have too many issues, for now ..."
            context.set_custom_status(status)
        
            # Schedule a new "wake up" signal
            next_check = context.current_utc_datetime + timedelta(minutes=polling_interval)
            yield context.create_timer(next_check)

    return "Monitor completed!"


main = df.Orchestrator.create(orchestrator_function)