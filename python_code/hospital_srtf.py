def srtf(processes,arrival_time,bt):
    n = len(processes)
    arrival_time=[0]*n
    bt=[0]*n
    time_remaining=bt.copy()
    waiting = 0
    completed =0


    while completed != n:
        for j in range(n):
             if arrival_time[j] <= t and time_remaining[j] < min_remaining and time_remaining[j] > 0:

                        min_remaining =time_remaining[j]
                        found_job = True
