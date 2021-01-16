import json

from azure.eventhub import EventData

from extensions import event_hub_client


class EventHubWriter:

    def write_to_event_hub(self, data):

        csv_dict = {}

        with event_hub_client:
            for idx, line in enumerate(data, start=1):
                line = line.split(',')
                try:
                    csv_dict['animal_id'] = line[0]
                    csv_dict['animal_type'] = line[1]
                    csv_dict['animal_breed'] = line[2]
                    csv_dict['kennel_number'] = line[3]
                except IndexError:
                    continue

                # Create a batch.
                data_batch = event_hub_client.create_batch()

                data_batch.add(EventData(json.dumps(csv_dict)))

                event_hub_client.send_batch(data_batch)
