########################################################################
# Owner: Anuj Singhal
# Description: Abstract class of unimplemented methods of logic
########################################################################

import abc

class EvenHub(abc.ABC):
    def __init__(self, CONNECTION_STR, EVENTHUB_NAME, BATCH_SIZE):
        self.CONNECTION_STR = CONNECTION_STR
        self.EVENTHUB_NAME = EVENTHUB_NAME
        self.EVENT_BATCH_SIZE = BATCH_SIZE

    @abc.abstractmethod
    def send_event(self):
        """Create spark session"""
        raise NotImplementedError
