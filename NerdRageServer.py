#!/usr/bin/env python3

# https://aiohttp.readthedocs.io/en/stable/index.html
import aiohttp.web
import asyncio
import serial

try:
        s = serial.Serial("/dev/ttyUSB0", 115200)
except:
        print("unable to open serial port")

async def websocket_handler(request):
    ws = aiohttp.web.WebSocketResponse()
    await ws.prepare(request)

    #print('enabling pitch')
    s.write(str.encode("enable pitch\n"))
    s.write(str.encode("enable yaw\n"))

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            elif msg.json()['commandName'] == "FireGun":
                s.write(str.encode("fire gun\n"))
            elif msg.json()['commandName'] == "StopGun":
               s.write(str.encode("stop gun\n"))
            elif msg.json()['commandName'] == "FireLaser":
                s.write(str.encode("fire laser\n"))
            elif msg.json()['commandName'] == "StopLaser":
               s.write(str.encode("stop laser\n"))
            elif msg.json()['commandName'] == "MovePitchPositive":
               s.write(str.encode("move pitch cw\n"))
            elif msg.json()['commandName'] == "MovePitchNegative":
               s.write(str.encode("move pitch ccw\n"))
            elif msg.json()['commandName'] == "StopPitch":
               s.write(str.encode("stop pitch\n"))
            elif msg.json()['commandName'] == "MoveYawPositive":
               s.write(str.encode("move yaw cw\n"))
            elif msg.json()['commandName'] == "MoveYawNegative":
               s.write(str.encode("move yaw ccw\n"))
            elif msg.json()['commandName'] == "StopYaw":
               s.write(str.encode("stop yaw\n"))
            elif msg.json()['commandName'] == "Stop":
               s.write(str.encode("stop all\n"))
            elif msg.json()['commandName'] == "Home":
               s.write(str.encode("home pitch\n"))
            elif msg.json()['commandName'] == "Execute":
               s.write(str.encode(msg.json()['command']))
            else:
                print(msg.json()['commandName']);
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())


if __name__ == '__main__':
    print("Nerd Rage Server")

    # Setup server instance
    server = aiohttp.web.Application()
    server.add_routes([aiohttp.web.get('/ws', websocket_handler)])
    server.router.add_static("/", "../NerdRageApp/", show_index=True)

    # Start server
    aiohttp.web.run_app(server, port=8081)
