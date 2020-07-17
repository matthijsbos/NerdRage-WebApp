import aiohttp.web
import nerdrage_webapp.server

if __name__ == '__main__':
    print("Nerd Rage Server")

    # Setup server instance
    server = aiohttp.web.Application()
    server.add_routes([aiohttp.web.get('/ws', nerdrage_webapp.server.websocket_handler)])
    server.router.add_static("/", ".", show_index=True)

    # Start server
    aiohttp.web.run_app(server, port=80)
