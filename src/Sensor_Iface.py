import lib16inpind, json, time, threading

class Sensor:
    def __init__(self, field_name, stack, channel_number, delay=0):
        self.field_name = field_name
        self.stack = stack
        self.channel_number = channel_number
        self.delay = delay
        self.prev_sensor_state = self.get_sensor_state()
        self.thread = threading.Thread(target=self.monitor_event_detect)
        self.thread.start()  # Start the monitoring thread

    def monitor_event_detect(self):
        while True:
            current_sensor_state = self.get_sensor_state()
            if not self.prev_sensor_state and current_sensor_state:
                self.sensor_action()  # Call sensor_action if sensor state changes from False to True
            self.prev_sensor_state = current_sensor_state
            

    def sensor_action(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            data[self.field_name][0] += 1
            print(data)
        
        with open('data.json', 'w') as file:
            file.write(json.dumps(data, indent=4))
        if self.delay > 0:
            time.sleep(self.delay)  # Delay to avoid double counting

    def get_sensor_state(self):
        return lib16inpind.readCh(self.stack, self.channel_number) == 1

# Instantiate Sensor objects for each sensor
#sensor_cases = Sensor("CASES", 0, 1)
#sensor_bins = Sensor("BINS", 0, 2, delay=15)
