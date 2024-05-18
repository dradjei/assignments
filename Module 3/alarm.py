def interpretWaitTime(current_time, wait_time):
    
    return (current_time + wait_time) % 24


if __name__ == "__main__":
    hour = int(input("Enter the current time (in hours) "))
    wait_time = int(input("Enter the amount of hours to wait for alarm "))
    print("Time of Alarm (24 Hour Clock):", interpretWaitTime(hour, wait_time))
    