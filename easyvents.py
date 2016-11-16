'''
@author: Sebastian Bechtold

Last Change: 2016-11-16
'''

############# BEGIN EventDispatcher class ############
class EventDispatcher:
    
    def __init__(self):
        # Create a dictionary for the subscription lists.
        # They keys will be event names, the values will
        # be the subscription lists for each event:
        self.listeners = dict()
    
    
    def addListener(self, eventName, listener):
        
        # If there's no subscription list for 
        # the passed event yet, create one:
        if not eventName in self.listeners:
            self.listeners[eventName] = []
        
        # If the passed listener is not on the
        # subscription list yet, add it:
        if not listener in self.listeners[eventName]:
            self.listeners[eventName].append(listener)
    
    
    def removeListener(self, eventName, listener):
        if not eventName in self.listeners:
            return
        
        if listener in self.listeners[eventName]:
            self.listeners[eventName].remove(listener)
    
        
    def fire(self, eventName, payload):
        
        # If passed event is unknown, abort here:
        if not eventName in self.listeners:
            return
        
        # Otherwise, call all registered subscribers:
        for listener in self.listeners[eventName]:
            listener(payload) 
            
############# END EventDispatcher class ############
