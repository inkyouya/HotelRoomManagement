import random
import copy

from .constants import (
	AVAILABLE,
	OCCUPIED,
	VACANT,
	REPAIR,
)

class Room:

	def __init__(self, floor, name):
		self.name = name
		self.floor = floor
		self.status = AVAILABLE

	def __str__(self):
		return "{}{}".format(self.floor, self.name)

	def get_verbose_status(self):
		if self.status == AVAILABLE:
			return "Available"
		elif self.status == OCCUPIED:
			return "Occupied"
		elif self.status == VACANT:
			return "Vacant"
		elif self.status == REPAIR:
			return "Repair"
		else:
			return "-"

	def set_room_status(self, status):
		if self.status not in [AVAILABLE, OCCUPIED, VACANT, REPAIR]:
			raise ValueError("Invalid room status")
		self.status = status


class Hotel:
	def __init__(self, number_of_floors=4, number_of_rooms=5):
		self.floors = []

		# Parameter validations
		number_of_floors = int(number_of_floors)
		number_of_rooms = int(number_of_rooms)
	
		# Set limitation to only use capitalized alphabets for room names
		if number_of_rooms > 26:  
			raise ValueError("Only upto 26 rooms are supported")

		# Initialize floors and rooms
		for floor_number in range(number_of_floors):
			floor = []
			for room_number in range(number_of_rooms):
				name = chr(65+room_number)
				room = Room(floor_number+1, name)
				floor.append(room)
			self.floors.append(floor)

		self.number_of_floors = number_of_floors
		self.number_of_rooms = number_of_rooms

	def get_nearest_available_room(self):
		for floor_index in range(len(self.floors)):
			current_floor = self.floors[floor_index]
			if floor_index % 2 == 1:
				floor_in_itr_order = current_floor[::-1]
			else:
				floor_in_itr_order = current_floor
			for room in floor_in_itr_order:
				if room.status == AVAILABLE:
					return room
		return None

	def get_room(self, room_id):
		floor_number = int(room_id[0])
		name = room_id[1]
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
			return False, "No available rooms"
		room.set_room_status(OCCUPIED)
		return True, "Room {} assigned".format(room)

	def checkout_room(self, room_id):
		# Occupied -> Vacant
		room = self.get_room(room_id)
		if not room:
			return False, "Room {} not found".format(room_id)
		if room.status != OCCUPIED:
			return False, "Room {} is not occupied".format(room_id)

		room.set_room_status(VACANT)
		return True, "Room {} is now Vacant".format(room_id)

	def clean_room(self, room_id):
		# Vacant -> Available/Repair
		room = self.get_room(room_id)
		if not room:
			return False, "Room {} not found".format(room_id)
		if room.status != VACANT:
			return False, "Room {} is not vacant".format(room_id)

		if random.randint(0, 1) == 1:  # Equal chance
			result = AVAILABLE
		else:
			result = REPAIR

		room.set_room_status(result)
		return True, "Room {} is now {}".format(room_id, room.get_verbose_status())

	def repair_room(self, room_id):
		# Repair -> Vacant
		room = self.get_room(room_id)
		if not room:
			return False, "Room {} not found".format(room_id)
		if room.status != REPAIR:
			return False, "Room cannot be repaired"

		room.set_room_status(VACANT)
		return True, "Room {} is now Vacant".format(room_id)

	def get_available_rooms(self):
		available_rooms = []
		for floor in self.floors:
			for room in floor:
				if room.status == AVAILABLE:
					available_rooms.append(str(room))
		available_rooms_str = ", ".join(available_rooms)
		print("Number of available rooms: {}".format(len(available_rooms)))
		print("Available rooms: {}".format(available_rooms_str))
		return available_rooms_str

	def list_rooms(self):
		for floor in self.floors[::-1]:
			names = []
			status = []
			for room in floor[::-1]:
				names.append("{:^9}".format(str(room)))
				status.append("{:^9}".format(room.get_verbose_status()))
			print(" ".join(names))
			print(" ".join(status))
			print(" ")
