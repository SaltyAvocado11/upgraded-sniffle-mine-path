import random
import time
CT=0
dtime=0
realhealth=2
r = 0


i = [ 0 , 0 , 0 , 0 , 0]
#_ =[ 0 , 1 , 2 , 3]
#i = [ STICKS , LOGS , PLANKS , COBBLE , Iron]

d = [ 0 , 0 , 0 , 0]
#d = [Pickaxe , Sword, Sovel , Axe]
# 1=WOOD 2=STONE 3=IRON

f = [ 0 , 0 , 0]
#f = [Rotten Flesh , Bones , Steak]

o = [0 , 0]
#o = [Coal , Iron Ore]


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD
def overworld():

	global dtime

	print ('\n {OUTSIDE}.')
	choice = input('>chop< OR >mine< OR >craft<? ')
	choice = str(choice)
	if choice == 'chop':
		trees()
	elif choice == 'mine':
		mine()
	elif choice == 'i':
		invintory()
	elif choice == 'd':
		hud()
	elif choice == 't':
		atime()
	elif choice == 'o':
		ores()
	elif choice == 'addtime':
		dtime += 5
		if dtime >=10 and dtime <= 25:
			night()
		else:
			overworld()
	elif choice == 'h':
		health()
	elif choice == 'f':
		food()
	elif choice == 'craft':
		craft()
	elif choice == 'cancel':
		print('Thanks for Playing')
	elif choice == 'givesword':
		d[1]+=1
		print('{}'.format(d))
		overworld()
	else:
		overworld()
	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT

def night():

	global dtime
	global realhealth
	global strat
	global livesLost

	while dtime >=10 and dtime < 25:
		monster = random.randint(1,5)
		if monster == 1: #ZOMBIE
				print('\nZOMBIE attacks')
				fightMonster()
		elif monster == 2: #SKELETON
				print('\nSKELETON attacks')
				fightMonster()
		elif monster == 3: #CREEPER
				print('\nCREEPER attacks')
				fightMonster()
	#SAFE
		elif monster == 4 or monster == 5:
			print('\n SAFE')
			
			strat = input ('____? ')
			if strat == 'run':
				timepassed = random.randint(2,5)
				dtime += timepassed
				night()
			if strat == 'hide':
				timePassedTierI = random.randint(1,3)
				if timePassedTierI == 1:
					timepassed = random.randint(2,8)
					dtime += timepassed
					night()
				if timePassedTierI == 2:
					timepassed = random.randint(4,6)
					dtime += timepassed
					night()
				if timePassedTierI == 3:
					timepassed = random.randint(3,7)
					dtime += timepassed
					night()
	dtime = 0
	overworld()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#FIGHT DEM MONSTERS

def fightMonster():
	global realhealth
	global livesLost
	global monster
	global dtime

	strat = input('_____? ')
	live = random.randint(1,5)
#RUN AWAY
	if strat == 'run' and live != 4:
		print ('You LIVE')
		dtime += 1
		night()
	if strat == 'fight' and live !=4:
#FIGHT (NO SWORD)
		if d[1] == 0:
			print ('You need a SWORD to fight.')
			live = random.randint(1,5)
			if live == 3: #or live == 2:
				print ('You LIVE')
				# global monster
				# if monster == 1:
				# 	monsterDrops = random.randint(1,3)
				# 	print ('{} Rotten Flesh'.format(monsterDrops))


				dtime += 1
				night()
			else:
				livesLost = 0
				livesLost = random.randint(2,7)
				if livesLost >= realhealth:
					die()
				else:
					print('- {} HP'.format(livesLost))
					realhealth -= livesLost
					print ('{} HP'.format(realhealth))
					night()
#FIGHT WITH SWORD
		elif d[1] == 1:
			if live == 1:
				livesLost = 0
				livesLost = random.randint(3,8)
				if livesLost >= realhealth:
					die()
				else:
					('- {} HP'.format(livesLost))
					realhealth -= livesLost
					print ('{} HP'.format(realhealth))
					night()
			else:
				print ('You LIVE')
				night()
