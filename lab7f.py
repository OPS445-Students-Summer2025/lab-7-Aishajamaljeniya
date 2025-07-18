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

    def __add__(self, other):
        """Overload the + operator to add two time objects"""
        total_seconds = self.to_seconds() + other.to_seconds()
        return sec_to_time(total_seconds)

    def to_seconds(self):
        """Convert time to total seconds"""
        return self.hour * 3600 + self.minute * 60 + self.second

def sec_to_time(seconds):
    """Convert seconds to a time object"""
    hour = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return Time(hour, minutes, seconds)

# Example usage
if __name__ == "__main__":
    t1 = Time(9, 50, 0)
    t2 = Time(1, 10, 0)
    t3 = t1 + t2  # Using overloaded + operator
    print(f"Sum of times: {str(t3)}")
