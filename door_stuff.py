	key_taken = False



	global current_room
	global key_taken
	if current_room == corridor_upstairs and direction == 'west' and key_taken ==True:
		print("The door is locked..... kinda sus")
		return
	elif current_room == corridor_upstairs and direction == 'west' and key_taken == False:
		print(current_room)
	else:
		print("The door is locked")










	global door_locked
	if current_room == corridor_upstairs and door_locked == True and player_inventory.find("key"):
	 print("You insert the key into the door, you twist and the door starts to open....") 
	 corridor_upstairs.west = locked_room
	else:
		Print("you do not have a key.")
		
