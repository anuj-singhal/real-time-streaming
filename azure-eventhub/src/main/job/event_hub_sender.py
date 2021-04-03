########################################################################
# Owner: Anuj
# Frequency: realtime sender
# Job Description: Event hub sender class to create
# producer and send messages in batch
########################################################################

from src.main.base import EvenHub
from azure.eventhub import EventHubProducerClient, EventData, EventDataBatch


class EvenHubSender(EvenHub):
    producer = EventHubProducerClient
    event_data_batch = EventDataBatch
    current_batch_size = 0
    batch_count = 0

    def __init__(self, CONNECTION_STR, EVENTHUB_NAME, BATCH_SIZE):
        EvenHub.__init__(self, CONNECTION_STR, EVENTHUB_NAME, BATCH_SIZE)
        self.producer = self.__create_producer__()
        self.current_batch_size = int(self.EVENT_BATCH_SIZE)
        self.event_data_batch = self.producer.create_batch()

    def __create_producer__(self):
        return EventHubProducerClient.from_connection_string(
            conn_str=self.CONNECTION_STR,
            eventhub_name=self.EVENTHUB_NAME
        )

    def send_event(self, message) -> str:
        status = self.__create_batch__(message)
        return status

    def __create_event_data__(self, message) -> EventData:
        event_data = EventData(message)
        return event_data

    def __create_batch__(self, message) -> str:
        status = None
        try:
            self.current_batch_size -= 1
            event_data = self.__create_event_data__(message)
            try:
                self.event_data_batch.add(event_data)
                status = "event_added"
            except ValueError as ve:
                print("Exception occured in message" + message)
                print(ve)
            if (self.current_batch_size == 0):
                if len(self.event_data_batch) > 0:
                    print("length of event_data_batch is " + str(len(self.event_data_batch)))
                    self.producer.send_batch(self.event_data_batch)
                    self.current_batch_size = int(self.EVENT_BATCH_SIZE)
                    self.event_data_batch = self.producer.create_batch()
                    self.batch_count += 1
                    print("batch sent successfully")
                    status = "event_success"
        except:
            status = "event_failed"
        return status