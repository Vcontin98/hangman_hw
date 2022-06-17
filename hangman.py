import random
key = ["drake","meek","bob", "lebron", "roze","melly","pitbull","tpain","xxxtentacion", "kodak"]

class Hangman:
  
  def __init__(self):
    self.word = random.choice(key) 
    self.display = ['_' for letter in self.word] 
    self.guesses = 0 
    
    
  def show(self): 
      display = ''.join(self.display) 
                                      
      print(f'the word is: {display}')
      
  
  def  get_word_index (self,guess):   
    location =[] 
    for index, char in enumerate(list(self.word)):
        if char == guess:         
          location.append(index)  
    return location 
    
  
  def update(self, idx, letter): 
    for number in idx: 
      self.display[number] = letter 
      
      
  def check_guess(self, guess): 
    if guess in self.word:  
      idx = self.get_word_index(guess) 
      self.update(idx, guess) 
      
  def win(self): 
    display =''.join(self.display)  
    word = self.word 
    if display == word: 
      print ("you win")
      return True 
      
# Game function
def game():
  word = Hangman() 
  while True:
    if word.guesses >= 7:
      print(f'you ran out of guesses and the word is {word.word}')
      break
    elif word.win(): #if win condition true break the loop
      break
    word.show()
    guess = input('guess a letter\n>>>>: ')      
    word.check_guess(guess.lower())
    word.guesses += 1  

#looping our game   
def gameloop():
  while True:
    again = input("Want to play a game? Y/N: ")
    if again.lower() == 'n':
      break
    elif again.lower() == 'y':
      game()
    else:
      print("invalid input")
    
  

gameloop()

      

