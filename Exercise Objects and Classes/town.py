# Create a class Town. The __init__ method should receive the name of the town (string).
# Each town has a latitude - "0°N" upon initialization and a longitude - "0°E" upon initialization.
# It should also have 3 more methods:

# · set_latitude(latitude) - sets a latitude

# · set_longitude(longitude) - sets a longitude

# · __repr__ - returns a representation of the object in the following string format:
# "Town: {name} | Latitude: {latitude} | Longitude: {longitude}"

#                             Example

# Test Code                                               Output

# town = Town("Sofia")                                    Town: Sofia | Latitude: 42° 41' 51.04"
# town.set_latitude("42° 41\' 51.04\" N")                 N | Longitude: 23° 19' 26.94" E
# town.set_longitude("23° 19\' 26.94\" E")
# print(town)


class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = ""
        self.longitude = ""

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)