def ritual_block(mc,alter,id,status=0):
	while True:
		events=mc.events.pollBlockHits()
		for e in events:
			if e.pos.x==alter.pos.x and e.pos.y==alter.pos.y and e.pos.z==alter.pos.z:
				return
			pos=[e.pos.x,e.pos.y,e.pos.z]
			if e.face==0:
				pos[1]-=1
			elif e.face==1:
				pos[1]+=1
			elif e.face==2:
				pos[2]-=1
			elif e.face==3:
				pos[2]+=1
			elif e.face==4:
				pos[0]-=1
			else:
				pos[0]+=1
			mc.setBlock(pos[0],pos[1],pos[2],id,status)


def through(mc,alter,r=3):
	mc.events.clearAll()
	while True:
		events=mc.events.pollBlockHits()
		for e in events:
			if e.pos.x==alter.pos.x and e.pos.y==alter.pos.y and e.pos.z==alter.pos.z:
				return
			pos=mc.player.getPos()
			x=pos.x
			y=pos.y
			z=pos.z
			if e.face==0:
				y=y+3
			elif e.face==1:
				y=y-3
			elif e.face==2:
				z=z+r
			elif e.face==3:
				z=z-r
			elif e.face==4:
				x=x+r
			else:
				x=x-r
			mc.player.setPos(x,y+0.2,z)

