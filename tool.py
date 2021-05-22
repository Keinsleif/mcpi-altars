#!/usr/bin/python3

from mcpi import minecraft
import sys
import threading

mc=minecraft.Minecraft.create()


def self_block(id):
	try:
		mc.events.clearAll()
		while True:
			events=mc.events.pollBlockHits()
			if events:
				for e in events:
					x=e.pos.x
					y=e.pos.y
					z=e.pos.z
					if e.face==0:
						y=y-1
					elif e.face==1:
						y=y+1
					elif e.face==2:
						z=z-1
					elif e.face==3:
						z=z+1
					elif e.face==4:
						x=x-1
					else:
						x=x+1
					mc.setBlock(x,y,z,int(id))
	except KeyboardInterrupt:
		print()


def put_pos():
	try:
		mc.events.clearAll()
		while True:
			events=mc.events.pollBlockHits()
			[mc.postToChat("x:"+str(e.pos.x)+" y:"+str(e.pos.y)+" z:"+str(e.pos.z)) for e in events]

	except KeyboardInterrupt:
		print()

def put_block_id():
	try:
		mc.events.clearAll()
		while True:
			events=mc.events.pollBlockHits()
			[mc.postToChat(str(mc.getBlock(e.pos.x,e.pos.y,e.pos.z))) for e in events]
	except KeyboardInterrupt:
		print()


def through(r=3):
	try:
		mc.events.clearAll()
		while True:
			events=mc.events.pollBlockHits()
			for e in events:
				pos=mc.player.getPos()
				x=pos.x
				y=pos.y
				z=pos.z
				if e.face==0:
					y=y+r
				elif e.face==1:
					y=y-r
				elif e.face==2:
					z=z+r
				elif e.face==3:
					z=z-r
				elif e.face==4:
					x=x+r
				else:
					x=x-r
				mc.player.setPos(x,y,z)
	except KeyboardInterrupt:
		print()

def teleport():
	try:
		mc.events.clearAll()
		while True:
			events=mc.events.pollBlockHits()
			for e in events:
				mc.player.setTilePos(e.pos.x,e.pos.y+1,e.pos.z)

	except KeyboardInterrupt:
		print()
