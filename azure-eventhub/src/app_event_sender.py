########################################################################
# Owner: Anuj
# Frequency: realtime sender
# Job Description: send messages to azure eventhub
########################################################################

import os
from src.config import *
from src.main.job.event_hub_sender import EvenHubSender
from src.main.utils import utils
import json
from time import sleep

logging.info("Event hub sender started")

CONNECTION_STR = eventinfosend["CONNECTION_STR"]
EVENTHUB_NAME = eventinfosend["EVENTHUB_NAME"]
BATCH_SIZE = eventinfosend["EVENT_BATCH_SIZE"]

def main():
    try:
        logging.info("Conection String is {}".format(CONNECTION_STR))
        logging.info("Event name is {}".format(EVENTHUB_NAME))

        filepath = os.path.dirname(os.path.abspath(__file__)) + "\data\sample_data.csv"
        jsonArray = utils.csv_to_listofdict(filepath)

        sender = EvenHubSender(CONNECTION_STR, EVENTHUB_NAME, BATCH_SIZE)
        for row in jsonArray:
            sender.send_event(json.dumps(row))
            sleep(1)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
