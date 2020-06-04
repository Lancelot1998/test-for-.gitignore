# coding=utf-8
"""
Example of how to use PyOTA's multisig feature.
This script will generate a multisig address using private keys from
three different seeds, prepare a bundle, sign the inputs, and then
finally broadcast the transactions to the Tangle.
References:
  - https://github.com/iotaledger/wiki/blob/master/multisigs.md
"""

from __future__ import absolute_import, division, print_function, \
    unicode_literals

from typing import List

from iota import Transaction, Address, Bundle, BundleValidator, ProposedTransaction, Tag, \
    TransactionTrytes, TryteString
from iota.crypto.types import Digest, PrivateKey, Seed
from iota.multisig import MultisigIota
from iota.multisig.types import MultisigAddress
import time

"""
step1
"""
bundle_trans = Transaction(hash_="AVPVVUUNZDTOHNZWIJVNSVQVOWXFGM9SKJSWAPGWNJCNDFPKSTQETASWTROWCSSTFLRFVRYFTYBD99999",  # type: Optional[TransactionHash]
                           signature_message_fragment="",  # type: Optional[Fragment]
                           address="FJKKSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX",  # type: Address
                           value=5,  # type: int
                           timestamp=1574903736,  # type: int
                           current_index=0,  # type: Optional[int]
                           last_index=3,  # type: Optional[int]
                           bundle_hash=TryteString.random(81),
                           trunk_transaction_hash="ZQLLKWWTPNXXKYHWXRIQZKRG9MLW9DHFVXHPGFYACGOUGPWENMEC9ZOWRUORUWEFBEREGNVPNRHXZ9999",  # type: Optional[TransactionHash]
                           branch_transaction_hash="DQEUSNVVGKZUMYXKDUIEDYHCDVVAXGWU9RZUGOGFCFSTDVJEIWIETEGLKUIEKMKKFOKHVGUAELCMWE999",  # type: Optional[TransactionHash]
                           tag="QA9999999999999999999999999",  # type: Optional[Tag]
                           attachment_timestamp=1574903776620,  # type: Optional[int]
                           attachment_timestamp_lower_bound=0,  # type: Optional[int]
                           attachment_timestamp_upper_bound=3812798742493,  # type: Optional[int]
                           nonce="LSJDSJRHNOHMWNRNJFHEORVHMXY",  # type: Optional[Nonce]
                           legacy_tag=None  # type: Optional[Tag]
                )
bundle_trans_2 = Transaction(hash_="ZQLLKWWTPNXXKYHWXRIQZKRG9MLW9DHFVXHPGFYACGOUGPWENMEC9ZOWRUORUWEFBEREGNVPNRHXZ9999",  # type: Optional[TransactionHash]
                             signature_message_fragment="",  # type: Optional[Fragment]
                             address="FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX",  # type: Address
                             value=-2779530283277761,  # type: int
                             timestamp=1574903736,  # type: int
                             current_index=1,  # type: Optional[int]
                             last_index=3,  # type: Optional[int]
                             bundle_hash=TryteString.random(81),
                             trunk_transaction_hash="RCANCATOVLSSPJFXMZBKEODVYXNKTKXRM9WRHPX9YSZJXVRUMCOMGZOLJWWWEVECYCGOKPOELDQLZ9999",  # type: Optional[TransactionHash]
                             branch_transaction_hash="DQEUSNVVGKZUMYXKDUIEDYHCDVVAXGWU9RZUGOGFCFSTDVJEIWIETEGLKUIEKMKKFOKHVGUAELCMWE999",  # type: Optional[TransactionHash]
                             tag="QA9999999999999999999999999",  # type: Optional[Tag]
                             attachment_timestamp=1574903769168,  # type: Optional[int]
                             attachment_timestamp_lower_bound=0,  # type: Optional[int]
                             attachment_timestamp_upper_bound=3812798742493,  # type: Optional[int]
                             nonce="CVREKSTNCZMMXIEWQJLPADWVEBB",  # type: Optional[Nonce]
                             legacy_tag=None  # type: Optional[Tag]
                )

bundle_trans_3 = Transaction(hash_="RCANCATOVLSSPJFXMZBKEODVYXNKTKXRM9WRHPX9YSZJXVRUMCOMGZOLJWWWEVECYCGOKPOELDQLZ9999",  # type: Optional[TransactionHash]
                             signature_message_fragment="",  # type: Optional[Fragment]
                             address="FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX",  # type: Address
                             value=-2779530283277761,  # type: int
                             timestamp=1574903736,  # type: int
                             current_index=2,  # type: Optional[int]
                             last_index=3,  # type: Optional[int]
                             bundle_hash=TryteString.random(81),
                             trunk_transaction_hash="RCANCATOVLSSPJFXMZBKEODVYXNKTKXRM9WRHPX9YSZJXVRUMCOMGZOLJWWWEVECYCGOKPOELDQLZ9999",  # type: Optional[TransactionHash]
                             branch_transaction_hash="DQEUSNVVGKZUMYXKDUIEDYHCDVVAXGWU9RZUGOGFCFSTDVJEIWIETEGLKUIEKMKKFOKHVGUAELCMWE999",  # type: Optional[TransactionHash]
                             tag="QA9999999999999999999999999",  # type: Optional[Tag]
                             attachment_timestamp=1574903769168,  # type: Optional[int]
                             attachment_timestamp_lower_bound=0,  # type: Optional[int]
                             attachment_timestamp_upper_bound=3812798742493,  # type: Optional[int]
                             nonce="CVREKSTNCZMMXIEWQJLPADWVEBB",  # type: Optional[Nonce]
                             legacy_tag=None  # type: Optional[Tag]
                )

