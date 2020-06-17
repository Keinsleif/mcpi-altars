#!/usr/bin/python3

from mcpi import minecraft
import os
import sys
import queue
import json


def main(mc,q,wd):
	os.chdir(wd)
	sys.path.insert(1,wd)
	d1=os.listdir("ritual")
	d2=""
	for i in d1:
		r=i.split(".")[0]
		if r or not r=="__pycache__":
			d2=d2+"from ritual import "+r+"\n"
	exec(d2)

	with open("data/alter",'r') as f:
#		dalter=f.read()
#	dalter=dalter.replace("\n","")
#	exec("alter="+dalter)
		alter=json.load(f)

	e1="if False:\n	print('Error!')\n"
	for i in alter:
		e1=e1+"elif al=="+str(alter[i]["alter"])+":\n	mc.postToChat('Success')\n	"+alter[i]["function"]+"\n	mc.postToChat('Stopped')\n	mc.events.clearAll()\n"
	e1=e1+"else:\n	mc.postToChat('Ritual not found.')"

	mc.postToChat("Welcome to Minecraft Pi Alters.")

	mc.events.clearAll()
	try:
		while q.get()==1:
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

if __name__=="__main__":
	mc=minecraft.Minecraft.create()
	qu=queue.Queue()
	main(mc,qu,os.getcwd())

