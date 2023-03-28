Thanks and shout out to Jon Petter Skagmo.
Never spoken, but clearly knowledgable.
I'm a few years older and a native briton.

Been living with the esmart3 for a couple of years now. After owning and using an esmart2  for 18 mopnth and it failing after being maxed out for ages (main transformer failed), I've stayed with the brand. Reasoning is historic, as a computer maintenence tech I already had several UPS's of different battery voltages, which has allowed me 
to increase battery bank voltage and make the occassional mistake during learning while also keeping the cost of replacements down. That also includes death of 2 inverters/ups's that I forgot to completely isolate during nearby lightening strikes.

I dabbled at copying the comms a few years back and gave up, hibernating this winter has put me infront of the screen.

My ultimate goal is get all this into javascript so the control system can control the inverter natively.
For now my comms setup is quite unnecessarily elaborate.
I'm a big fan of serial/rs232 ports so the adaptor I use for the comms is one of these
https://www.ebay.co.uk/itm/234491472477
That goes into a 4 port duplicator (one to future control systemuse, one to ubuntu server serial port for influxdb, one another 4 port duplicator)
2nd duplicator has one port to pc com port for mysolar monitor and one port to anther pc comm port to view and capture with realterm

RJ45 pinout:
* 1: A
* 2: B
* 5,6: Ground (for powering isolated RS-485 interface)
* 7,8: 5V out (for powering isolated RS-485 interface)

Totally aware I'm treading the same path, but we do what we do right?
