"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        self.start = start

    def generate(self):
        ''' Returns the next incremental value initially passed to the class and adds 1 to said value'''
        print(self.start)
        self.start += 1
    
    def reset(self):
        '''Resets the current value back to the initial value'''
        self.start = 100



