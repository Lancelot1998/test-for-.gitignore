# coding=utf-8
"""
Example script that shows how to use PyOTA to send a transfer to an address.
"""
from argparse import ArgumentParser
from sys import argv
from multiprocessing import Process
import time
from iota import (
  __version__,
  Address,
  Iota,
  ProposedTransaction,
  Tag,
  TryteString,
)
from six import text_type

seed = 'SEED99999999999999999999999999999999999999999999999999999999999999999999999999999'
api = Iota("http://localhost:14265", seed) 


def send(value):
    ti = time.time()
    api.send_transfer(
        depth=3,        
        transfers=[
            ProposedTransaction(
                # Recipient of the transfer.
                address=Address("RECEIVINGWALLETADDRESSGOESHERE9WITHCHECKSUMANDSECURITYLEVELB999999999999999999999999999999"),
                value=value,

                # Optional tag to attach to the transfer.
                tag=Tag(b'KITTEHS'),

                # Optional message to include with the transfer.
                message=TryteString.from_unicode('thx fur cheezburgers'),
            ),
        ],
        min_weight_magnitude=9
    )
    print(time.time() - ti)


def main():
    for i in range(20000):
        if i % 5 is 0:
            send(1)
        else:
            send(0)
       

if __name__ == '__main__':
    for i in range(2):
        Process(target=main, args=()).start()