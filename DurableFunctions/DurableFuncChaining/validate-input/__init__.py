# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
import time
from typing import Any, Dict


def main(transfer: Dict[str, Any]) -> Dict[str, Any]:
    time.sleep(15)

    if not transfer:
        raise Exception('The funds transfer data is mandatory')

    if not transfer.get('sourceAccount'):
        raise Exception('The Source Account is mandatory')

    if not transfer.get('targetAccount'):
        raise Exception('The Target Account is mandatory')

    return transfer
