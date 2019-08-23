
import random
import time
CT=0
skip = 0

i = [ 0 , 0 , 0 , 0 , 0]
#_ =[ 0 , 1 , 2 , 3 , 4]
#i = [ STICKS , LOGS , PLANKS , COBBLE , COAL ]

h = [ 0 , 0 , 0 , 0]
#h = [Pickaxe , Sword, Sovel , Axe]
# 1=WOOD 2=STONE 3=IRON


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def overworld():
	print ('\n {OUTSIDE}.')
	choice = raw_input('>chop< OR >mine< OR >craft<? ')
	if choice == 'chop':
		trees()
	elif choice == 'mine':
		mine()
	elif choice == 'i':
		invintory()
	elif choice == 'h':
		hud()
	elif choice == 'craft':
		craft()
	

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def trees():
	print ('Chopping...')
	time.sleep(0.25) #delay
	

	SticksDropped = random.randint(0,4)
	if SticksDropped != 0:
		print ('You got {} STICKS'.format(SticksDropped))
		i[0] += SticksDropped
		
		
	LogsDropped = random.randint(4,7)
	print ('You got {} LOGS'.format(LogsDropped))
	i[1] += LogsDropped
		
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def mine():
	print('Mining...')
	time.sleep(0.25) #delay
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
def invintory():
	print ('{}'.format(i))
	
	overworld()
	
def hud():
	print ('{}'.format(h))
	
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#CT=0
def craft():
	
	global CT
	
	
	
	while CT == 0:
		if i[1] > 0 and i[2]<4:
			input = raw_input('>planks< OR >cancel< ')
 			if input == 'planks':
 				i[1] -= 1
				i[2] += 4
				break
				
				
		elif i[2] >= 4:
			input = raw_input('>planks< OR >sticks< OR >crafting table< OR >cancel< ')
 			
 			if input == 'planks':
 				i[1] -= 1
				i[2] += 4
				break
 			
 			if input == 'sticks':
				i[2] -= 2
				i[0] += 4
				break
				
			elif input == 'ct':	
				i[2] -= 4
 				CT += 1
				break
			
 				
 	if CT == 1:
 		input = raw_input('craft ____?')
 		
 		if input == 'planks':
 				i[1] -= 1
				i[2] += 4
				
 		if input == 'sticks':
				i[2] -= 2
				i[0] += 4
		
 		if input == 'pickaxe':
 			pickaxeM = raw_input ('Material?')
 			if pickaxeM == 'wood' and i[0]>=2 and i[2]>=3:
 				h[0] -= h[0]
 				h[0] += 1
 				print ('crafted WOOD PICKAXE')
 			elif pickaxeM == 'stone' and i[0]>=2 and i[3]>=3:
 				h[0] -= h[0]
 				h[0] += 2
 				print ('crafted STONE PICKAXE')
 			else:
 				print('Sorry, you dont have enough materials.')
 				
		if input == 'axe':
 			pickaxeM = raw_input ('Material?')
 			if pickaxeM == 'wood' and i[0]>=2 and i[2]>=3:
 				h[0] += 1
 				print ('crafted WOOD AXE')
 			else:
 				print('Sorry, you dont have enough materials.')
	
	overworld()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
print ('Generating Realty...')
time.sleep(0.25) #delay

overworld()



