from adventurelib import *

Room.items = Bag()


space = Room("""
	you are drifting in space. It feels very cold. 
	A slate-blue spacespace sits completely silenty to your left,
	its airlock open and waiting
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, whith thousands
	of small red, blinking lights.
	""")

cargo = Room("""
	Thecargo room is very large
	""")

docking = Room("""
	Where the smaller ships come to dock
	""")

hallway = Room("""
	acsess to diffrent rooms
	""")

bridge = Room("""
	This is where the ship gets driven
	""")

quarters = Room("""
	this is where the crew sleeps
	""")

mess_hall = Room("""
	Where the crew eats togthers
	""")

escape_pods = Room("""
	In case of emergency
	""")






spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
cargo.east = docking 
cargo.south = hallway
quarters.east =mess_hall
bridge.south = escape_pods

Item.description = "" #this adds a blank description to each item


knife = Item("a dirty knife","knife")
knife.discription = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item(" a red keycard","red card","red card")
red_keycard.discription = "Its a red keycard. It probably opens a door or a locker"

emergency_erickim_button = Item("erickim","button","emergency")
emergency_erickim_button.discription = "a button that should not be pressed as it spawns eric kim."

ronaldo = Item("ronaldo","Ronaldo")
ronaldo.discription = "Its R7 lets gooooooooooooooooo."


mess_hall.items.add(red_keycard)
cargo.items.add(knife)
escape_pods.items.add(ronaldo)
docking.items.add(emergency_erickim_button)

current_room = spaceship
inventory = Bag()

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = spaceship
		print("""You heave yourself into the spaceship and slam you hand on the 
		button to close the door
		""")
		print(current_room)



@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)


@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}")
	if len(current_room.items) > 0:
		print("you also see:")
		for item in current_room.items:
			print(item)


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"you pick up the {item}")
	else


def main():
	start()

if __name__ == '__main__':
	main()