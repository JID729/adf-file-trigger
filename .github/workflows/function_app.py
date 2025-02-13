import logging
import azure.functions as func

def main(event: func.EventGridEvent):
    logging.info('Received Event Grid event: %s', event.get_json())
