#!/usr/bin/python2
xword = ["TELLZ",
		 "WRAMP",
		 "FGELZ",
		 "AHIEN",
		 "ABCDE"]

bank = ["TREE", "TELL", "RAM"]

def find_word(word, i, xword, x, y, actions = [[0, 1], 
											   [1, 0], 
											   [-1, 0], 
											   [0, -1], 
											   [-1, -1], 
											   [1, 1]]):
	if y > len(xword) - 1 or y < 0:
		return None
	if x > len(xword[0]) - 1 or x < 0:
		return None
	if i + 2 > len(word):
		return [[x, y]]
	if word[i] == xword[y][x]:
		for action in actions:
			new_x = x + action[0]
			new_y = y + action[1]
			pos = find_word(word, i + 1, xword, new_x, new_y, [action])
			if pos:
				return [[x, y]] + pos
				
def solve_xword(xword, bank):
	words = []
	
	for y in range(len(xword)):
		for x in range(len(xword[y])):			
			found = []
			for word in bank:
				word_pos = find_word(word, 0, xword, x, y)
				if word_pos:					
					words.append((word, word_pos))
					found.append(word)
			for word in found:
				bank.remove(word)			
			if len(bank) == 0: return words
	
					
print solve_xword(xword, bank)
					
				
			
			
