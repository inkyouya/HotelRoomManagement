from hotel import Hotel

def main_loop():
	help_message = "help message"
	valid_commands = ["exit", "help"]
	print(help_message)
	while True:
		command = input("Please enter a command:")
		if command not in valid_commands:
			print("oops, hint: use \"help\" for help")
		elif command == "exit":
			break
		elif command == "help":
			print(help_message)