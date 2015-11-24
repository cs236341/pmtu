from router import Router

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from time import sleep


import os

sleepytime = 3

class PmtuTopo ( Topo ):

    def build ( self ):
    
        r1 = self.addSwitch ('R1', cls=Router )
        r2 = self.addSwitch ('R2', cls=Router )
        r3 = self.addSwitch ('R3', cls=Router )

        for h, s in [ (r1, r2), (r2, r3) ]:
            self.addLink( h, s )

#        s1 = self.addSwitch ('s1')

def run():
    #clean previous run
    
    os.system("rm -f  /tmp/*.pid logs/*")
    os.system("mn -c >/dev/null 2>&1")
    os.system("killall -9 zebra ripd > /dev/null 2>&1")

    topo = PmtuTopo()
    net = Mininet( topo=topo )
    net.start()
    
    for router in net.switches:
        router.cmd("sysctl -w net.ipv4.ip_forward=1")
        router.waitOutput()

    #Waiting (sleepytime) seconds for sysctl changes to take effect..
    sleep(sleepytime)


    net.get('R1').initZebra('conf/zebra-R1.conf')
    router.waitOutput()
    net.get('R1').initRipd('conf/ripd-R1.conf')
    router.waitOutput()
    net.get('R2').initZebra('conf/zebra-R2.conf')
    router.waitOutput()
    net.get('R2').initRipd('conf/ripd-R2.conf')
    router.waitOutput()
    net.get('R3').initZebra('conf/zebra-R3.conf')
    router.waitOutput()
    net.get('R3').initRipd('conf/ripd-R3.conf')
    router.waitOutput()
    CLI( net )
    net.stop()

if __name__== '__main__':
    setLogLevel( 'info' )
    run()
