import logging
import json

def main(event: dict):
    logging.info(f"Received Event Grid event: {json.dumps(event)}")
    return "Event processed successfully"
