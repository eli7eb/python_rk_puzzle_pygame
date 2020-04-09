import sys


# switch between game states
# each state has enter update exit

class FsmManager:
    def __init__(self):
        self.currentState = None

    def update(self):
        if (self.currentState != None):
            self.currentState.update()

    def changeState(self, newState):
        if (self.currentState != None):
            self.currentState.exit()
            self.currentState = newState
            self.currentState.enter()