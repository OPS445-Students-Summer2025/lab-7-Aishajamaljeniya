#!/usr/bin/env python3

schoolName = "Seneca"

def function1():
    schoolName = "SICT"
    print(f"print() in function1 on schoolName: {schoolName}")

def function2():
    global schoolName
    schoolName = "SSDO"
    print(f"print() in function2 on schoolName: {schoolName}")

# Main program
if __name__ == "__main__":
    print(f"print() in main on schoolName: {schoolName}")
    function1()
    print(f"print() in main on schoolName: {schoolName}")
    function2()
    print(f"print() in main on schoolName: {schoolName}")
