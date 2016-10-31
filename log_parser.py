import sys
import time
from datetime import datetime, date
import numpy as np

def parse_lines(lines):

    # Initialize times for total time and connected
    start_time = 0
    connected_time = 0
    connect_start = 0
    total_time = 0

    for log in lines:
        # Split into timestamp and status
        log_details = log.split(" :: ")
        log_time = retrieve_time(log_details[0])
        # Retrieve status of each log
        status = log_details[1]
        # Mark start time
        if status == "START\n":
            start_time = log_time
        # Make sure to mark any final connected time before calculating final
        elif status == "SHUTDOWN\n":
            connected_time += (log_time - connect_start).total_seconds()
            total_time = (log_time - start_time).total_seconds()
        # Start the clock for any connected logs
        elif status == "CONNECTED\n":
            connect_start = log_time
        # Check when disconeccted and add to running total
        elif status == "DISCONNECTED\n":
            connected_time += (log_time - connect_start).total_seconds()
            connect_start = 0

    # If user never connected
    if connected_time == 0:
        return "0%"
    else:
        final_connected_time = (connected_time / total_time) * 100
        return str(final_connected_time) + "%"

def retrieve_time(timestamp):

    timestamp = timestamp[1:-1]
    utc_time = datetime.strptime(timestamp, "%m/%d/%Y-%H:%M:%S")
    print(utc_time)
    return utc_time
    # print(utc_time.time())
    #epoch_time = (utc_time - datetime(1970, 1, 1)).days * (24 * 60 * 60)
    #print(epoch_time)


    #return epoch_time


####################################
# Don't modify the functions below #
####################################

def parse_file(filename):
    try:
        with open(filename, "rU") as f:
            all_lines = f.readlines()
        return parse_lines(all_lines)
    except IOError:
        print "File not found."
        sys.exit()


def main():
    filename = "input_1.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    answer = parse_file(filename)
    print answer

if __name__ == "__main__":
    main()
