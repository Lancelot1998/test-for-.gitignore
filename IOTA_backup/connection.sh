#!/bin/bash

nodeX=$1
nodeY=$2
  
argErr="Args Error: Usage ./killconn <Node 1 ip/name> <Node 2 ip/name>"

if (($#!=2)); then
echo $argErr
exit 
fi

echo NodeX: $nodeX
echo NodeY: $nodeY

ssh ubuntu@$nodeX sudo iptables -w -D INPUT -p tcp -s $nodeY -j DROP
ssh ubuntu@$nodeY sudo iptables -w -D INPUT -p tcp -s $nodeX -j DROP

