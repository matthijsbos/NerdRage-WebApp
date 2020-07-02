#!/usr/bin/env python3

# https://aiohttp.readthedocs.io/en/stable/index.html
import aiohttp.web

if __name__ == '__main__':
    print("Nerd Rage Server")

    # Setup server instance
    server = aiohttp.web.Application()
    server.router.add_static("/", ".", show_index=True)

    # Start server
    aiohttp.web.run_app(server, port=8080)
