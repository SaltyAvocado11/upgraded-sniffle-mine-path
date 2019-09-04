import random
import time
CT=0
dtime=0
realhealth=20
r = 0
Puses = 0
# axeD == 0
# pickaxeD == 0
# swordD == 0

i = [ 0 , 0 , 0 , 0 , 0 , 0]
#_ =[ 0 , 1 , 2 , 3 , 4 , 5]
#i = [ STICKS , LOGS , PLANKS , COBBLE , Iron , Torches]

d = [ 0 , 0 , 0 , 0]
#d = [Pickaxe , Sword, Sovel , Axe]
# 1=WOOD 2=STONE 3=IRON

f = [ 0 , 0 , 0]
#f = [Rotten Flesh , Bones , Steak]

o = [0 , 0]
#o = [Coal , Iron Ore]


if d[1]== 0:
	Suses =0

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD OVERWORLD
def overworld():

	global dtime

	print ('\n {OUTSIDE}.')
	choice = input('>chop< OR >mine< OR >craft<? OR >smelt< ')
	choice = str(choice)
	if choice == 'chop':
		trees()
	elif choice == 'mine':
		mine()
	elif choice == 'smelt':
		furnace()
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
	elif choice == 'help':
		help()
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
	global swordD

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
			if live == 3 or live == 2:
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
				
					if d[1] == 0:
						Suses = 0
					elif d[1] > 0:
						Suses -= 1
						if Suses == 0:
							print('Your SWORD broke')
							d[0] == 0
					else:
						print('Sword HP: {}'.format(Suses))

					die()

				else:
					('- {} HP'.format(livesLost))
					realhealth -= livesLost
					print ('{} HP'.format(realhealth))

				if d[1] == 0:
					Suses = 0
				elif d[1] > 0:
					Suses -= 1
					if Suses == 0:
						print('Your SWORD broke')
						d[0] == 0
				else:
					print('Sword HP: {}'.format(Suses))

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

	# for x in range(len(i)):
	# 	r == 0
	# 	if i[r] > 4:
	# 		i[r] -= 5
	# 		r += 1
	# 	else:
	# 		i[r]== 0
	# 		# rd += 1
	# stuffLost = random.randint(5,7)
	# r = 1
	# goagain = 0
	# while goagain <= 4:
	# 	if i[r] < 3:
	# 		i[r] = 4
	# 		r += 1
	# 	else:
	# 		i[r] -= stufflost
	# 		r += 1
	i = [ 0 , 0 , 0 , 0 , 0 , 0]


	print('I = {}'.format(i))

	d = [0 , 0 , 0 ,0]
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
	global Auses
	print ('\n Chop.' , end = '\r')
	time.sleep(0.30) #delay
	print (' Chop..' , end = '\r')
	time.sleep(0.30) #delay
	print (' Chop...')
	time.sleep(0.30) #delay

	dtime += int(1)
		
	print('\n')

	SticksDropped = random.randint(0,4)
	SticksDropped += d[3]
	if SticksDropped != 0:
		print ('+ {} STICKS'.format(SticksDropped))
		i[0] += SticksDropped
			
			
	logsDropped = random.randint(4,7)
	logsDropped += d[3]
	print ('+ {} LOGS'.format(logsDropped))
	i[1] += logsDropped

	if d[3] == 0:
		Auses = 0

	elif d[3] > 0:
		Auses -= 1
		if Auses == 0:
			print('Your AXE broke')
			d[3] = 0
		else:
			print('Axe HP: {}'.format(Auses))
	overworld()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE MINE

def mine():
	
	global dtime
	global Puses

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
			print ('+ {} COBBLESTONE.'.format(CobbleDropped))
			i[3] += CobbleDropped
		
			CoalDropped = random.randint(0,3)
			if CoalDropped != 0:
				print('+ {} COAL.'.format(CoalDropped))
				o[0] += CoalDropped
				
		if d[0]==2:
			CobbleDropped = random.randint(6,9)
			print ('+ {} COBBLESTONE.'.format(CobbleDropped))
			i[3] += CobbleDropped
		
			CoalDropped = random.randint(3,6)
			print('+ {} COAL.'.format(CoalDropped))	
			o[0] += CoalDropped

			IronOreDropped = random.randint(0,2)
			if IronOreDropped != 0:
				print('+ {} IRON ORE.'.format(IronOreDropped))
				o[1]+= IronOreDroppd
	
	if d[0] == 0:
		Puses = 0

	elif d[0] > 0:
		Puses -= 1
		if Puses == 0:
			print('Your PICKAXE broke')
			d[0] = 0
		else:
			print('Pickaxe HP: {}'.format(Puses))
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%	
# OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS OTHERS
def invintory():
	print ('\n{}'.format(i))
	print(' S, L, P, Cb ,Ii,T')
	overworld()
		
