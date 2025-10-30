def sjf(processes,burst_time):
    n = len(processes)
    sorted_processes=sorted(zip(burst_time,processes))
    sorted_bursttime = [b for b,p in sorted_processes]
    sorted_pids = [p for b , p in sorted_processes]

    waiting_time = [0]*n
    turnaround_time = [0]*n

    for i in range(1,n):
        waiting_time[i]=waiting_time[i-1]+sorted_bursttime[i-1]

    for i in range(n):
        turnaround_time[i]=waiting_time[i]+sorted_bursttime[i]

    avg_waiting=sum(waiting_time)/n
    avg_turnaround=sum(turnaround_time)/n

    for i in range(n):
      print(f"P{sorted_pids[i]}\t{sorted_bursttime[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")


    print("avg waiting time is",avg_waiting)
    print("avg turnaround time is ",avg_turnaround)

processes=[0,2,4,6,8]
burst_time=[5,2,1,3,5]

sjf(processes,burst_time)