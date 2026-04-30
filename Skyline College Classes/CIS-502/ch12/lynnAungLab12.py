##
#  Student Name:  Lynn Aung
#  Course: CIS 502 Applied Python Programming
#  Lab Assignment 12 - Multithreaded Programming
#  Application: Using threads in Python
#  Description: Use Python's threading module to work with threads.
#               I will create a baisc API for spawning multiple threads
#               in a program using Python3's threading module.  
#  Development Environment:  Anaconda
#  Version: Python 3.7
#  Solution File:  lynnAungLab12.py
#  Date: 05/06/25


import threading
import time
import math

event1_done = threading.Event()
event2_done = threading.Event()

def job1():
    """
    Thread-1: compute square+1 of a list of numbers.
    """
    print("Thread 1 job one: Square plus one of 3 numbers:")
    numbers = [2, 4, 6]
    for n in numbers:
        result = n * n + 1
        print(f"  Square plus one of {n:2} = {result:3}")
        time.sleep(0.1) 
    # signal that job1 is done
    event1_done.set()

def job2():
    """
    Thread-2: wait for job1, then compute cubes of same numbers.
    """
    event1_done.wait()
    print("\nThread 2 job two: Cube of 3 numbers:")
    numbers = [2, 4, 6]
    for n in numbers:
        result = n ** 3
        print(f"  Cube of {n:2} = {result:4}")
        time.sleep(0.1)
    # signal that job2 is done
    event2_done.set()

def job3():
    """
    Thread-3: wait for job2, then compute factorial of the numbers.
    """
    event2_done.wait()
    print("\nThread 3 job three: Factorial of 3 numbers:")
    numbers = [2, 4, 6]
    for n in numbers:
        result = n / 2
        print(f"  Factorial of {n:2} = {result:4}")
        time.sleep(0.1)

def main():
    # Create threads
    t1 = threading.Thread(target=job1, name="Thread-1")
    t2 = threading.Thread(target=job2, name="Thread-2")
    t3 = threading.Thread(target=job3, name="Thread-3")

    print(f"{t1.name} created: {isinstance(t1, threading.Thread)}")
    print(f"{t2.name} created: {isinstance(t2, threading.Thread)}")
    print(f"{t3.name} created: {isinstance(t3, threading.Thread)}")

    # Start threads
    try:
        t1.start()
        print(f"{t1.name} started successfully.")
    except Exception as e:
        print(f"Failed to start {t1.name}: {e}")

    try:
        t2.start()
        print(f"{t2.name} started successfully.")
    except Exception as e:
        print(f"Failed to start {t2.name}: {e}")

    try:
        t3.start()
        print(f"{t3.name} started successfully.")
    except Exception as e:
        print(f"Failed to start {t3.name}: {e}")

    # Wait for all to finish before exiting
    t1.join()
    t2.join()
    t3.join()
    print("\nAll threads have completed.")

if __name__ == "__main__":
    main()
