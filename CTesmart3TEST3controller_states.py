#!/usr/bin/python3
# -*- coding: utf-8 -*-

import CTesmart
import time
import datetime

def handle_data(d):
        # Correct error in readings
        d['bat_volt'] *= 1.00
        d['load_volt'] *= 1.00
        # Only correct if reading is not zero
        if d['chg_cur']:
                d['chg_cur'] += 1.00

        # chg_power uses uncorrected voltage/current, so recalculate
        actual_power = d['bat_volt']*d['chg_cur']

        print('Timestamp: {:%d-%b-%Y %H:%M:%S}'.format(datetime.datetime.now()))
        print("Solar",d['chg_mode'],"State " "%s" % (CTesmart.DEVICE_MODE[d['chg_mode']]))
        print("PV %.1f V" % (d['pv_volt']))
        print("Batt %.1f V" % (d['bat_volt']))
        print("Watts %.1f W" % (actual_power))
        print("BCurr %.1f A" % (d['chg_cur']))
        print("")
        print("IntTemp %.1f C" % (d['int_temp']))
        print("BattTemp %.1f C" % (d['bat_temp']))
        print("")
        print("")

e = CTesmart.esmart()
e.open("/dev/ttyUSB1")
e.set_callback(handle_data)

while 1:
        try:
                e.tick()
                time.sleep(0.001)
        except KeyboardInterrupt:
                break
