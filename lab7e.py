#!/usr/bin/env python3

class Time:
    """Class to represent a time object"""
    
    def __init__(self, hour, minute, second):
        """Initialize the time object with hour, minute, and second"""
        if not (0 <= hour < 24) or not (0 <= minute < 60) or not (0 <= second < 60):
            raise ValueError("Invalid time values")
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return time in HH:MM:SS format"""
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __repr__(self):
        """Return time in a more detailed format for debugging"""
        return f"Time({self.hour}, {self.minute}, {self.second})"

# Example usage
if __name__ == "__main__":
    t = Time(9, 50, 0)
    print(f"__str__: {str(t)}")
    print(f"__repr__: {repr(t)}")
