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
