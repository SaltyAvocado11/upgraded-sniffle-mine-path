
import random
import time
CT=0
dtime=0
realhealth=20

i = [ 0 , 0 , 0 , 0 , 0]
#_ =[ 0 , 1 , 2 , 3 , 4]
#i = [ STICKS , LOGS , PLANKS , COBBLE , COAL ]

h = [ 0 , 0 , 0 , 0]
#h = [Pickaxe , Sword, Sovel , Axe]
# 1=WOOD 2=STONE 3=IRON


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD
def overworld():

	global dtime

	print ('\n {OUTSIDE}.')
	choice = input('>chop< OR >mine< OR >craft<? ')
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
	elif choice == 'addtime':
		dtime += 5
		if dtime >=15 and dtime <= 25:
			night()
		else:
			overworld()
	elif choice == 'h':
		health()
	elif choice == 'craft':
		craft()
	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT NIGHT

def night():

	global dtime
	global realhealth
	global strat

	while dtime >=15 and dtime < 25:
		monster = random.randint(1,6)
		if monster == 1: #ZOMBIE
				print('\nZOMBIE attacks')
				strat = input('_____? ')
				live = random.randint(1,5)
				if strat == 'run' and live != 4:
					print ('You LIVE')
					dtime += 1
					night()
				elif live == 4:
					livesLost = 0
					livesLost = random.randint(3,8)
					if livesLost >= realhealth:
						die()
					else:
						print('- {} HP'.format(livesLost))
						print ('{} HP'.format(realhealth))
						realhealth -= livesLost

						night()

				elif strat == 't':
						print('{}'.format(time))
						night()
		if monster == 2: #SKELETON
			print('\nSKELETON attacks')
			strat = input('_____? ')
			live = random.randint(1,5)
			if strat == 'run' and live != 4:
				print ('You LIVE')
				dtime += 1
				night()
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
		if monster == 3: #CREEPER
			print('\nCREEPER attacks')
			strat = input('_____? ')
			live = random.randint(1,5)
			if strat == 'run' and live != 4:
				print ('You LIVE')
				dtime += 1
				night()
			elif live == 4:
				livesLost = 0
				livesLost = random.randint(3,8)
				if livesLost >= realhealth:
					die()
				else:
					print('- {} HP'.format(livesLost))
					print ('{} HP'.format(realhealth))
					realhealth -= livesLost

					night()
		#SAFE SAFE SAFE SAFE SAFE

		if monster == 54 or monster == 5 or monster ==6:
			print('\nSAFE')			
			srat = input ('____? ')
			
			if strat == 'run':
				timepassed = random.randint(2,5)
				dtime += timepassed
				night()
			if strat == 'hide':
				timePassedTierI = radom.randint(1,3)
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
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE DIE

def die():
	dtime += 3
	print ('You DIED')
	saved = random.randint(0,5)
	if i[0] >= saved:
		i[0] == saved
	else:
		i[0] = 0

	if i[1] >= saved:
		i[1] == 5
	else:
		i[1] = 0 

	if i[2] >= saved:
		i[2] == 5
	else:
		i[2] = 0

	if i[3] >= saved:
		i[3] == 5
	else:
		i[3] = 0

	if i[4] >= saved:
		i[4] == 5
	else:
		i[4] = 0

	if dtime >=15 and dtime <= 25:
		night()
	else: 
		overworld()
		dtime = 0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# TREES TREES TREES TREES TREES TREES TREES TREES TREES TREES TREES

def trees():

	global dtime

	print ('\nChop')
	time.sleep(0.25) #delay
	print (' Chop.')
	time.sleep(0.25) #delay
	print ('  Chop..')
	time.sleep(0.25) #delay
	print ('   Chop...')
	time.sleep(0.25) #delay

	dtime += int(1)
	
	print('\n')

	SticksDropped = random.randint(0,4)
	if SticksDropped != 0:
		print ('You got {} STICKS'.format(SticksDropped))
		i[0] += SticksDropped
		
		
	LogsDropped = random.randint(4,7)
	print ('You got {} LOGS'.format(LogsDropped))
	i[1] += LogsDropped
		
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE

def mine():

	global dtime

	print ('\nMine')
	time.sleep(0.25) #delay
	print (' Mine.')
	time.sleep(0.25) #delay
	print ('  Mine...')
	time.sleep(0.25) #delay
	print ('   Mine...')
	time.sleep(0.25) #delay

	dtime += int(1)
	
	print('\n')

	if h[0]==0:
		print ('Craft a PICKAXE to mine')
	if h[0]==1:
		CobbleDropped = random.randint(4,7)
		print ('You got {} COBBLESTONE.'.format(CobbleDropped))
		i[3] += CobbleDropped
	
		CoalDropped = random.randint(0,6)
		if CoalDropped != 0:
			print('You got {} COAL.'.format(CoalDropped))
			i[4] += CoalDropped
			
	if h[0]==2:
		CobbleDropped = random.randint(6,9)
		print ('You got {} COBBLESTONE.'.format(CobbleDropped))
		i[3] += CobbleDropped
	
		CoalDropped = random.randint(3,7)
		if CoalDropped != 0:
			print('You got {} COAL.'.format(CoalDropped))	
			i[4] += CoalDropped
			
	overworld()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%	
# OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS
def invintory():
	print ('{}'.format(i))
	
	overworld()
	
def hud():
	print ('{}'.format(h))
	
	overworld()

def atime():

	print ('{}'.format(dtime))
	if dtime >= 15:
		night()
	else:
		overworld()
def health():
	global realhealth
	print ('{}'.format(realhealth))
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT

def craft():
	global CT
	global inputt

	while CT == 0:
		if i[1] > 0 and i[2]< 4:
			inputt = input('>planks< OR >cancel<')
			if inputt=='planks':
				i[1] -= 1
				i[2] += 4
				break
				
		elif i[2] >= 4:
			inputt = input('>planks< OR >sticks< OR >crafting table< OR >cancel< ')
			if inputt == 'planks':
				i[1] -= 1
				i[2] += 4
				break
			
			if inputt == 'sticks':
				i[2] -= 2
				i[0] += 4
				break
				
			elif inputt == 'ct':	
				i[2] -= 4
				CT += 1
				break
			
				
	if CT == 1:
		inputt = input('craft ____?')
		
		if inputt == 'planks':
				i[1] -= 1
				i[2] += 4
				
		if inputt == 'sticks':
				i[2] -= 2
				i[0] += 4
		
		if inputt == 'pickaxe':
			pickaxeM = input ('Material?')
			if pickaxeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				h[0] -= h[0]
				h[0] += 1
				print ('crafted WOOD PICKAXE')
			elif pickaxeM == 'stone' and i[0]>=2 and i[3]>=3:
				i[0] -= 2
				i[3] -= 3
				h[0] -= h[0]
				h[0] += 2
				print ('crafted STONE PICKAXE')
			else:
				print('Sorry, you dont have enough materials.')
				
		if inputt == 'axe':
			axeM = input ('Material?')
			if axeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				h[3] -= h[3]
				h[3] += 1
				print ('crafted WOOD AXE')
			else:
				print('Sorry, you dont have enough materials.')

		if inputt == 'sword':
			swordM = input ('Material?')
			if swordM == 'wood' and i[0]>=1 and i[2]>=2:
				i[0] -= 1
				i[2] -= 2
				h[1] += 1
				print ('crafted WOOD sword')
			else:
				print('Sorry, you dont have enough materials.')	

	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# START START START START START START START START START START START

print ('Generating Realty...')

time.sleep(0.25) #delay

overworld()



