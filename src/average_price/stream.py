import random
import threading
import time


def stream_from_thread(stop_event, loop, ins_dict, queues, throttle=False):
    print('***Starting the thread for the continuous stream...')
    nr_ins = len(ins_dict)
    t = threading.currentThread()
    while not stop_event.is_set():
        instrument = random.randint(1, nr_ins)
        ins_name = 'ins' + str(instrument)
        nr_market = len(ins_dict[ins_name])
        market = random.randint(1, nr_market)
        price = random.random() * 100
        ins_dict[ins_name]['m' + str(market)] = price
        loop.call_soon_threadsafe(queues[instrument - 1].put_nowait, ins_name)
        if throttle:
            print('Put', ins_name)
            time.sleep(0.01)
