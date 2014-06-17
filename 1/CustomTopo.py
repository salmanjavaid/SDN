#!/usr/bin/python

'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''


from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        # Add your logic here ...

        self.k = 4

        lastSwitch = None

        switches = {}
        hosts = {}
        root = 0
        switches["switch"+str(root)] = self.addSwitch('s%s' % root)


        for i in range(0, fanout):
            switches["switch"+str(i)] = self.addSwitch('s%s' % str(i))


        for i in range(0, self.k):
            hosts["host"+str(i)] = self.addHost('h%s' % str(i), cpu=.5/2)

    
        for i in range(1, fanout):
            self.addLink(switches["switch"+str(root)], switches["switch"+str(i)], bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)


        for i in range(1, fanout):
            for j in range(0, self.k):
                print i, j
                #self.addLink(switches["switch"+str(i)], hosts["hosts"+str(j)], bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)




        
        
        


def perfTest():                    
    topos = { 'custom': ( lambda: CustomTopo() ) }
    linkopts = dict(bw=10, delay='5ms', loss=1, max_queue_size=1000, use_htb=True)
    topo = CustomTopo(linkopts1=linkopts, linkopts2=linkopts, linkopts3=linkopts, fanout=2)
    net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
    net.start()
    dumpNodeConnections(net.hosts)
    net.pingAll()
    h1, h2 = net.get('h1', 'h2')
    net.iperf((h1, h2))
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    perfTest()
