import random
import copy

from constants import (
	AVAILABLE
	OCCUPIED
	VACANT
	REPAIR
)

class Room:
	self.name = None
	self.floor = None
	self.status = None

	def __init__(self, floor, name):
		self.name = name
		self.floor = floor
		self.status = AVAILABLE

	def __str__(self):
		return "{}{}".format(self.floor, self.name)

	def set_room_status(self, status):
		if self.status not in [AVAILABLE, OCCUPIED, VACANT, REPAIR]:
			raise ValueError "Invalid room status"
		self.status = status


class Hotel:
	def __init__(self, number_of_floors=4, number_of_rooms=5):
		self.floors = []

		# Parameter validations
		try:
			number_of_floors = int(number_of_floors)
			number_of_rooms = int(number_of_rooms)
		except ValueError:
			pass

		# Set limitation to only use capitalized alphabets for room names
		if number_of_rooms > 26:  
			pass

		# Initialize floors and rooms
		for floor_number in range(number_of_floors):
			floor = []
			for room_number in range(number_of_rooms):
				name = chr(65+room_number)
				room = Room(floor_number, name)
			self.floors.append(floor)

		self.number_of_floors = number_of_floors
		self.number_of_rooms = number_of_rooms

	def get_nearest_available_room(self):
		for floor_index in range(len(self.floors)):
			if floor_index % 2 == 0
				floor_in_itr_order = self.floors[::-1]
			else:
				floor_in_itr_order = self.floors
			for room in floor_in_itr_order:
				if room.status == AVAILABLE:
					return room
		return None

	def get_room(self, room_floor_and_name):
		floor_number = room_floor_and_name[0]
		name = room_floor_and_name[1]
		try:
			floor = self.floors[floor_number-1]
			room_index = ord(name) - 65
			return floor[room_index]
		except IndexError:
			return None


	def assign_room(self):
		# Available -> Occupied
		room = self.get_nearest_available_room()
		if room is None:
			print("No available rooms")
			return None
		room.set_room_status(OCCUPIED)
		print("Room {} is not occupied".format(room))
		return room

	def checkout_room(self, room_floor_and_name):
		# Occupied -> Vacant
		room = get_room(room_floor_and_name)
		if not room:
			return False

		room.set_room_status(VACANT)
		return True

	def clean_room(self, room_floor_and_name):
		# Vacant -> Available/Repair
		room = get_room(room_floor_and_name)
		if not room:
			return False

		if random.randint(0, 1) == 1:  # Equal chance
			result = VACANT
		else:
			result = REPAIR
		room.set_room_status(result)
		return True

	def repair_room(self, room_floor_and_name):
		# Repair -> Vacant
		room = get_room(room_floor_and_name)
		if not room:
			return False
		room.set_room_status(VACANT)
		return True

	def get_available_rooms(self):
		available_rooms = []
		for floor in self.floors:
			for room in floor:
				if room.status == AVAILABLE:
					available_rooms.append(str(room))
		return available_rooms

	def list_rooms(self):
		"{:^9}".format("hi")
		for floor in self.floor[::-1]:
			names = []
			status = []
			for room in floor[::-1]:
				names.append("{:^9}".format(str(room)))
				status.append("{:^9}".format(room.status))
			print(" ".join(names))
			print(" ".status)