#LOST SOME LIFE
	elif live == 4:
		livesLost = 0
		livesLost = random.randint(3,8)
		if livesLost >= realhealth:
			die()
		else:
			print('- {} HP'.format(livesLost))
			realhealth -= livesLost
			print ('{} HP'.format(realhealth))
			night()
#ASK FOR THE TIME
	elif strat == 't':
			print('{}'.format(time))
			night()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE

def die():
	global dtime
	global r
	global repeat
	global i

	dtime += 3
	print ('You DIED')

	stuffLost = random.randint(3,7)
	# while repeat <= 4:
	# 	rd == 5
	# 	if i[rd] > 4:
	# 		i[rd] -= 5
	# 		rd += 1
	# 		repeat += 1
	# 	else:
	# 		i[rd]== 0
	# 		rd += 1
	# 		repeat += 1

	for x in range(len(i)):
		r == 0
		if i[r] > 4:
			i[r] -= 5
			r += 1
		else:
			i[r]== 0
			# rd += 1


	print('I = {}'.format(i))
	if dtime >=10 and dtime <= 25:
		night()
	else: 
		overworld()
		dtime = 0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# TREES TREES TREES TREES TREES TREES TREES TREES TREES TREES TREES

def trees():
	global logsDropped
	global dtime
	if dtime <10:
		print ('\nChop.' , end = '\r')
		time.sleep(0.30) #delay
		print ('Chop..' , end = '\r')
		time.sleep(0.30) #delay
		print ('Chop...')
		time.sleep(0.30) #delay

		dtime += int(1)
		
		print('\n')

		SticksDropped = random.randint(0,4)
		SticksDropped += d[3]
		if SticksDropped != 0:
			print ('You got {} STICKS'.format(SticksDropped))
			i[0] += SticksDropped
			
			
		logsDropped = random.randint(4,7)
		logsDropped += d[3]
		print ('You got {} LOGS'.format(logsDropped))
		i[1] += logsDropped
			
		overworld()
	else:
		night()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE

def mine():
	
	global dtime
	if dtime <10:
		print ('\nMine.' , end='\r')
		time.sleep(0.40) #delay
		print ('Mine..' , end='\r')
		time.sleep(0.40) #delay
		print ('Mine...')
		time.sleep(0.40) #delay


		dtime += int(1)
		
		print('\n')

		if d[0]==0:
			print ('Craft a PICKAXE to mine')
		if d[0]==1:
			CobbleDropped = random.randint(4,7)
			print ('You got {} COBBLESTONE.'.format(CobbleDropped))
			i[3] += CobbleDropped
		
			CoalDropped = random.randint(0,3)
			if CoalDropped != 0:
				print('You got {} COAL.'.format(CoalDropped))
				o[0] += CoalDropped
				
		if d[0]==2:
			CobbleDropped = random.randint(6,9)
			print ('You got {} COBBLESTONE.'.format(CobbleDropped))
			i[3] += CobbleDropped
		
			CoalDropped = random.randint(3,6)
			print('You got {} COAL.'.format(CoalDropped))	
			o[0] += CoalDropped

			IronOreDropped = random.randint(0,2)
			if IronOreDropped != 0:
				print('You got {} IRON ORE.'.format(IronOreDropped))
				o[1]+= IronOreDroppd
				
		overworld()
	else:
		night()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%	
# OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS
def invintory():
	print ('{}'.format(i))
	print('S, P, L,Cb,Ii')
	overworld()
		
def hud():
	print ('{}'.format(d))
	print('P,S,A,SH')
	overworld()

def atime():
	global atime
	print ('{}'.format(dtime))
	if dtime <10:
		overworld()
	else:
		night()


def health():
	global realhealth
	print ('{} HP'.format(realhealth))
	overworld()

def food():
	print('{}'.format(f))
	overworld()

def ores():
	print('{}'.format(o))
	print('Cl,Io')
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT

