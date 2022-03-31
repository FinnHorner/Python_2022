from adventurelib import *

#Room description 
car_park = Room("""
	This is where your investagation begins, You find yourself at a muder sence. 
	a old man has been stabed 57 times in the chest, the body is located in an alleyway behind the old pub. You know nothing yet.
	there are two houses nearby and a pub, next to the pub is a alleywau where the body is located. 
	""")

house_1 = Room(""" 
	A young couple live here. Its the house accross the street from the pub. they tell you they herad talking but wernt able to make out.
	They have no other information. """)

house_2 = Room("""
	A older couple live here, they are right next door to the alyway where the man was murdered. They tell you they heard a loud thump hiting the pavment. 
	They did also here talking but couldnt make it out because they where making tea.
	""")

LeveL1_pub = Room("""
	Its quite here mostly because everybody is looking at the body outside.
	The bartender is presnt though, she didnt see or hear anything but suggesets you talk the people upstairs, 
	they may of heard or saw something. 
	""") 

alleyway = Room("""
	Its dark and glommy, and most importantly theres a dead body. Theres people standing around it, most likey customers from the pub.
	""")

old_womens_room = Room("""
	Here lives a sweet old lady shes kind and asks if you want to come in to have a look around.
	""")

locked_room = Room("""
	You find a man covered in blood you are resonably sure this is the man who has been writing those notes. 
	You ask for his name and he gives you the bname that is writen on some of the notes.
	""")

broomstick_closet = Room("""
	The closet is fulled with brooms but it looks like theres a chest tucked away behind the mass amounts of brooms, you get greedy and open it.
	To your surprise theres a bunch of money and notes talking about diffrent people and what they owe. You also see a knife hidden withen the money. 
	Theres blood on it.
	""")

womens_bedroom = Room("""
	Its old fashioned and smelly in here, it looks like theres a lose floorboard by the closet.
	""")

corridor_upstairs = Room("""
	Looks like theres 2 diffrent rooms to enter, theres also what looks to be a broomstick closet.
	""")

#Room connections
car_park.north = house_1
car_park.south = house_2
car_park.east = LeveL1_pub
LeveL1_pub.north = corridor_upstairs
corridor_upstairs.south = broomstick_closet
corridor_upstairs.west = locked_room
corridor_upstairs.east = old_womens_room
old_womens_room.south = womens_bedroom


Item.discription = ""

Torch = Item("torch","Torch")
Torch.discription = "Its your average torch but it produces 100,000 lumens. "

Clipboard = Item("clipboard","Clipboard","clip board","Clip Board")




















