# coding=utf-8
"""
A simulated Sybil attack against blockchain.
"""
import time
import random
from config import *

peers = honest_peer + sybil_peer # all peers 
print(peers)

def peer_connection(peer_list): # initial peer distribution
    for peer in honest_peer:
        peer_list[peer] = list()
        for index in range(2):
            peer_index = random.randint(0, len(peers) - 1)
            if peers[peer_index] is not peer and peers[peer_index] not in peer_list[peer]:
                flag = 0
                for i in peer_list.values():
                    if peers[peer_index] not in i:
                        pass
                    else:
                        flag = 1
                if flag is 0:
                    peer_list[peer].append(peers[peer_index])    		

    # print(peer_list)

    # adjustment
    peer_num = dict()
    for node in peers:
        peer_num[node] = 0
        for peer in peer_list.keys():
            if peer is node:
                peer_num[node] += len(peer_list[peer])
            else:
                pass
        temp = peer_list.values()
        for i in temp:
            for j in i:
                if j is node:
                    peer_num[node] += 1

#    print(peer_list)

    for peer in honest_peer:
        if peer_num[peer] is 0:
            peer_index = random.randint(len(sybil_peer), len(peers) - 1)
            peer_list[peer].append(peers[peer_index])
            peer_num[peer] += 1
            peer_num[peers[peer_index]] += 1

#    print('\n\ninter')
#    print(peer_list)
#    print(peer_num)
#    print('inter\n\n')

    for peer in sybil_peer:
        if peer_num[peer] <= 1:
            for i in range(2):
                peer_index = random.randint(0, len(sybil_peer) - 1)
                if peer_num[peers[peer_index]] < 4:
                    flag = 0
                    for i in peer_list.values():
                        if peer not in i:
                            pass
                        else:
                            flag = 1
                    if flag is 0:
                        peer_list[peers[peer_index]].append(peer)
                        peer_num[peer] += 1
                        peer_num[peers[peer_index]] += 1

    print('-------------n--------------')
    print(peer_list)
    print('-------------n--------------')
    print(peer_num)
    print('-------------n--------------')

    return peer_list


if __name__ == '__main__':
    peer_list = dict()
    peer_list = peer_connection(peer_list)

    # peer connection
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            pass # add peer via API, including honest_peer and sybil_peer

    # partition the network
    disconnection_sybil = list()  # save the current disconnetion peers, where the item is designed as [honest_peer, sybil_peer]
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            if neighbor in sybil_peer:
                disconnection_sybil.append([peer, neighbor])
                pass # disconnect: both peer -> neighbor and neighbor -> peer

    # time interval between peer update
    # time.sleep(100)

    # peer update
    disconnection_honest = list()
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            if neighbor in honest_peer:
                peer_list[peer].remove(neighbor)
                disconnection_honest.append([peer, neighbor]) # save the current disconnection peers, where the item is designed as [honest_peer, honest_peer]
                pass # disconnect: both neighbor -> peer and neighbor -> peer

    # print('\n\n', peer_list)

    peer_list = dict()
    print(disconnection_sybil)
    print(disconnection_honest)

    peer_list = peer_connection(peer_list)
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            if neighbor in sybil_peer:
                if [peer, neighbor] not in disconnection_sybil:
                    print(peer, neighbor, 'connect via API')
                    pass # connect via API
                else:
                    # disconnection_sybil.remove([peer, neighbor])
                    print(peer, neighbor, 'connect via TCP')
                    pass # connection: both neighbor -> peer and peer -> neighbor
            if neighbor in honest_peer:
                if ([peer, neighbor] not in disconnection_honest) and ([neighbor, peer] not in disconnection_honest):
                    print(peer, neighbor, 'connect via API')
                    pass # connect via API
                else:
                    print(peer, neighbor, 'connect via TCP')
                    pass # connection； both neighbor -> peer and peer -> neighbor

    # partition the network
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            if neighbor in sybil_peer:
                if [peer, neighbor] in disconnection_sybil:
                    print(peer, neighbor, 'disconnect via TCP')
                    pass # disconnect: both peer -> neighbor and neighbor -> peer
                else:
                    disconnection_sybil.append([peer, neighbor])
                    print(peer, neighbor, 'disconnect via TCP2')
                    pass # disconnect: both peer -> neighbor and neighbor -> peer

    # time.sleep(100)

    # peer update
    for peer in peer_list.keys():
        for neighbor in peer_list[peer]:
            if neighbor in honest_peer:
                if ([peer, neighbor] not in disconnection_honest) and ([neighbor, peer] not in disconnection_honest):
                    peer_list[peer].remove(neighbor)
                    disconnection_honest.append([peer, neighbor]) # save the current disconnection peers, where the item is designed as [honest_peer, honest_peer]
                    pass # disconnect: both neighbor -> peer and neighbor -> peer
                else:
                    pass # disconnect: both neighbor -> peer and neighbor -> peer

    peer_list = dict()
    print(disconnection_sybil)
    print(disconnection_honest)
