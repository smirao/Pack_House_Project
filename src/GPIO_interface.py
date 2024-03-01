import json

class GPIO_Iface:
    def __init__(self, GPIO):
        self.GPIO = GPIO
        self.PIN = 18
        self.total = 0
        self.GPIO.setmode(GPIO.BCM)
        
        self.GPIO.setup(self.PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.GPIO.add_event_detect(self.PIN, GPIO.BOTH, callback=self.break_beam_callback)
    
    def break_beam_callback(self):
        if self.GPIO.input(self.BEAM_PIN):  
            with open('data.json', 'r') as file:
                data = json.load(file)
                print(data)
                data["BEAM"][0] += 1
                print(data)
            with open('data.json', 'w') as file:
                file.write(json.dumps(data, indent=4))
