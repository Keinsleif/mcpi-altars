#!/usr/bin/python3

from mcpi import minecraft
import os,sys,queue,json,time,threading


def main(mc,q,wd):
	os.chdir(wd)
	sys.path.insert(1,wd)

	rituals={}
	altar={}
	files=[os.path.splitext(i)[0] for i in os.listdir("ritual")]
	for i in files:
		if i or not r=="__pycache__":
			rituals[i]=import_module(i,"ritual")
		with open("altar/"+i,'r') as f:
			altar[i]=json.load(f)

	mc.postToChat("Welcome to Minecraft Pi Altars.")

	mc.events.clearAll()
	try:
		while q.get()==1:
			events=mc.events.pollBlockHits()
			for e in events:
				if mc.getBlock(e.pos.x,e.pos.y,e.pos.z)==247:
					al=[mc.getBlock(x,y,z) for y in range(e.pos.y,e.pos.y+3) for x in range(e.pos.x-1,e.pos.x+2) for z in range(e.pos.z-1,e.pos.z+2)]
					for i in files:
						for a in alter[i]:
							if al==alter[a]['altar']:
								mc.postToChat('Success')
								exec(altar[i][a]["function"].format(ritual="rituals['"+i+"']"))
								mc.postToChat('Stopped')
								mc.events.clearAll()
								break
						else:
							continue
						break
					else:
						mc.postToChat('Ritual not found.')
			time.sleep(0.5)
	except KeyboardInterrupt:
		print()

if __name__=="__main__":
	mc=minecraft.Minecraft.create()
	qu=queue.Queue()
	thread=threading.Thread(target=main,args=(mc,qu,os.getcwd()))
	thread.start()
	while True:
		try:
			com=input("> ")
			if com=="exit":
				qu.put(0)
				thread.join()
				sys.exit()
		except KeyboardInterrupt:
			qu.put(0)
			thread.join()
			sys.exit()
