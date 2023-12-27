def isAlienSorted(words, order):
    
    order_index = {char: i for i, char in enumerate(order)}
  
    def isOrdered(word1, word2):
        for i in range(min(len(word1), len(word2))):
       
            if word1[i] != word2[i]:
                
                if order_index[word1[i]] > order_index[word2[i]]:
                    return False
                
                return True
        
        return len(word1) < len(word2)
    
    for i in range(len(words) - 1):
        if not isOrdered(words[i], words[i + 1]):
            return False

    return True

words = ["habito", "hacer", "sonreir", "lectura"]
order = "hlabcdefgijkmnopqrstuvwxyz"
print(isAlienSorted(words, order))  