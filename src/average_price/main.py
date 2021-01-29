import asyncio
from copy import deepcopy
import random
import threading
import time

from async_set_queue import SetQueue
from config import setup_instrument_dictionary
from db import create_table, setup_database, upsert
from stream import stream_from_thread


async def calc(db, i, q, throttle=False):
    while True:
        #print('Running...', i)
        item = await q.get()
        ins = deepcopy(INS_DICT[item])
        avg_price = sum(ins.values()) / len(ins)
        await upsert(db, 'HighScores', ['ins', 'price'], [item, avg_price], 'ins')
        if throttle:
            #await asyncio.sleep(random.random() / 5 * (i+1))
            await asyncio.sleep(0.5 * (i+1))
        print('Calculated', i, avg_price, ins)


if __name__ == '__main__':
    print('START...')

    INS_DICT = {}
    Q = []

    setup_instrument_dictionary(INS_DICT)
    nr_ins = len(INS_DICT)
    loop = asyncio.get_event_loop()

    db = loop.run_until_complete(setup_database('sqlite:///example.db'))
    query = """CREATE TABLE HighScores (ins VARCHAR(10) PRIMARY KEY, price DOUBLE)"""
    loop.run_until_complete(create_table(db, query))
    print(db)
    for i in range(10):
        loop.run_until_complete(upsert(db, 'HighScores', ['ins', 'price'], ['bla', 1.1], 'ins'))

    for i in range(0, nr_ins):
        Q.append(SetQueue())
        loop.create_task(calc(db, i, Q[i], True))

    # Thread for stream
    th_stream = threading.Thread(target=stream_from_thread, args=(loop, INS_DICT, Q, False, ))
    th_stream.start()
    
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('INTERRUPTED')
        th_stream.join()
