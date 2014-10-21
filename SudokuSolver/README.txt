#### Grace Hadiyanto
#### Assignment 9
#### E-mail: ifoundparis@gmail.com
#### CS 223P

Product: A program that reads in a text file of sudoku puzzles, solves them,
	and writes the solutions to another text file.

Description: This sudoku solver works, but can be very unpredictable with
	solving speed. On average, it takes 150-300 or so seconds to solve one
	hard sudoku puzzle with only 17 given starting cells. On occasion,
	if lucky, it can take 4 - 50 seconds. 

How to run: Make sure the puzzles are within one text file and formatted as 	one line per puzzle with 81 characters. Each cell has a symbol that
	is either represented by the numbers 1-9 or a period(‘.’) for an
	unknown cell.

	on the terminal, commands:
	python3.3 sudoku.py {textfilename.txt}

		where textfilename is the name of your text file.
	Please avoid using periods within the text file name.
	(i.e. don’t have a file that is named sudoku.puzzles.txt)

	The program will then solve the puzzle and print the solutions
	to a text file within the same directory called

	yourtextfilename-solution.txt

	where yourtextfilename was the original name of your text file.