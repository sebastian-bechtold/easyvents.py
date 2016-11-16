'''
@author: Sebastian Bechtold

Last Change: 2016-11-16
'''

# Import the easyvents module:
import easyvents

# Create event dispatcher instance:
ed = easyvents.EventDispatcher()

# Define an event handler function:   
def handleMyEvent(message):
    print "I'm a function and I just received a message: ", message

# Register event handler for the "myEvent" event:
ed.addListener("myEvent", handleMyEvent)

# Fire the "myEvent" event:
ed.fire("myEvent", "Hello world!")

# Remove the stand-alone function from the subscribers list:
ed.removeListener("myEvent", handleMyEvent)


# Now, let's create an event handler-handing class:   
class MyEventHandlerClass:
    
    def handleMyEvent(self, message):
        print "I'm an object method and I just received a message:", message



# Create an instance of our event handler class:
myObject = MyEventHandlerClass()

# Register object method as event handler for the "myEvent" event:
ed.addListener("myEvent", myObject.handleMyEvent)

# Fire the "myEvent" event:
ed.fire("myEvent", "Hello universe!")

