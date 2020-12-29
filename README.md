# Pick a generic object where something could cause exception in its state (example: parts breaking on a vehicle),

I picked a car, with the arguments tires, engine, gasoline.

# Describe a generic exception that could happen in your object (example: BrokenVehiclePartError),

I just named this Error.

# Describe two subclasses of the object (examples: car and truck, boat and starship, boat and bike),

The two subclasses are a jeep and a truck.

# Describe two subclasses of the exception (examples: flat tire, busted hitch, reactor coolant leak)

The engine could be broken, or tires flat, or gasoline tank empty.

# Draw an inheritance diagram that shows the relationships between the various classes and the exceptions.

I don’t have my ipad at the moment but essentially the car has all of the arguments as well as three methods (engine_working, tires_inflated, gasoline_full) which all return true. The truck and jeep inherits those methods and arguments, as well as both the truck and jeep change 1 of the methods each.

# What kinds of tests would be useful for this?  How could we test some of it to verify that it was working properly?

I only used simple print statements to check whether the jeep and truck classes inherited from the car class. Unsure of what other methods I could use, wasn't able to get feedback from you.

# Implement some of those tests in PyTest!

Unsure if I did this correctly, I tried and created a simple one. Still don't understand this part of class, especially when it comes to GUI functions and methods. Haven't gotten the feedback I needed in order to succeed in this area of the class due to the circumstances of our class.
