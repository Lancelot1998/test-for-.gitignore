NODES=['193.112.213.80', '106.53.86.163']
partition_cmd = './partition.sh {} {} {} &'
api_cmd = 'curl -H \'X-IOTA-API-VERSION: 1.4\' -d \'{{\"command\":\"addNeighbors\", \"uris\":[\"tcp://{}:15600\"]}}\' http://localhost:14265 &'
disconnection_cmd = './disconnection.sh {} {} &'
connection_cmd = './connection.sh {} {} &'
disconnection_single_cmd = './disconnection_single.sh {} {} &'
TIMEOUT=200

honest_peer = list() # the list of honest peer
honest_peer.append('172.18.127.129')
honest_peer.append('172.18.127.128')
honest_peer.append('172.18.127.127')
honest_peer.append('172.18.127.126')
honest_peer.append('172.18.127.125')

sybil_peer = list()  # the IP address of Sybil attackers
sybil_peer.append('172.18.127.124')
sybil_peer.append('172.18.127.123')
sybil_peer.append('172.18.127.122')
sybil_peer.append('172.18.127.121')
sybil_peer.append('172.18.127.120')
