class RingBuffer:
    def __init__(self, capacity):
        # Initialize capacity and empty buffer, yawn; had to add a location pointer
        self.capacity = capacity
        self.buffer_items = [None]*capacity
        self.location = 0
        

    def append(self, item):
        # Point new item to location
        self.buffer_items[self.location] = item

        # Check to see if capacity was reached, if so, assign it to position 0
        if self.location >= len(self.buffer_items) - 1:
            self.location = 0
        
        # else advance location
        else:
            self.location = self.location + 1

            
    def get(self):
        # return contents of buffer if not none
        return [item for item in self.buffer_items if item is not None]