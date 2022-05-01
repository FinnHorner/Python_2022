from adventurelib import *
Room.items=Bag()

Room.add_direction("up","down")
#opening statement
print("""The local police station has called you to a old pub located North of London. You are called there to investagate a murder.""")
print("""Type look to start. Use the directions West, North, East, and South to go in diffrent directions. You can also use inventory to look inside your inventory where you can find all the items have have.""")
print("\n")
print("Created by Finn Horner")

#Room discription. These are used to give my room discriptions so the player knows whats happening in the specific area 
car = Room("""
You arrive in your old but reliable 1976 Honda Accord. It's a good old car and you love it to bits.
""")

car_park = Room("""
This is where your investigation begins, You find yourself at a murder scene. An old man has been stabbed 57 times in the chest. 
There are two houses nearby and a pub, next to the pub is an alleyway where the body is located.
""")

house_1 = Room(""" 
A young couple lives here. It's the house across the street from the pub. they tell you they heard talking but weren't able to make out what was being said. 
They have no other information.
""")

house_2 = Room("""
An older couple lives here, they are right next door to the alleyway where the man was murdered. 
They tell you they heard a loud thump hitting the pavement. They did also here talking but couldn't make it out because they were making a lovely cup of tea.
""")

LeveL1_pub = Room("""
It's quiet here mostly because everybody is looking at the body outside. 
The bartender is present though, she didn't see or hear anything but suggests you talk to the people upstairs, they may have heard or seen something. 
""")

alleyway = Room("""
It's dark and gloomy, and most importantly there's a dead body. People are standing around it, most likely customers from the pub.
""")

old_womens_room = Room("""
Here lives a sweet old lady shes kind and asks if you want to come in to have a look around. She also tells you the other room doesnt have a light and doesnt have a spear torch, might be good to find one?
""")

locked_room = Room("""
You find a man covered in blood you are reasonably sure this is the man who has been writing those notes. You ask for his name. He replies with "John Connor". You ask him if you killed the man outside.
He says "no, I tried to stop him from dying, it was a machine, I, I couldn't stop it". He starts tearing up then suddenly stops and stares at you with a horrified stare, you turn around to see a giant disfigured machine.
It lunges at you. To be continued. (ps don't go east the game is done. Or if you want to continue looking around go for it).
""")

broomstick_closet = Room("""
The closet is full of brooms but it looks like there's a chest tucked away behind the mass amounts of brooms, you get greedy and open it. 
To your surprise, there are a bunch of notes and pictures of different people. You also see a knife hidden within the random stuff. There's blood on it.
""")

womens_bedroom = Room("""
It's old fashioned and smelly in here, it looks like there's a lose floorboard by the closet.
""")

corridor_upstairs = Room("""
Looks like there are 2 different rooms to enter, there's also what looks to be a broomstick closet.
""")

#Room connections
car.east = car_park
car_park.north = house_1
car_park.south = house_2
car_park.east = LeveL1_pub
LeveL1_pub.up = corridor_upstairs
corridor_upstairs.down = LeveL1_pub
LeveL1_pub.south = alleyway
corridor_upstairs.south = broomstick_closet
corridor_upstairs.west = locked_room
corridor_upstairs.east = old_womens_room
old_womens_room.south = womens_bedroom


Item.discription = ""


#item discriptions. These give diffrent discriptions to each item and it also allows me to put the items in my game.
torch = Item("torch")
torch.discription = "It's your average torch but it produces 100,000 lumens, the bartender gave it to you. Do you really need it"


loose_floorboard = Item("loose floorboard","floorboard")
loose_floorboard.discription = "It's your average floorboard but this one is loose. Probably something hidden under it."

key = Item("key")
key.discription = "Maybe this key unlocks something?"

dead_body = Item("dead body","deadbody")
dead_body.discription = "Its a dead body, maybe theres somthing hidden under it."

#defing bags
#these are where I have put some of my items in my game.
alleyway.items.add(dead_body)
womens_bedroom.items.add(loose_floorboard)

#variables. This is assgining values to things.
current_room = car
key_taken = False
torch_taken = False
inventory = Bag()



#binds
#binds allow the player to move between rooms and look around giving the player control of what is happening inside the game
@when("exit car")
def exit_car():
	global current_room
	if current_room is not car:
		print("This is not the way.")
	else:
		current_room = car_park
		print("""You are now in the car park, its cold and dark but its peaceful.
			""")
		print(current_room)


#this is my code for locking and unlocking doors with diffrent items
@when ("go DIRECTION")
def travel(direction):
	global current_room
	
	if current_room == corridor_upstairs and direction == 'west' and key_taken == False:
		print("The door is locked.")
		return
	elif current_room == corridor_upstairs and direction == 'west' and key_taken == True:
		print("You have now entered the room.")


	if current_room == old_womens_room and direction == 'south' and torch_taken == False:
		print("There is no light source.")
		return

	elif current_room == old_womens_room and direction == 'south' and torch_taken == True:
		print("You turn on the flashlight, you can now see")


	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("You cant go that way.")

@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}")
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)
	


#this code is for my key under floorboard code. The key is used for the locked door located in the upstairs of the pub. 
#this code adds the key and floor board into the game.
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	global key_taken 
	global torch_taken
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
		if t == loose_floorboard:
			print("There is a key under it")
			womens_bedroom.items.add(key)			
			key_taken = True
		if t == dead_body:
			print("There is a torch under it")
			alleyway.items.add(torch)			
			torch_taken = True
		

#this code lets me put diffrent items into an inventory the player can access by typing in inventory in windows powershell.

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}.")




def main():
	start()

if __name__ == '__main__':
	main()






