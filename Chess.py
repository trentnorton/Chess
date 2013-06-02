Chess Implementation
    Copyright (C) 2013  Trent Norton

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from Chessboard import Chessboard;

chessboard = Chessboard();
playing = True;

def main():
	print("Chess, v0.0.1, Trent Norton <trent@trentnorton.id.au>");
	chessboard.reset();
	chessboard.print();

	while playing:
		valid_input = False;
		while not valid_input:
			print("White move [row,column row,column]: ");
			white_input = input();
			valid_input = process_input(white_input, chessboard.white);	
		chessboard.print();
		
		valid_input = False;
		while not valid_input:
			print("Black move [row,column row,column]: ");
			black_input = input();
			valid_input = process_input(black_input, chessboard.black);	
		chessboard.print();

def process_input(input, player):
	global playing;
	if input in ["quit", "exit", "end", "terminate"]:
		exit();
	input = input.split();
	if len(input) is 2:
		orig = input[0].split(',');
		dest = input[1].split(',');
		if len(orig) is 2 and len(dest) is 2:
			orig_y = orig[0];
			orig_x = orig[1];
			dest_y = dest[0];
			dest_x = dest[1];
			if orig_y.isdigit and orig_x.isdigit and dest_y.isdigit and dest_x.isdigit:
				if chessboard.move(player, int(orig_y), int(orig_x), int(dest_y), int(dest_x)):	
					return True;
	return False;

if __name__ == "__main__":
	main();
