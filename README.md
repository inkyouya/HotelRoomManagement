# HotelRoomManagement

## Instalation instructions

### Requriements
Only requirement for running the `HotelRoomManagement` is Python (this was created in 3.10.4 but it should work for most versions of Python 3).

### Instructions
Download/checkout this repo

## Running the program
`management_interface.py` is the entrypoint for this program. To start it, run it with Python:
`python interface.py`

### Commands
assign      -> Assigns room nearest to the entrance
help        -> Brings out this message
checkout    -> Vacants a room that was occupied
clean       -> Marks a vacant room as cleaned
repair      -> Marks a room due for repair as vacant
list        -> Lists all rooms and their statuses
available   -> Lists all available rooms
reset       -> Turns all rooms available
exit        -> Exits this program

## Running tests
In order to run the tests, you will need to download pytest and any other requirements in test-requirements.txt:
`pip install test-requirements.txt`

After installing the requirents, simply run:
`python -m pytest`