def hud():
	print ('{}'.format(d))
	print('P,S,Sh,A')
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
	overworld()

def help():
	print('\nWelcome to MinePath. You have entered the help tutorial.')
	print('To make a choice in the {OVERWORLD}, enter in the >code<')
	print('Other {OVERWOLD} commands are: >t< >i< >o< >d< >h<')
	print('\n>t< gives you the time')
	print('>i< and >o< will give you your invintory and ore invin.')
	print('>d< shows you your tools and >h< shows your health')
	print('Most commands can be run wherever there is a promt')
	print('\n>d< will give you a list of numbers.')
	print('-The first slot is your Pickaxe, second Sword, third Shovel, fourth Axe.')
	print('-The number in each slot is the material. 1=wood 2=stone 3=iron')
	print('\nIn the craft and smelt interface you enter the whole command or just the first letter.')
	print('-When asked if you want to smelt or craft again (____?)...')
	print(' You may enter " " or "yes" to craft again.')
	print('\nYou can reaccess this tutorial whenever you are in the {OVERWORLD}')
	time.sleep(5) #delay
	
	overworld()
	
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT CRAFT

def craft():
	global CT
	global inputt
	global Auses
	global Puses
	global Suses

	while CT == 0:
		if i[1] == 0:
			print('You dont have any materials.')
			overworld()
#No plank
		if i[1] > 0 and i[2]< 4:
			inputt = input('>PLANKS< OR >STICKS< >cancel<')
			if inputt=='planks' or inputt=='p':
				i[1] -= 1
				i[2] += 4
				print('+ 4 PLANKS')
				inputt = input('Craft Again?')
				if inputt == ' ' or inputt == 'yes':
					craft()
				else:
					overworld()

		if inputt == 'sticks' or inputt=='s' and i[2]>=2:
				i[2] -= 2
				i[0] += 4
				print('+ 4 STICKS')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				

#has planks
		elif i[2] >= 4:
			inputt = input('>planks< OR >sticks< OR >crafting table< OR >cancel< ')
			if inputt == 'planks' or inputt=='p' and i[1]>=1:
				i[1] -= 1
				i[2] += 4
				print('+ 4 PLANKS')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				else:
					break
				
			
			if inputt == 'sticks' or inputt=='s' and i[2]>=2:
				i[2] -= 2
				i[0] += 4
				print('+ 4 STICKS')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				else:
					break
 
			if inputt == 'torch' or inputt=='t'and i[0] >=1 and o[0]>= 1:
				i[0]-= 1
				o[0] -= 1
				i[5] += 4
				print('+ 4 TORCHES')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				else:
					break

				
			elif inputt == 'ct' or inputt == 'craftingtable' and i[2]>=4:
				i[2] -= 4
				CT += 1
				print('+ CRAFTING TABLE')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
				else:
					break

			elif inputt == 'cancel':
				overworld()
			else:
				print('Sorry, you dont have enough materials')
				print('{}'.format(i))
			
#has CT~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	if CT == 1:
		inputt = input('craft ____?')
#Planks		
		if inputt == 'planks' or inputt=='p' and i[1]>=1:
			i[1] -= 1
			i[2] += 4
			print('+ 4 PLANKS')
			inputt = input('Craft Again?')
			if inputt == ' ':
				craft()
#Sticks				
		if inputt == 'sticks' or inputt=='t'and i[0] >=1 and o[0]>= 1:
			i[2] -= 2
			i[0] += 4
			print('+ 4 STICKS')
			inputt = input('Craft Again?')
			if inputt == ' ':
				craft()

		if inputt == 'torch' or inputt=='t'and i[0] >=1 and o[0]>= 1:
			i[0]-= 1
			o[0] -= 1
			i[5] += 4
			print('+ 4 TORCHES')
			inputt = input('Craft Again?')
			if inputt == ' ':
				craft()

