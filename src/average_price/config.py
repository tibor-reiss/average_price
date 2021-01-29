from typing import Dict


def setup_instrument_dictionary(ins_dict: Dict) -> None:
    '''
    Set up the instrument dictionary containing the prices.
    Number of instruments and number of markets per instrument are provided in file.
    '''
    with open('instrument_definition', 'r') as f:
        for line in f:
            ins_number, markets = line.split()
            ins_name = 'ins' + ins_number
            if ins_name not in ins_dict:
                ins_dict[ins_name] = {}
            for i in range(int(markets)):
                ins_dict[ins_name]['m' + str(i+1)] = 0
