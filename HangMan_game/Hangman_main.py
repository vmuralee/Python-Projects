import pdb
from random import choice
from pyfiglet import figlet_format

HangMan_pics = ['''
           +---+
           |   |
               |
               |
               |
           ======== ''','''
           +---+
           |   |
            O  |
               |
               |
           ========
           ''','''
           +---+
           |   |
            O  |
            |  |
               |
           ========
           ''','''
           +---+
           |   |
            O  |
           /|  |
               |
           ========
           ''','''
           +---+
           |   |
            O  |
           /|\ |
               |
           ========
           ''','''
           +---+
           |   |
            O  |
           /|\ |
           /   |
           ========
           ''','''
           +---+
           |   |
            O  |
           /|\ |
           / \ |
           ========
           '''
           
           ]

words=['GROOT','IRONMAN','SPIDERMAN','THOR','ROCKET','DRAX','DOCTOR.STRANGE','CAPTAIN.AMERICA','HAWK.EYE','HULK','ANTMAN']

def Index(letter,word):
	new=[x*0 for x in range(0,len(word))]
	pos=0
	while(letter!=word[pos]):
		pos=pos+1	
	#new.insert(pos,letter)
	return pos

def FillWord(list1,word):
        new_list=['_*' for x in range(0,len(word))]
        for iw in range(0,len(word)):
                for il in range(0,len(list1)):
                        if(list1[il]==word[iw]):
                                new_list.pop(iw)
                                new_list.insert(iw,list1[il])
        #print(''.join(new_list))
        return new_list

        
print(figlet_format('Welcome To HangMan'))
print('|------*------------------*-------------------*-------|')
is_Over=False
n=0
is_repetive=False
word = choice(words)
print('_*'*len(word))
new_word=[]
while(is_Over!=True):
	#string = 'Guess the Letter: '.rjust(50)
        let=input('Guess the Letter: ').upper()
        if let in word:
                index=Index(let,word)
                if let not in new_word:
                        new_word.insert(index,let)
                        temp_list=FillWord(new_word,word)
                        print("".join(FillWord(new_word,word)))
                        if(temp_list==list(word)):
                                print(figlet_format('Congratz'))
                                is_Over=True
                else:
                     print('You already used the letter, Please choose any other letter')           
        else:
                print(HangMan_pics[n])
                n=n+1
                if(n==7):
                        print("Better luck next time !!")
                        is_Over=True