def craft():
	global CT
	global inputt

	while CT == 0:
		if i[1] > 0 and i[2]< 4:
			inputt = input('>PLANKS< OR >cancel<')
			if inputt=='planks':
				i[1] -= 1
				i[2] += 4
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				break
				
		elif i[2] >= 4:
			inputt = input('>planks< OR >sticks< OR >crafting table< OR >cancel< ')
			if inputt == 'planks':
				i[1] -= 1
				i[2] += 4
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				break
				
			
			if inputt == 'sticks':
				i[2] -= 2
				i[0] += 4
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				break
				
			elif inputt == 'ct':	
				i[2] -= 4
				CT += 1
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				break
			
				
	if CT == 1:
		inputt = input('craft ____?')
		
		if inputt == 'planks':
			i[1] -= 1
			i[2] += 4
			inputt = input('Craft Again?')
			if inputt == ' ':
				craft()
				
		if inputt == 'sticks':
			i[2] -= 2
			i[0] += 4
			inputt = input('Craft Again?')
			if inputt == ' ':
				craft()

		if inputt == 'pickaxe':
			pickaxeM = input ('Material?')
			if pickaxeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				d[0] -= d[0]
				d[0] += 1
				print ('Crafted WOOD PICKAXE')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
			

			elif pickaxeM == 'stone' and i[0]>=2 and i[3]>=3:
				i[0] -= 2
				i[3] -= 3
				d[0] -= d[0]
				d[0] += 2
				print ('Crafted STONE PICKAXE')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				
			else:
				print('Sorry, you dont have enough materials.')
				
		if inputt == 'axe':
			axeM = input ('Material?')
			if axeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				d[3] -= d[3]
				d[3] += 1
				print ('Crafted WOOD AXE')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
			elif axeM == 'stone' and i[0]>=2 and i[3]>=3:
				i[0] -= 1
				i[3] -= 2
				d[3] -= d[3]
				d[3] += 1
				print('Crafted STONE AXE')
			else:
				print('Sorry, you dont have enough materials.')

		if inputt == 'sword':
			swordM = input ('Material?')
			if swordM == 'wood' and i[0]>=1 and i[2]>=2:
				i[0] -= 1
				i[2] -= 2
				d[1] -= d[1]
				d[1] += 1
				print ('Crafted WOOD SWORD')
				inputt = input('Craft?')
				if inputt == ' ':
					craft()
			elif swordM == 'stone' and i[0]>=1 and i[3]>=2:
				i[0] -= 1
				i[3] -= 2
				d[1] -= d[1]
				d[1] += 1
				print('Crafted STONE SWORD')
			else:
				print('Sorry, you dont have enough materials.')

	overworld()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Furnace Furnace Furnace Furnace Furnace Furnace Furnace Furnace
def furnace():
	inputt = input('Smelt _____?')

	if inputt == iron and o[0]>=1 and o[1]>=3:
		print('Smelting..' , end='\r')
		time.sleep(0.30) #delay
		print('Smelting...' , end='\r')
		time.sleep(0.30) #delay
		if o[1]<=3:
			i[4] == o[1]#Add Iron to Invintory
			o[1] == 0#Set Iron Ore to 0
			o[0] -= 1#Coal - 1
			print('+ {} Iron'.format(o[1]))
			inputt = input('Smelt Again?')
			if inputt == ' ':
				furnace()
		else:
			i[4] += o[1]#Add Iron to Invintory
			o[1] -= 3#Iron ore - 3
			o[0] -= 1#Coal - 1
			print('+ 3 Iron')
			inputt = input('Smelt Again?')
			if inputt == ' ':
				furnace()
	if inputt == logs and i[1]>=2:
		print('Smelting..' , end='\r')
		time.sleep(0.30) #delay
		print('Smelting...' , end='\r')
		time.sleep(0.30) #delay
		i[1]-=2
		o[0]+=1
		print('+ 1 coal')
		inputt = input('Smelt Again?')
		if inputt == ' ':
			furnace()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# START START START START START START START START START START START

print ('Generating Realty...')

time.sleep(0.25) #delay

overworld()



