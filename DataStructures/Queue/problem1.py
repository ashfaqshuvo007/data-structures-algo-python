# Queue (FIFO) data structure implementation
# Problem:
# Design a food ordering system where your python program will run two threads,
#
#   i.  Place Order:
#           This thread will be placing an order and inserting that into a queue.
#           This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
#   ii. Serve Order:
#       This thread will server the order.
#       All you need to do is pop the order out of the queue and print it.
#       This thread serves an order every 2 seconds.
#       Also start this thread 1 second after place order thread is started.

from collections import deque
import time
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, element):
        self.buffer.appendleft(element)

    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0


def place_order(q, placed_orders):
    for order in placed_orders:
        print("Placing order for: ", order)
        q.enqueue(order)
        time.sleep(0.5)


def serve_order(q):
    if q.is_empty():
        return "Order queue is empty"
    else:
        while q.size() != 0:
            print("Order Served: ", q.dequeue())
            time.sleep(2)


if __name__ == '__main__':
    t = time.time()
    que = Queue()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    placeOrderQueue = threading.Thread(target=place_order, args=(que, orders))
    serveOrderQueue = threading.Thread(target=serve_order, args=(que,))

    placeOrderQueue.start()
    time.sleep(1)
    serveOrderQueue.start()

    placeOrderQueue.join()
    serveOrderQueue.join()

    timeTaken = time.time() - t
    print("Time taken: ", timeTaken)
