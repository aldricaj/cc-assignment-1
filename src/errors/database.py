
class ItemDoesNotExistError(Exception):
    def __init__(self, location, name):
        Exception.__init__(self, f'Item: {name} could not be found at {location}')

class ItemAlreadyExistError(Exception):
    def __init__(self, location, name):
        Exception.__init__(self, f'Item: {name} already exists at {location}')