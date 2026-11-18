# Optional live chat relay so two partners on different devices can talk.
# Run: pip install -r requirements.txt   then   python chat_server.py
import asyncio, json
import websockets

rooms = {}  # couple code -> set of connections

async def handler(ws):
    couple = None
    try:
        async for raw in ws:
            data = json.loads(raw)
            couple = data.get("couple")
            if not couple:
                continue
            rooms.setdefault(couple, set()).add(ws)
            if data.get("type") in ("msg", "avatar", "sig", "gs", "media"):
                for peer in list(rooms[couple]):
                    if peer is not ws:
                        await peer.send(raw)
    finally:
        if couple:
            rooms.get(couple, set()).discard(ws)

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765, max_size=24 * 1024 * 1024):
        print("HeartConnect chat server on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
