# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
import time
from typing import Any, Dict


def main(body: Dict[str, Any]) -> Dict[str, Any]:
    time.sleep(15)
    return body['data'] if body and body.get('data') else {}
