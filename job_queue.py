#! /usr/bin/python

import socketio
import asyncio
import requests
import warnings
from datetime import datetime
import os
import time
from salsa_ep_h import XY2, CNC,FROM_SALSA_SIO_EVENTS, TO_SALSA_SIO_EVENTS

#===== Laser Machine Information =====
SALSA_IP = "192.168.58.172"



warnings.filterwarnings("ignore", message="Unverified HTTPS request")
sio = socketio.AsyncClient(ssl_verify=False)

#===== Helper Class =====
class job_control:
    def __init__(self, salsa_ip):
        self.salsa_ip = salsa_ip

    is_idle = True
    start_time = time.time()
    def msg_packet(self, endpoint, header, data = ""):
        msg = {
            'endpoint': endpoint,
            'header':header,
            'data': data
        }
        return msg

    async def run_lap(self):
        self.is_idle = False
        msg = {
            'mode': ''
        }
        await sio.emit(TO_SALSA_SIO_EVENTS.TO_SALSA_CONTROL,self.msg_packet(XY2.XY2_ENDPOINT, XY2.XY2_LAST_LAP_JOB, msg))
        print(f"Job Initiated:\t{datetime.now()}")
        self.start_time = time.time()

    async def wait_for_job_end(self):
        while True:
            await asyncio.sleep(0.2)
            if self.is_idle:
                minutes, seconds = divmod(time.time() - self.start_time, 60)
                formatted_time = f"{int(minutes)} min {seconds:.2f} sec"
                print(f"Duration:\t{formatted_time}")
                print(f"Job End:\t{datetime.now()}")
                print("-" * 40)
                return
    
    async def toggle_door(self, is_open: bool):
        print(f"Toggle door {is_open}")
        result = await sio.call(TO_SALSA_SIO_EVENTS.TO_SALSA_CONTROL,self.msg_packet(CNC.CNC_ENDPOINT, CNC.CNC_TOGGLE_DOOR, is_open), timeout=60)
        print(f"Toggle door result -> {result}")

        
#===== Main =====

jq = job_control(SALSA_IP)

@sio.event
async def connect():
    print('Connected to salsa')
    await jq.toggle_door(False)
    await asyncio.sleep(5)
    await jq.run_lap()
    await jq.wait_for_job_end()
    await jq.toggle_door(True)
    await asyncio.sleep(5)

    print("Finished!")
    await sio.disconnect()

@sio.event
async def disconnect():
    print('Disconnected from server')

@sio.on(FROM_SALSA_SIO_EVENTS.FROM_SALSA_ECHO)
async def on_status(data):
    header = data.get('header')
    if header == FROM_SALSA_SIO_EVENTS.FROM_SALSA_JOB_END:
        jq.is_idle = True


async def main():
    await sio.connect(f"http://{SALSA_IP}:80",transports=['websocket'],wait_timeout=90)
    await sio.wait()
    await sio.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
