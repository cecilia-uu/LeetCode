def solution(schedules, length) -> int:
    # 1. flatten all schedules into a single list
    meetings = []
    for schedule in schedules:
        for m in schedule:
            meetings.append(m)
    # 2. sort
    meetings.sort()

    # 3. merge overlapping meetings
    merged_meetings = []
    for meeting in meetings:
        if not merged_meetings or merged_meetings[-1][1] < meeting[0]:
            merged_meetings.append(meeting)
        else:
            # Overlapping or touching meetings, merge them
            merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])

    # 4. Check gaps between merged meetings
    start_of_day = 0
    end_of_day = 24 * 60
    
    # Check the gap before the first meeting
    if merged_meetings[0][0] - start_of_day >= length:
        return start_of_day
    
    # Check gaps between consecutive meetings
    for i in range(1, len(merged_meetings)):
        previous_end = merged_meetings[i-1][1]
        current_start = merged_meetings[i][0]
        if current_start - previous_end >= length:
            return previous_end
    
    # Check the gap after the last meeting
    if end_of_day - merged_meetings[-1][1] >= length:
        return merged_meetings[-1][1]
    
    # If no suitable gap is found, return -1
    return -1

print(solution(schedules=[
    [[60,150],[180,240]],
    [[0,210], [360,420]]
], length=120))