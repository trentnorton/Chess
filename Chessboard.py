from Player import *;

from Pawn import *;
from King import *;
from Queen import *;
from Rook import *;
from Bishop import *;
from Knight import *;

class Chessboard:
	white = Player();
	black = Player();
	
	board = [[None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None],
		 [None, None, None, None, None, None, None, None]];

	def reset(self):
		# clear the board
		for i in range (0,8):
			for j in range (0,8):
				self.board[i][j] = None;

		# black pieces
		for i in range (0,8):
			self.board[1][i] = Pawn(self.black);
		self.board[0][0] = Rook(self.black);
		self.board[0][1] = Knight(self.black);
		self.board[0][2] = Bishop(self.black);
		self.board[0][3] = Queen(self.black);
		self.board[0][4] = King(self.black);
		self.board[0][5] = Bishop(self.black);
		self.board[0][6] = Knight(self.black);
		self.board[0][7] = Rook(self.black);

		# white pieces
		for i in range (0,8):
			self.board[6][i] = Pawn(self.white);
		self.board[7][0] = Rook(self.white);
		self.board[7][1] = Knight(self.white);
		self.board[7][2] = Bishop(self.white);
		self.board[7][3] = Queen(self.white);
		self.board[7][4] = King(self.white);
		self.board[7][5] = Bishop(self.white);
		self.board[7][6] = Knight(self.white);
		self.board[7][7] = Rook(self.white);

	def move(self, player, oy, ox, dy, dx):
		if 0 <= oy < 8 and 0 <= ox < 8 and 0 <= dy < 8 and 0 <= dx < 8:
			if self.board[oy][ox] is not None and self.board[oy][ox].owner is player:
				if self.board[dy][dx] is None or self.board[dy][dx].owner is not player:
					if self.valid_move(self.board[oy][ox], oy, ox, dy, dx):
						self.board[dy][dx] = self.board[oy][ox];
						self.board[oy][ox] = None;		
						return True;
		return False;

	def valid_move(self, piece, oy, ox, dy, dx):
		if piece.name is "Pawn":
			if piece.owner is self.white:
				#attack
				if self.board[dy][dx] is not None and self.board[dy][dx].owner is self.black:
					if dy is oy - 1 and dx in [ox - 1, ox + 1]:
						return True;
					return False; 
				#two forward (intial)
				if oy is 6:
					if ox is dx and dy is 4:
						return True;
				#one forward
				if ox is dx and oy - 1 is dy:
					return True;
			elif piece.owner is self.black:
				#attack
				if self.board[dy][dx] is not None and self.board[dy][dx].owner is self.white:
					if dy is oy + 1 and dx in [ox - 1, ox + 1]:
						return True;
					return False; 
				#two forward (intial)
				if oy is 1:
					if ox is dx and dy is 3:
						return True;
				#one forward
				if ox is dx and oy + 1 is dy:
					return True;
			return False;
		elif piece.name == "Rook":
			if dy is oy:
				for i in range(min([ox+1,dx-1]),max([ox,dx-1])):
					print(str(dy) + " " + str(i));
					if self.board[dy][i] is not None:
						return False;
			elif dx is ox:
				for i in range(min([oy+1,dy-1]),max([oy,dy-1])):
					print(str(i) + " " + str(dx));
					if self.board[i][dx] is not None:
						return False;
			return True;
		elif piece.name == "Knight":
			if dy in [oy - 2, oy + 2]:
				if dx in [ox - 1, ox + 1]:
					return True;
			elif dx in [ox - 2, ox + 2]:
				if dy in [oy - 1, oy + 1]:
					return True;
			return False;
		elif piece.name == "Bishop":
			return True;
		elif piece.name == "Queen":
			return True;
		elif piece.name == "King":
			if dx in [ox - 1, ox + 1] and dy in [oy - 1, oy + 1]:
				return True;
			return False;	
	
	def print(self):
		line = str(" ");
		for i in range (0,8):
			line += "     " + str(i);
		print(line);
		print("  ----------------------------------------------------");
		for i in range (0,8):
			if i is not 0:
				print("  |--------------------------------------------------|");
			line = str(i) + " " + "| ";
			for j in range (0,8):
				if i % 2 != 0:
					if j % 2 != 0:
						line += "〖";
					else:
						line += "【";
				else:
					if j % 2 != 0:
						line += "【";
					else:
						line += "〖";
				if self.board[i][j] is not None:
						
					if self.board[i][j].owner is self.black:
						line += self.board[i][j].black_symbol;
					else:
						line += self.board[i][j].white_symbol;
				else:
					line += " ";	
				if i % 2 != 0:
					if j % 2 != 0:
						line += " 〗";
					else:
						line += " 】";
				else:
					if j % 2 != 0:
						line += " 】";
					else:
						line += " 〗";
			line += " |";
			print(line);
		print("  ----------------------------------------------------");
