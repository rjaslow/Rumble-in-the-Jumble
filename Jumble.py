#takes a string and returns a dictionary of key = letters, values = number of occurences
def jumble(word): 
    let_hist = {}
    for letter in word:  # itterates over the letters in the string
        if letter in let_hist:
            let_hist[letter]+=1 #if letter was already a key increment value
        else:                    
            let_hist[letter] = 1 #if letter is  not a key add it and set value to 1
    return let_hist

#takes base and case words and checks to see if the case can be created from base      
def anagram(b,c):
      for key in c:  #iterates over all keys in case
          if key not in b: #if there exists a key in case that is not in base-> fail
              return 0
          elif c[key]>b[key]: #if there exists a value in case larger than in base -> fail
              return 0
      return 1 

def main():
    debug = 0
    jumble_list = []

    base_word = input("Enter a word: ").lower()
    base_hist = jumble(base_word)

    file_name = input("Enter a text file to compare: ")   
    words_file = open(file_name,'r').read().splitlines()
    for case_word in words_file:
        case_hist = jumble(case_word.lower())
        #checks if case_word is a jumble of base_word and adds it to list if it is
        if (len(base_word)>=len(case_word)) and anagram(base_hist,case_hist):
            jumble_list.append(case_word)

    #for debuggin purposes set debug= 0 to disable
    if debug == 1: 
        print("jumble list:")          
        for i in jumble_list:
            print(i)


    return jumble_list


main()
