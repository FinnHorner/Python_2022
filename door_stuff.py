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