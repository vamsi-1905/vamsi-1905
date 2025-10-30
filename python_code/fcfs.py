

def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting times
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate turnaround times
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Calculate averages
    avg_waitingtime = sum(waiting_time) / n
    avg_turnaroundtime = sum(turnaround_time) / n

    # Print results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waitingtime:.2f}")
    print(f"Average Turnaround Time: {avg_turnaroundtime:.2f}")


# Example usage
processes = [1, 2, 3, 4]
burst_time = [5, 8, 6, 3]

fcfs(processes, burst_time)
