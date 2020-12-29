# This is a simple program that should show inheritance, polymorphism, and exceptions being handled

class Car():
    def __init__(self, tires, engine, gasoline):
        self.tires = tires
        self.engine = engine
        self.gasoline = gasoline

    def engine_working(self):
        return True

    def tires_inflated(self):
        return True

    def gasoline_full(self):
        return True


class truck(Car):
    def __init__(self, tires, engine, gasoline):
        super().__init__(tires, engine, gasoline)

    def tires_inflated(self):
        return False


class jeep(Car):
    def __init__(self, tires, engine, gasoline):
        super().__init__(tires, engine, gasoline)

    def engine_working(self):
        return False


class Error(Exception):
    """Base class for other exceptions"""
    pass


class FlatTiresError(Error):
    """Raised when the tires are flat."""
    pass


class EngineFailureError(Error):
    """Raised when the engine does not work."""
    pass


trucker = truck(4, 1, 'full')
jeeper = jeep(5, 1, 'empty') # extra wheel

print(trucker.tires, trucker.tires_inflated())
print(jeeper.gasoline, jeeper.engine_working())

# Exceptions section
while True:
    try:
        if trucker.tires_inflated() == False:
            raise FlatTiresError
        break
    except FlatTiresError:
        print("The tires are flat!")
        break

while True:
    try:
        if jeeper.engine_working() == False:
            raise EngineFailureError
        break
    except EngineFailureError:
        print("The engine is not working!")
        break

while True:
    if jeeper.engine_working() == False:
        raise EngineFailureError
    break

def test_answer():
    assert trucker.tires_inflated() == False