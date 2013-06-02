class Rook:
	name = "Rook";
	white_symbol = "♖";
	black_symbol = "♜";
	owner = None;
	
	def __init__(self, owner):
		self.owner = owner;
