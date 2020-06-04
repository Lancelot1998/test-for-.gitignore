from __future__ import absolute_import, division, print_function, \
    unicode_literals

import iota
from pprint import pprint
import time

# Generate a random seed.
myseed = 'SEED99999999999999999999999999999999999999999999999999999999999999999999999999999'
# Get an address generator.
addres_generator = iota.crypto.addresses.AddressGenerator(myseed)

# Instantiate API. Note the `local_pow=True` argument.
# This will cause PyOTA to do proof-of-work locally,
# by using the pyota-pow extension package. (if installed)
# Find it at: https://pypi.org/project/PyOTA-PoW/
api = iota.Iota("https://nodes.thetangle.org:443",myseed,local_pow=True)

# Generate two addresses
addys = addres_generator.get_addresses(1, count=2)
pprint('Generated addresses are:')
pprint(addys)
transaction = list()
# Preparing transactions
for i in range(10):
	pt = iota.ProposedTransaction(address = iota.Address(addys[0]),
                              	  message = iota.TryteString.from_unicode('Tx1: The PoW for this transaction was done by Pyota-Pow.'),
                                  tag     = iota.Tag(b'LOCALATTACHINTERFACE99999'), # Up to 27 trytes
                                  value   = 0)
	transaction.append(pt)

print('packaged ok')
# `send_transfer` will take care of the rest
for i in range(10):
	t1 = time.time()
	response = api.send_transfer([transaction[i]])
	print(time.time() - t1)
