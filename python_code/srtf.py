# Function to implement the Shortest Remaining Time First (SRTF) scheduling algorithm.
# It takes three lists as input: process IDs, arrival times, and burst times.
def srtf(processes, arrival_time, burst_time):
    # Get the total number of processes.
    n = len(processes)
    # Create a copy of the burst_time list to track remaining time for each process.
    remaining_time = burst_time.copy()
    # Initialize lists to store the waiting and turnaround times for each process.
    waiting_time = [0] * n
    turnaround_time = [0] * n
    # 'completed' tracks the number of processes that have finished execution.
    completed = 0
    # 't' acts as a system clock, simulating time units.
    t = 0
    # 'min_remaining' stores the shortest remaining time found in each time unit.
    min_remaining = float("inf")
    # 'shortest_job_index' stores the index of the process with the minimum remaining time.
    shortest_job_index = 0
    # 'found_job' is a flag to check if a process was found to execute in the current time unit.
    found_job = False

    # The main loop continues until all processes are completed.
    while completed != n:
        # Loop to find the process with the minimum remaining time that has arrived.
        for j in range(n):
            # Check if the process has arrived (arrival_time[j] <= t)
            # and has a smaller remaining time than the current minimum
            # and is not yet finished (remaining_time[j] > 0).
            if arrival_time[j] <= t and remaining_time[j] < min_remaining and remaining_time[j] > 0:
                # Update the minimum remaining time.
                min_remaining = remaining_time[j]
                # Store the index of this process.
                shortest_job_index = j
                # Set the flag to true since we found a process to run.
                found_job = True

        # If no process has arrived yet, or all arrived processes are finished,
        # increment time and continue to the next loop iteration.
        if not found_job:
            t += 1
            continue

        # Run the shortest job for one time unit by decrementing its remaining time.
        remaining_time[shortest_job_index] -= 1
        # Update the minimum remaining time with the current process's remaining time.
        min_remaining = remaining_time[shortest_job_index]
        # If the remaining time becomes 0, reset min_remaining for the next search.
        if min_remaining == 0:
            min_remaining = float("inf")

        # Check if the current process has just finished execution.
        if remaining_time[shortest_job_index] == 0:
            # Increment the count of completed processes.
            completed += 1
            # Reset the found_job flag.
            found_job = False
            # Get the finish time of the completed process.
            finish_time = t + 1
            # Calculate the waiting time for the finished process.
            # waiting = finish_time - burst_time - arrival_time
            waiting_time[shortest_job_index] = finish_time - burst_time[shortest_job_index] - arrival_time[shortest_job_index]
            # Ensure waiting time is not negative (can happen due to initial conditions).
            if waiting_time[shortest_job_index] < 0:
                waiting_time[shortest_job_index] = 0

        # Increment the system clock for the current time unit.
        t += 1

    # After the loop, all processes are completed. Now, calculate turnaround times.
    for i in range(n):
        # Turnaround time = Burst time + Waiting time
        turnaround_time[i] = burst_time[i] + waiting_time[i]

    # Print the final results table.
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    # Calculate and print the average waiting and turnaround times.
    print(f"\nAverage Waiting Time: {sum(waiting_time) / n:.2f}")
    print(f"Average Turnaround Time: {sum(turnaround_time) / n:.2f}")

# Example usage of the srtf function.
processes = [1, 2, 3, 4]
arrival_time = [0, 1, 2, 3]
burst_time = [8, 4, 9, 5]

srtf(processes, arrival_time, burst_time)