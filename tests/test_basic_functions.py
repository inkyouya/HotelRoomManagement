import pytest
from hotel_room_management.hotel import (
	Hotel,
)
from hotel_room_management.constants import (
	AVAILABLE,
	OCCUPIED,
	VACANT,
	REPAIR,
)



class TestClass:

	def setup_class(self):
		self.hotel = Hotel(number_of_floors=4, number_of_rooms=5)

	def teardown_class(self):
		del self.hotel

	def test_get_room(self):
		room = self.hotel.get_room("4E")
		assert str(room) == "4E"

		non_existent_room = self.hotel.get_room("6E")
		assert non_existent_room == None

	def test_set_status(self):
		room = self.hotel.get_room("4E")
		room.set_room_status(VACANT)
		assert room.get_verbose_status() == "Vacant"

		room.set_room_status(AVAILABLE)
		assert room.get_verbose_status() == "Available"

	def test_available(self):
		all_rooms = "1A, 1B, 1C, 1D, 1E, 2A, 2B, 2C, 2D, 2E, 3A, 3B, 3C, 3D, 3E, 4A, 4B, 4C, 4D, 4E"
		assert self.hotel.get_available_rooms() == all_rooms

	def test_assign(self):
		for _ in range(6):
			self.hotel.assign_room()

		assert self.hotel.get_room("1A").get_verbose_status() == "Occupied"
		assert self.hotel.get_room("1B").get_verbose_status() == "Occupied"
		assert self.hotel.get_room("2E").get_verbose_status() == "Occupied"
		assert self.hotel.get_room("3E").get_verbose_status() == "Available"
		assert self.hotel.get_room("2A").get_verbose_status() == "Available"

		expected_avilable_rooms = "2A, 2B, 2C, 2D, 3A, 3B, 3C, 3D, 3E, 4A, 4B, 4C, 4D, 4E"
		assert self.hotel.get_available_rooms() == expected_avilable_rooms

	def test_checkout(self):
		self.hotel.checkout_room("1B")
		assert self.hotel.get_room("1B").get_verbose_status() == "Vacant"

		success, _ = self.hotel.checkout_room("2A")
		assert self.hotel.get_room("2A").get_verbose_status() == "Available"
		assert not success
		
	def test_clean(self):
		success, _ = self.hotel.checkout_room("2E")
		assert success

		self.hotel.clean_room("2E")
		assert self.hotel.get_room("2E").get_verbose_status() in ["Available", "Repair"]

	def test_repair(self):
		vacant_room = self.hotel.get_room("3E")
		vacant_room.set_room_status(VACANT)
		success, _ = self.hotel.repair_room("3E")
		assert not success

		repair_room  = self.hotel.get_room("4D")
		repair_room.set_room_status(REPAIR)
		success, _ = self.hotel.repair_room("4D")
		assert success
		assert repair_room.get_verbose_status() == "Vacant"
