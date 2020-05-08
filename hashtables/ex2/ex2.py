#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    storage = dict()
    routes = list()

    for i in tickets:
        storage[i.source] = i.destination

    index = 0
    # the first destination will be the one with "NONE" because this is the starting airport
    destination = "NONE"

    #run loop as long as there are still tickets in itenerary
    while index < length:
        # reset the destination to be the next destination for the next iteration
        destination = storage.get(destination)
        # add that destination to the final routes list
        routes.append(destination)
        index += 1
    
    return routes


