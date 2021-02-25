import asyncio
import websockets
connected = set()

#async def echo(websocket, path):
#    async for message in websocket:
#        connected.add(websocket)
#
#        await websocket.send(message)
async def send_two(websocket, path, message):
     for socket in connected:
        if socket != websocket:
            await socket.send(message)

async def handler(websocket, path):
    # Register.
    connected.add(websocket)
    async for message in websocket:
        await send_two(websocket,path,message)
        #await asyncio.wait([ws.send("Hello!") for ws in connected])
        #await asyncio.sleep(5)
        #await hell()





#start_server = websockets.serve(echo, "185.70.196.171", 4710)
start_server = websockets.serve(handler, "185.70.196.171", 4710)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
