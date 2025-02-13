import logging
import azure.functions as func

def main(event: func.EventGridEvent):
    logging.info(f"Event received: {event.get_json()}")
