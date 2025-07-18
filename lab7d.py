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

    def time_to_sec(self):
        """Method to convert time to total seconds"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        """Method to format the time as HH:MM:SS"""
        return str(self)

# Example usage
if __name__ == "__main__":
    t = Time(9, 50, 0)
    print(f"Time in seconds: {t.time_to_sec()}")
    print(f"Formatted time: {t.format_time()}")
