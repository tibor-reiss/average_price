'''Create a test stream with specified number of instruments'''

import random

number_of_instruments = 10
number_of_markets = []
for i in range(number_of_instruments):
    number_of_markets.append(random.randint(1, 3))
with open('instrument_definition', 'w') as f:
    for ins, market in enumerate(number_of_markets, start=1):
        f.write(f'{ins} {market}\n')

number_of_entries = 100000
with open('stream_from_file', 'w') as f:
    for i in range(number_of_entries):
        instrument = random.randint(1, number_of_instruments)
        market = random.randint(1, number_of_markets[instrument-1])
        f.write(f'ins{instrument} m{market} {random.random() * 100}\n')
