# def getMaxTrafficTime(start, end) -> int:
#     n = len(start)
#     time = max(end) # nlogn
#     record = [0] * (time+1)
#     for s, e in zip(start, end): # n
#         for i in range(s, e+1): # n
#             record[i] += 1
#     r = max(record)
#     print(record)
#     for i in range(time+1):
#         if record[i] == r:
#             return i
    

# start = [1, 6, 2, 9]
# end = [8, 7, 6, 10]
# print(getMaxTrafficTime(start, end))

def find_earliest_peak_time(start, end):
    # Create an event list with (time, type) where type is +1 for start and -1 for end
    events = []
    for s in start:
        events.append((s, 1))  # +1 for start of interaction
    for e in end:
        events.append((e + 1, -1))  # -1 for end of interaction (end is inclusive, so add 1)

    # Sort events by time; in case of tie, sort -1 before +1 to ensure correct order
    events.sort()

    max_clients = 0  # Track the maximum number of concurrent clients
    current_clients = 0  # Track the current number of clients interacting
    earliest_time = 0  # Track the earliest time with maximum clients

    # Iterate over sorted events
    for time, event in events:
        current_clients += event  # Update current concurrent clients
        
        # Check if this is the new maximum
        if current_clients > max_clients:
            max_clients = current_clients
            earliest_time = time
    
    return earliest_time

# Example usage:
start = [1, 6, 2, 9]
end = [8, 7, 6, 10]
result = find_earliest_peak_time(start, end)
print(f"The earliest time with the maximum number of concurrent clients is: {result}")
