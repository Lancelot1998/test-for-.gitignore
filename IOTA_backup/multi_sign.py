#!/bin/python

api_2 = MultisigIota(
    adapter='http://localhost:14265',

    seed=Seed(
        b'TESTVALUE9DONTUSEINPRODUCTION99999DDWDKI'
        b'FFBZVQHHINYDWRSMGGPZUERNLEAYMLFPHRXEWRNST',
    ),
)

# You can use any starting index that you want.
# For maximum security, each index should be used only once.
gd_result = api_2.get_digests(index=42, count=1, security_level=3)