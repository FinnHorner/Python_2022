from adventurelib import *

space1 = Room("""
	you are drifting in space. It feels very cold. 
	A slate-blue spacespace sits completely silenty to your left,
	its airlock open and waiting
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, whith thousands
	of small red, blinking lights.
	""")

current_room = space

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


spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
cargo.east = docking 
cargo.south = hallway
quarters.east =mess_hall
bridge.south = escape_pods

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)

def main():
	start()

if __name__ == '__main__':
	main()