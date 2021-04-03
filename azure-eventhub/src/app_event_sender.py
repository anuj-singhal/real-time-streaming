########################################################################
# Owner: Anuj
# Frequency: realtime sender
# Job Description: send messages to azure eventhub
########################################################################

import time
import os
from src.config import *
from src.main.job.event_hub_sender import EvenHubSender
from azure.eventhub import EventHubProducerClient, EventData

CONNECTION_STR = eventinfosend["CONNECTION_STR"]
EVENTHUB_NAME = eventinfosend["EVENTHUB_NAME"]
BATCH_SIZE = eventinfosend["EVENT_BATCH_SIZE"]

#start_time = time.time()

def main():
    try:
        print("Conection String is {}".format(CONNECTION_STR))
        print("Event name is {}".format(EVENTHUB_NAME))

        sender = EvenHubSender(CONNECTION_STR, EVENTHUB_NAME, BATCH_SIZE)
        for i in range(10):
            msg = "Message Number: " + str(i)
            print("Batch Number - " + str(sender.batch_count))
            status = sender.send_event(msg)
            print("Status - " + status)

        #print("Send messages in {} seconds.".format(time.time() - start_time))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
