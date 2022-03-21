from adventurelib import *
space = Room("""
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


def main():
	start()

if __name__ == '__main__':
	main()