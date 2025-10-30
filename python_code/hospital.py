class Process:
    def __init__(self, pid, priority, arrival_t, burst):
        self.pid = pid
        self.priority = priority
        self.arrival_t = arrival_t
        self.burst = burst
        self.rem_time = burst
        self.start_time = -1
        self.finish_time = 0


def scheduler(process_list, time_period):
    process_list.sort(key=lambda x: x.arrival_t)

    ready_q1 = []  # Emergency
    ready_q2 = []  # Moderate
    ready_q3 = []  # Routine

    current_time = 0
    completed_list = []
    next_proc = 0
    total_procs = len(process_list)

    print(f"Time Quantum = {time_period}\n")

    # Main loop
    while len(completed_list) < total_procs:

        # Add arriving processes to ready queues
        while next_proc < total_procs and process_list[next_proc].arrival_t <= current_time:
            p = process_list[next_proc]
            if p.priority == 1:
                ready_q1.append(p)
            elif p.priority == 2:
                ready_q2.append(p)
            else:
                ready_q3.append(p)

            print(f"{p.pid} arrives at t={current_time} (Priority {p.priority})")
            next_proc += 1

        p = None
        p_priority = -1

        if len(ready_q1) > 0:
            p = ready_q1.pop(0)
            p_priority = 1
        elif len(ready_q2) > 0:
            p = ready_q2.pop(0)
            p_priority = 2
        elif len(ready_q3) > 0:
            p = ready_q3.pop(0)
            p_priority = 3

        if p is None:
            # idling
            if next_proc < total_procs:
                current_time = process_list[next_proc].arrival_t
                continue
            else:
                break

        if p.start_time == -1:
            p.start_time = current_time


        run_time_limit = min(time_period, p.rem_time)

        if p_priority == 1:
            # Priority 1 runs for its full TQ, ignoring new arrivals
            exec_time = run_time_limit
        else:
            # Other priorities are interrupted by arrivals
            next_arr_in = 999999
            if next_proc < total_procs:
                next_arr_in = process_list[next_proc].arrival_t - current_time
            exec_time = min(run_time_limit, next_arr_in)


        if exec_time <= 0:
            if p_priority == 1:
                ready_q1.insert(0, p)
            elif p_priority == 2:
                ready_q2.insert(0, p)
            else:
                ready_q3.insert(0, p)
            continue

        print(
            f"{p.pid} starts at t={current_time} -> runs for {exec_time} mins -> remaining = {p.rem_time - exec_time}")

        p.rem_time -= exec_time
        current_time += exec_time  # Advance clock


        while next_proc < total_procs and process_list[next_proc].arrival_t <= current_time:
            new_p = process_list[next_proc]
            if new_p.priority == 1:
                ready_q1.append(new_p)
            elif new_p.priority == 2:
                ready_q2.append(new_p)
            else:
                ready_q3.append(new_p)
            print(f"{new_p.pid} arrives at t={current_time} (Priority {new_p.priority})")
            next_proc += 1


        if p.rem_time == 0:
            print(f"{p.pid} FINISHED at t={current_time}\n")
            p.finish_time = current_time
            completed_list.append(p)
        else:
            if p_priority == 1:
                if exec_time == time_period:  # Only print for TQ end
                    print(f"{p.pid} time quantum end, put to back (rem: {p.rem_time})\n")
                ready_q1.append(p)
            elif p_priority == 2:

                if len(ready_q1) > 0:
                    print(f"{p.pid} preempted (rem: {p.rem_time})\n")
                elif exec_time == time_period:
                    print(f"{p.pid} time quantum end, put to back (rem: {p.rem_time})\n")
                ready_q2.append(p)
            else:

                if len(ready_q1) > 0 or len(ready_q2) > 0:
                    print(f" {p.pid} preempted (rem: {p.rem_time})\n")
                elif exec_time == time_period:
                    print(f"{p.pid} time quantum end, put to back (rem: {p.rem_time})\n")
                ready_q3.append(p)



if __name__ == "__main__":
    # input part
    my_processes = [
        Process(pid="P1", priority=2, arrival_t=0, burst=25),
        Process(pid="P2", priority=1, arrival_t=2, burst=15),
        Process(pid="P3", priority=3, arrival_t=3, burst=10),
        Process(pid="P4", priority=1, arrival_t=5, burst=20),
    ]

    # func call
    scheduler(my_processes, time_period=10)