#!/usr/bin/python3

from mcpi import minecraft
import sys,json

mc=minecraft.Minecraft.create()

mc.events.clearAll()
while True:
	print("Click your altar.")
	events=mc.events.pollBlockHits()
	for e in events:
		if mc.getBlock(e.pos.x,e.pos.y,e.pos.z)==247:
			al=[mc.getBlock(x,y,z) for y in range(e.pos.y,e.pos.y+3) for x in range(e.pos.x-1,e.pos.x+2) for z in range(e.pos.z-1,e.pos.z+2)]
			print(al)
			yn1=input("Are you add this altar?(y/n/quit): ")
			if yn1=="n":
				continue
			elif yn1=="quit":
				sys.exit()
			name=input("Input altar name: ")
			func=input("Input altar funcution: ")
			tf=True
			while tf:
				file=input("Input altar file name: ")
				if os.path.isfile("altar/"+file):
					tf=False
				else:
					print("Invalid alter file name.")
			with open("altar/"+file,"r") as f:
				a3=json.load(f)
			a3[name]={"altar":al,"function":func}
			with open("altar/"+file,"w") as f:
				json.dump(a3,f,indent=4)
			print("Altar successful installed.")
