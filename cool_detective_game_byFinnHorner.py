from adventurelib import *
Room.items=Bag()

Room.add_direction("up","down")
#opening statement
print("The local police station has called you to a old pub located North of London. You are called there to investagate a murder. Type look to start. (btw this game is very easy and should only take 30 secounds, the locked door doesnt work lol. Use the directions north east and south to go in diffrent directions. And the look function to see items. To make this game more realistic please find key before heading to the west in the corridor upstairs, thank you. You can also use inventory to look inside your inventory.")
print("\n")
print("Created by Finn Horner")

#Room description. These are used to give my room discriptions so the player knows whats happening in there current state.
car = Room("""
	You arive in your old but reliable 1976 Honda Accord, this is where you keep all your belongings. You might need these.
	""")

car_park = Room("""
	This is where your investagation begins, You find yourself at a muder sence. An old man has been stabed 57 times in the chest. There are two houses nearby and a pub, next to the pub is a alleyway where the body is located. 
	""")

house_1 = Room(""" 
	A young couple live here. Its the house accross the street from the pub. they tell you they herad talking but wernt able to make out. They have no other information. """)

house_2 = Room("""
	A older couple live here, they are right next door to the alyway where the man was murdered. They tell you they heard a loud thump hiting the pavment. They did also here talking but couldnt make it out because they where making tea.
	""")

LeveL1_pub = Room("""
	Its quite here mostly because everybody is looking at the body outside. The bartender is presnt though, she didnt see or hear anything but suggesets you talk the people upstairs, they may of heard or saw something. 
	""")

alleyway = Room("""
	Its dark and glommy, and most importantly theres a dead body. Theres people standing around it, most likey customers from the pub.
	""")

old_womens_room = Room("""
	Here lives a sweet old lady shes kind and asks if you want to come in to have a look around.
	""")

locked_room = Room("""
	You find a man covered in blood you are resonably sure this is the man who has been writing those notes. You ask for his name. He replies with "John Connor". You ask him if you killed the man outside. He says "no, I tried to stop him from dieing, it was a machine, I I couldnt stop it". He starts tearing up then suddenly stops and stares at you with a horrifed stare, you turn around to see a gaint disfigured machine. It lunges at you and you die. THE END (ps dont go east the game is done)
	""")

broomstick_closet = Room("""
	The closet is fulled with brooms but it looks like theres a chest tucked away behind the mass amounts of brooms, you get greedy and open it. To your surprise theres a bunch of money and notes talking about diffrent people. You also see a knife hidden withen the money. Theres blood on it.
	""")

womens_bedroom = Room("""
	Its old fashioned and smelly in here, it looks like theres a lose floorboard by the closet.
	""")

corridor_upstairs = Room("""
	Looks like theres 2 diffrent rooms to enter, theres also what looks to be a broomstick closet.
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

corridor_upstairs.east = old_womens_room
old_womens_room.south = womens_bedroom


Item.discription = ""


#item discriptions
torch = Item("torch")
torch.discription = "Its your average torch but it produces 100,000 lumens, the bartender gave it to you. Do you really need it."


loose_floorboard = Item("loose floorboard","floorboard")
loose_floorboard.discription = "its your average floorboard but this one is loose. Probably somthing hidding under it."

key = Item("key")
key.discription = "Maybe this key unlocks something?"

door = Item("door")
door.discription = "door"

#defing bags

LeveL1_pub.items.add(torch)

womens_bedroom.items.add(loose_floorboard)

#variables
current_room = car
inventory = Bag()
key_taken = False


#binds
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


#this is my code for locking and unlocking doors
@when ("go DIRECTION")
def travel(direction):

	global door_locked
	"""if current_room == corridor_upstairs and door_locked == True and player_inventory.find("key"):
	 print("You insert the key into the door, you twist and the door starts to open....") 
	 corridor_upstairs.west = locked_room
	else:
		Print("you do not have a key.")"""
		

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("you cant go that way.")



@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}")
	if len(current_room.items) > 0:
		print("you also see:")
		for item in current_room.items:
			print(item)
	
@when ("unlock door")
def unlock_door():
	global door_locked
	if current_room == corridor_upstairs and door_locked == True and player_inventory.find("key"):
	 print("You insert the key into the door, you twist and the door starts to open....") 
	 corridor_upstairs.west = locked_room
	else:
		Print("you do not have a key.")
		







#this code is for my key under floorboard code
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	global key_taken 

	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"you pick up the {item}")
	if t == loose_floorboard:
		print("There is a key under it")
		womens_bedroom.items.add(key)			
		key_taken == True
	else:
		print(f"You do not see a {item}.")
	


#this code lets me put stuff in and inventory

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		prinnt(f"You aren't carrying an {item}.")




def main():
	start()

if __name__ == '__main__':
	main()






