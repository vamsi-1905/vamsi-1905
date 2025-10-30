import time
import threading

# Shared variable
flag = [False, False]  # flag[0] for User A, flag[1] for User B
turn = 0

def user_a():
    global flag, turn
    print("User A wants to access the printer.")

    flag[0] = True
    turn = 1  # Give priority to User B

 # Wait while not A turn
    while flag[1] and turn == 1:
        time.sleep(0.1)  # Busy wait
 # CS
    print("User A enters the printer.")
    print("...User A is printing...")
    time.sleep(0.5)
    print("User A completes printing and exits.")
    # Exit Section
    flag[0] = False

def user_b():
    global flag, turn
    print("User B wants to access the printer.")

    flag[1] = True
    turn = 0  # Give priority to User A
    # Wait while not B turn
    while flag[0] and turn == 0:
        time.sleep(0.1)  # Busy wait

    # CS
    print("User B enters the printer.")
    print("...User B is printing...")
    time.sleep(0.5)
    print("User B completes printing and exits.")
 # Exit Section
    flag[1] = False

if __name__ == "__main__":
    print("Peterson's Algorithm")
    # concurrency
    t1 = threading.Thread(target=user_a)
    t2 = threading.Thread(target=user_b)

    t1.start()
    time.sleep(0.1)  #let a start
    t2.start()

    t1.join()
    t2.join()

    print("...So on\n")
