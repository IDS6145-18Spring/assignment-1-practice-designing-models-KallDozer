class request:
    ''' A general request class '''

    def __init__(self, u, n, a, sX, sY, dX, dY, nS):
        self.user_ID = u
        self.number = n
        self.arrivalTime = a
        self.startLocX = sX
        self.startLocY = sY
        self.destinationLocX = dX
        self.destinationLocY = dY
        self.neededSpace = nS

    def __str__ (self):
        '''this function ensures that the request-details can be used for messages that '''
        return "This contains the detailed request for transportation!"

    def sendRequest (self):
        '''this function is responsible for submitting the request for transportation, with all his details'''
        return None

    def getStatus (self):
        '''this function is ensuring that the user can check the status of his request'''
        return None
