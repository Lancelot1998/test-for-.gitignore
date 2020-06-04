# coding=utf-8
"""
Example script that shows how to use PyOTA to send a transfer to an address.
"""
from argparse import ArgumentParser
from sys import argv

from iota import (
  __version__,
  Address,
  Iota,
  ProposedTransaction,
  Tag,
  TryteString,
)
from six import text_type
import time

def main():
    # Ensure seed is not displayed in cleartext.
    seed = 'SEED99999999999999999999999999999999999999999999999999999999999999999999999999999'
    # Create the API instance.
    api = Iota("http://localhost:14265", seed)
    t1 = time.time()
    print('Starting transfer.')
    # For more information, see :py:meth:`Iota.send_transfer`.
    api.send_transfer(
        depth=3,
        # One or more :py:class:`ProposedTransaction` objects to add to the
        # bundle.
        transfers=[
            ProposedTransaction(
                # Recipient of the transfer.
                address=Address('RECEIVINGWALLETADDRESSGOESHERE9WITHCHECKSUMANDSECURITYLEVELB999999999999999999999999999999'),

                # Amount of IOTA to transfer.
                # By default this is a zero value transfer.
                value=42,

                # Optional tag to attach to the transfer.
                tag=Tag(b'EXAMPLE'),

                # Optional message to include with the transfer.
                message=TryteString.from_string('Hello World!'),
            ),
        ],
        min_weight_magnitude=9,
        security_level=2
    )
    print('Transfer complete.', time.time() - t1)

if __name__ == '__main__':
    i = 0
    for i in range(10000):
    	main()
