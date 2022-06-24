#!usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def index(request):
    return web.Response(body=b'<h1>AWESON</h1>', content_type='text/html')

def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host='127.0.0.1', port='9000')
    logging.info('server http://127.0.0.1:9000 is running...')

if __name__ == "__main__":
    main()
