#!/usr/bin/env python
from mininet.net  import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli  import CLI
from mininet.log  import setLogLevel, info
from mininet.link import Link, TCLink, Intf
from subprocess   import call

def sample():
    
#=====================================================
#Add host or Node to Mininet
#=====================================================
   net = Mininet(topo=None,
                 build=False,
                 ipBase='127.0.0.1',
                 link=TCLink)
   info('*** Adding controller\n')
   h1  = net.addHost('h1')
   h2  = net.addHost('h2')
   h3  = net.addHost('h3') 
   h4  = net.addHost('h4') # H4 adalah switch
   h5  = net.addHost('h5') # H5 adalah route Gateway
#====================================================
#create link to connecting all node
#====================================================
   Link(h1, h4)
   Link(h2, h4)
   Link(h3, h4)
   Link(h4, h5)
   net.build()
#====================================================
# remove all default address on each node interface
#====================================================
   h1.cmd("ifconfig h1-eth0 0")
   h2.cmd("ifconfig h2-eth0 0")
   h3.cmd("ifconfig h3-eth0 0")
   h4.cmd("ifconfig h4-eth0 0")
   h4.cmd("ifconfig h4-eth1 0")
   h4.cmd("ifconfig h4-eth2 0")
   h4.cmd("ifconfig h4-eth3 0")
   h5.cmd("ifconfig h5-eth0 0")

#====================================================
# add virtual subintervace interface on switch
#====================================================
   h4.cmd("vconfig add h4-eth3 10")
   h4.cmd("vconfig add h4-eth3 20")
   h4.cmd("vconfig add h4-eth3 30")
#====================================================
#set administartife interface to be UP
#====================================================
   h4.cmd("ifconfig h4-eth3.10 up")
   h4.cmd("ifconfig h4-eth3.20 up")
   h4.cmd("ifconfig h4-eth3.30 up")
#====================================================
#set virtual interface on router
#====================================================
   h5.cmd("vconfig add h5-eth0 10")
   h5.cmd("vconfig add h5-eth0 20")
   h5.cmd("vconfig add h5-eth0 30")
#===================================================
# set VLAN (vlan10 and 20) on Switch
#===================================================
   h4.cmd("brctl addbr vlan10")
   h4.cmd("brctl addbr vlan20")
   h4.cmd("brctl addbr vlan30")
#===================================================
# Assign vlan to switch Interface facing to host
#===================================================
   h4.cmd("brctl addif vlan10 h4-eth0")
   h4.cmd("brctl addif vlan20 h4-eth1")
   h4.cmd("brctl addif vlan30 h4-eth2")
#==================================================
#assign vlan to interface facing to router
#==================================================
   h4.cmd("brctl addif vlan10 h4-eth3.10")
   h4.cmd("brctl addif vlan20 h4-eth3.20")
   h4.cmd("brctl addif vlan30 h4-eth3.30")
#==================================================
#bring up vlan 10 and vlan 20 on switch
#==================================================
   h4.cmd("ifconfig vlan10 up")
   h4.cmd("ifconfig vlan20 up")
   h4.cmd("ifconfig vlan30 up")
#==================================================
#enable forward IP function on router
#==================================================
   h5.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")
#=================================================
#config IP address to virtual subinterface router
#=================================================
   h5.cmd("ifconfig h5-eth0.10 10.1.1.254 netmask 255.255.255.0")
   h5.cmd("ifconfig h5-eth0.20 10.1.2.254 netmask 255.255.255.0")
   h5.cmd("ifconfig h5-eth0.30 10.1.3.254 netmask 255.255.255.0")
#=================================================
#config IP address on all host h1,h2 and H3
#=================================================
   h1.cmd("ifconfig h1-eth0 10.1.1.5 netmask 255.255.255.0")
   h2.cmd("ifconfig h2-eth0 10.1.2.5 netmask 255.255.255.0")
   h3.cmd("ifconfig h3-eth0 10.1.3.5 netmask 255.255.255.0")
#=================================================
#config default gateway  of host h1 and h2
#=================================================  
   h1.cmd("ip route add default via 10.1.1.254 dev h1-eth0")
   h2.cmd("ip route add default via 10.1.2.254 dev h2-eth0")
   h3.cmd("ip route add default via 10.1.3.254 dev h3-eth0")
   CLI(net)
   net.stop

if __name__== '__main__':
     setLogLevel('info')
     sample()

