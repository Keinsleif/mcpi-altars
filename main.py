#!/usr/bin/python3

from mcpi import minecraft
import os


d1=os.listdir("ritual")
#d1.remove("__pycache__")
d2=""
for i in d1:
	r=i.split(".")[0]
	if r or not r=="__pycache__":
		d2=d2+"from ritual import "+r+"\n"
exec(d2)

mc=minecraft.Minecraft.create()
with open("data/alter",'r') as f:
	dalter=f.read()
dalter=dalter.replace("\n","")
exec("alter="+dalter)
e1="if False:\n	print('Error!')\n"
for i in alter:
	e1=e1+"elif al=="+str(i[0])+":\n	mc.postToChat('Success')\n	"+i[1]+"\n	mc.postToChat('Stopped')\n	mc.events.clearAll()\n"
e1=e1+"else:\n	mc.postToChat('Ritual not found.')"

print("Welcome to Minecraft Pi Alters.")

mc.events.clearAll()
try:
	while True:
		events=mc.events.pollBlockHits()
		for e in events:
			if mc.getBlock(e.pos.x,e.pos.y,e.pos.z)==247:
				al=[]
				for y in range(e.pos.y,e.pos.y+3):
					for x in range(e.pos.x-1,e.pos.x+2):
						for z in range(e.pos.z-1,e.pos.z+2):
							al.append(mc.getBlock(x,y,z))
				exec(e1)
except KeyboardInterrupt:
	print()
