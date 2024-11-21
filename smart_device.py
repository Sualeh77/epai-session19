class SmartDevice:
    device_count = 0

    def __init__(self, device_name:str, model_number:str, is_online:bool = False) -> None:
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = dict()
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        """
            Adds or updates a status attribute in the status dictionary
        """
        self.status[attribute] = self.status.setdefault(attribute, value)

    def get_status(self, attribute):
        """
            Returns the value of a specific status attribute. If the attribute does not exist, it should return 'Attribute not found'. 
        """
        return self.status.get(attribute, 'Attribute not found')
    
    def toggle_online(self):
        """
            Changes the device's online status (is_online) to its opposite value
        """
        self.is_online = not self.is_online
        return not self.is_online

    def reset(self):
        """
            Resets all status attributes to their default values (i.e. clears the status dictionary)
        """
        self.status.clear()

    def __call__(self):
        return f"{self.device_name} (Model: {self.model_number})"
    
    def device_info(self):
        return {"name": self.device_name, "model": self.model_number, "is_online": self.is_online, "status": self.status}
