this is a PMTU demo for the tutorial

the topology is 

R1 ------------------  R2 ---------------------- R3
1.1.1.1		       2.2.2.2			 3.3.3.3
11.0.1.1	11.0.1.2-11.0.2.1		 11.0.2.1
      MTU = 1500		MTU = 1400


you need to configure mtu  = 1400 manually
use ifconfig {interface} mtu 1400 up

just open R1 terminal and wireshark
run ping -s 1472 -M want 3.3.3.3

