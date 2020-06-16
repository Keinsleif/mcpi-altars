#!/usr/bin/python3

from mcpi import minecraft
import sys

mc=minecraft.Minecraft.create()

mc.events.clearAll()
print("Click your ritual.")
while True:
	events=mc.events.pollBlockHits()
	for e in events:
		if mc.getBlock(e.pos.x,e.pos.y,e.pos.z)==247:
			al=[]
			for y in range(e.pos.y,e.pos.y+3):
				for x in range(e.pos.x-1,e.pos.x+2):
					for z in range(e.pos.z-1,e.pos.z+2):
						al.append(mc.getBlock(x,y,z))
			print(al)
			yn1=input("Are you add this ritual?(y/n/quit):")
			if yn1=="n":
				continue
			elif yn1=="quit":
				sys.exit()
			yn2=input("Input ritual funcution:")
			with open("data/alter","r") as f:
				a3=f.read()
			a3=a3.replace("\n","")
			exec("a4="+a3)
			a4.append([al,yn2])
			with open("data/alter","w") as f:
				f.write(str(a4)+"\n")
			print("Ritual successful installed.")
			print("Click your ritual.")