bundle_trans_4 = Transaction(hash_="RCANCATOVLSSPJFXMZBKEODVYXNKTKXRM9WRHPX9YSZJXVRUMCOMGZOLJWWWEVECYCGOKPOELDQLZ9999",  # type: Optional[TransactionHash]
                             signature_message_fragment="",  # type: Optional[Fragment]
                             address="FJHSSHBZTAKQNDTIKJYCZBOZDGSZANCZSWCNWUOCZXFADNOQSYAHEJPXRLOVPNOQFQXXGEGVDGICLMOXX",  # type: Address
                             value=-2779530283277761,  # type: int
                             timestamp=1574903736,  # type: int
                             current_index=3,  # type: Optional[int]
                             last_index=3,  # type: Optional[int]
                             bundle_hash=TryteString.random(81),
                             trunk_transaction_hash="RCANCATOVLSSPJFXMZBKEODVYXNKTKXRM9WRHPX9YSZJXVRUMCOMGZOLJWWWEVECYCGOKPOELDQLZ9999",  # type: Optional[TransactionHash]
                             branch_transaction_hash="DQEUSNVVGKZUMYXKDUIEDYHCDVVAXGWU9RZUGOGFCFSTDVJEIWIETEGLKUIEKMKKFOKHVGUAELCMWE999",  # type: Optional[TransactionHash]
                             tag="QA9999999999999999999999999",  # type: Optional[Tag]
                             attachment_timestamp=1574903769168,  # type: Optional[int]
                             attachment_timestamp_lower_bound=0,  # type: Optional[int]
                             attachment_timestamp_upper_bound=3812798742493,  # type: Optional[int]
                             nonce="CVREKSTNCZMMXIEWQJLPADWVEBB",  # type: Optional[Nonce]
                             legacy_tag=None  # type: Optional[Tag]
                )
            
trans = list()
trans.append(bundle_trans)
trans.append(bundle_trans_2)
trans.append(bundle_trans_3)
trans.append(bundle_trans_4)
print('\n in processing bundle')
bundle = Bundle(transactions=trans)
print(bundle.transactions[1].signature_message_fragment)
print('bundle creation is finished\n')
##
# Create digest 1 of 3.
#
# noinspection SpellCheckingInspection
api_1 = MultisigIota(
    adapter='http://localhost:14265',

    seed=Seed(
        b'TESTVALUE9DONTUSEINPRODUCTION99999XKMYQP'
        b'OIFGQSMIIWCQVMBSOKZASRQOFSIUSSHNDKVL9PJVS',
    ),
)

gd_result = api_1.get_digests(
    # Starting key index.
    index=0,

    # Number of digests to generate.
    count=1,

    # Security level of the resulting digests.
    # Must be a value between 1 (faster) and 3 (more secure).
    security_level=3,
)

# ``get_digests`` returns a dict which contains 1 or more digests,
# depending on what value we used for ``count``.
digest_1 = gd_result['digests'][0]  # type: Digest
print(digest_1)

"""
Step 4:  Sign the inputs.
Note that we must apply signatures in the same order as when we created
the multisig address!
This step normally happens on separate computers, so that participants
don't have to share their private keys (except when doing m-of-n).
https://github.com/iotaledger/wiki/blob/master/multisigs.md#how-m-of-n-works
For this example, the structure of the bundle looks like this:
- Transaction 0:  Spend IOTAs.
- Transactions 1-8:  Transactions that will hold the signature
  fragments for the multisig input:
  - 1-3:  Generated from ``digest_1`` (security level 3).
  - 4-6:  Generated from ``digest_2`` (security level 3).
  - 7-8:  Generated from ``digest_3`` (security level 2).
Note that transactions 1-8 don't have signatures yet; we need the
corresponding private keys in order to create those!
"""

# Note that we must use the same parameters that we provided to the
# ``get_digests`` method, in order to generate the correct value to
# sign the input!
gpk_result = api_1.get_private_keys(index=0, count=1, security_level=3)
private_key_1 = gpk_result['keys'][0]  # type: PrivateKey
t1 = time.time()
a = private_key_1.sign_input_transactions(bundle, 1)
print(time.time() - t1)
print(bundle.transactions[1].signature_message_fragment)
