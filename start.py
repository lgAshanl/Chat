#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import logging

from server import ChatServer
from client import ChatClient

print("dasdas")
logging.basicConfig(level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument('--client', action='store_true')
parser.add_argument('--server', action='store_true')
parser.add_argument('-p', '--port', type=int, default=8077)
parser.add_argument('-s', '--addr', type=str, default='0.0.0.0')
args = parser.parse_args()

if args.client:
	ChatClient(host=args.addr, port=args.port).start()
elif args.server:
	ChatServer(host=args.addr, port=args.port).start()
