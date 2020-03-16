# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
	pass

# Based on Vehicle class
class FlightVehicle(Vehicle):
	pass

# Based on FlightVehicle
class Starship(FlightVehicle):
	pass

# Based on FlightVehicle
class Airplane(FlightVehicle):
	pass

# Based on Vehicle
class GroundVehicle(Vehicle):
	pass

# Based on GroundVehicle
class Car(GroundVehicle):
	pass

# Based on GroundVehicle
class Motorcycle(GroundVehicle):
	pass