#Pickaxe
		if inputt == 'pickaxe':
			pickaxeM = input ('Material?')
	#Wood
			if pickaxeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				d[0] -= d[0]
				d[0] += 1
				Puses -= Puses
				Puses += 5
				print ('+ WOOD PICKAXE')
				print('Pickaxe HP:{}'.format(Puses))
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
			
	#Stone
			elif pickaxeM == 'stone' and i[0]>=2 and i[3]>=3:
				i[0] -= 2
				i[3] -= 3
				d[0] -= d[0]
				d[0] += 2
				Puses -= Puses
				Puses += 10
				print ('+ STONE PICKAXE')
				print('Pickaxe HP:{}'.format(Puses))
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
	#Iron
			elif pickaxeM == 'iron' and i[0]>=2 and i[4]>=3:
				i[0]-=2
				i[4] -= 3
				d[0] -= d[0]
				d[0] += 3
				Puses -= Puses
				Puses += 15
				print('+ Iron Pickaxe')
				print('Pickaxe HP:{}'.format(Puses))
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
			else:
				print('Sorry, you dont have enough materials.')
				print('{}'.format(i))
#Axe				
		if inputt == 'axe':
			axeM = input ('Material?')
	#Wood
			if axeM == 'wood' and i[0]>=2 and i[2]>=3:
				i[0] -= 2
				i[2] -= 3
				d[3] -= d[3]
				d[3] += 1
				Auses -= Auses
				Auses += 5
				print ('+ WOOD AXE')
				print('Axe HP:{}'.format(Auses))
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
	#Stone
			elif axeM == 'stone' and i[0]>=2 and i[3]>=3:
				i[0] -= 1
				i[3] -= 2
				d[3] -= d[3]
				d[3] += 1
				Auses -= Auses
				Auses += 10
				print('Axe HP:{}'.format(Auses))
				print('+ STONE AXE')
				inputt = input('Craft Again?')
				if inputt == ' ':
					craft()
			else:
				print('Sorry, you dont have enough materials.')
				print('{}'.format(i))
#Sword
		if inputt == 'sword':
			swordM = input ('Material?')
	#Wood
			if swordM == 'wood' and i[0]>=1 and i[2]>=2:
				i[0] -= 1
				i[2] -= 2
				d[1] -= d[1]
				d[1] += 1
				Suses -= Suses
				Suses += 5
				print ('+ WOOD SWORD')
				print('Sword HP:{}'.format(Suses))
				inputt = input('Craft?')
				if inputt == ' ':
					craft()
	#Stone
			elif swordM == 'stone' and i[0]>=1 and i[3]>=2:
				i[0] -= 1
				i[3] -= 2
				d[1] -= d[1]
				d[1] += 1
				Suses -= Suses
				Suses += 5
				print('+ STONE SWORD')
				print('Sword HP:{}'.format(Suses))
				inputt = input('Craft?')
				if inputt == ' ':
					craft()
			else:
				print('Sorry, you dont have enough materials.')
				print('{}'.format(i))

		elif inputt == 'cancel':
			overworld()
		else:
			craft()

	overworld()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Furnace Furnace
# ace Furnace Furnace Furnace Furnace Furnace Furnace
def furnace():
	inputt = input('Smelt _____?')

#IronIngots
	if inputt == 'iron' and o[0]>=1 and o[1]>=3:
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
			else:
				overworld()
#Logs
	if inputt == 'logs' and i[1]>=2:
		print('Smelting..' , end='\r')
		time.sleep(0.30) #delay
		print('Smelting...')
		time.sleep(0.30) #delay
		i[1]-=2
		o[0]+=1
		print('+ 1 coal')
		inputt = input('Smelt Again?')
		if inputt == ' ':
			furnace()
		else:
			overworld()

	if inputt == 'cancel':
		overworld()
	else:
		print('Insufficient materials.')
		overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# START START START START START START START START START START START

print ('Generating Realty...')

time.sleep(0.25) #delay

overworld()



