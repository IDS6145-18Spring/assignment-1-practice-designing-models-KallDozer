from control_info_element import control_info_element

class traffic_light(control_info_element):
    ''' A general traffic_light class '''
    def __init__(self, i, x, y, r, iN):
        self.locationX = x
        self.locationY = y
        self.belongstoRoad = r
        self.intervall = iN
        control_info_element.__init__(self, i)

    def pushStatus (self):
        return "This is the current status of the traffic light"

    def changeIntervall (self):
        return None