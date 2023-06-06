from hotel_room_management.hotel import Hotel

from textwrap import dedent


class ManagementInterface:
	def __init__(self):
		self.hotel = Hotel()

	def main_loop(self):
		help_message = dedent('''
			Available commands:
				assign      -> Assigns room nearest to the entrance
				help        -> Brings out this message
				checkout    -> Vacants a room that was occupied
				clean       -> Marks a vacant room as cleaned
				repair      -> Marks a room due for repair as vacant
				list        -> Lists all rooms and their statuses
				available   -> Lists all available rooms
				reset       -> Turns all rooms available
				exit        -> Exits this program
		''')
		print("Welcome! Enter a commands to start")
		print(help_message)
		while True:
			command = input("Please enter a command: ")
			if command == "exit":
				break

			elif command == "help":
				print(help_message)
			elif command == "assign":
				self.handle_assign()
			elif command == "checkout":
				self.handle_checkout()
			elif command == "clean":
				self.handle_clean()
			elif command == "repair":
				self.handle_repair()
			elif command == "list":
				self.handle_list_rooms()
			elif command == "available":
				self.handle_list_available_rooms()
			elif command == "reset":
				self.handle_reset()

			else:
				print("Invalid command, hint: use \"help\" for help")

	def validate_room_name_format(self, room_id):
		if len(room_id) > 2:
			return False

		floor_number = room_id[0]
		name = room_id[1]

		try:
			int(floor_number)
			return 65 <= ord(name) <= 90
		except ValueError:  # Invalid floor number
			return False
		return False

	def handle_assign(self):
		success, message = self.hotel.assign_room()
		print(message)

	def handle_checkout(self):
		room_id = input("Room to checkout: ")
		if not self.validate_room_name_format(room_id):
			print("Invalid room ID")
			return
		success, message = self.hotel.checkout_room(room_id)
		print(message)

	def handle_clean(self):
		room_id = input("Room to mark clean: ")
		if not self.validate_room_name_format(room_id):
			print("Invalid room ID")
			return
		success, message = self.hotel.clean_room(room_id)
		print(message)

	def handle_repair(self):
		room_id = input("Room to repair: ")
		if not self.validate_room_name_format(room_id):
			print("Invalid room ID")
			return
		success, message = self.hotel.repair_room(room_id)
		print(message)

	def handle_list_rooms(self):
		self.hotel.list_rooms()

	def handle_list_available_rooms(self):
		self.hotel.get_available_rooms()

	def handle_reset(self):
		self.hotel = Hotel()


if __name__ == '__main__':
	interface = ManagementInterface()
	interface.main_loop()
