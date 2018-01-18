from control_info_element import control_info_element

class traffic_light(control_info_element):
    ''' A general traffic_light class '''
    
    def __init__(self, i, x, y, r, iN):
        '''Intializes the traffic light'''
        self.locationX = x
        self.locationY = y
        self.belongstoRoad = r
        self.intervall = iN
        control_info_element.__init__(self, i)

    def pushStatus (self):
        '''Is pushing a feedback to the TCU and submitting his current Status (e.g. cars waiting at the intersection etc)'''
        return "This is the current status of the traffic light"

    def changeIntervall (self):
        '''This function is responsible for changing the intervall from green, to yellow to red'''
        '''So with this function it is possible to take influence on the duration of the green-phase (e.g. during rush hours)'''
        return None
