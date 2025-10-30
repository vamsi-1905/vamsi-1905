

import threading

def square_numbers(num):
    num = num * num
    print(f"square of number: {num}")

def reverse_texts(text):
    text = text[::-1]
    print(f"reverse text: {text}")


nums = 5
texts = "hello"

t1 = threading.Thread(target=square_numbers, args=(nums,))
t2 = threading.Thread(target=reverse_texts, args=(texts,))

t1.start()
t2.start()

t1.join()
t2.join()
