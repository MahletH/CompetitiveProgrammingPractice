class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_dict,guess_dict = {},{}
        bulls,cows = 0,0
        
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i]in secret_dict:
                    secret_dict[secret[i]] += 1
                else:
                    secret_dict[secret[i]] = 1
                    
                if guess[i] in guess_dict:
                    guess_dict[guess[i]] += 1
                else:
                    guess_dict[guess[i]] = 1
                
        keyG = secret_dict.keys()
        keyS = guess_dict.keys()
        
        for n in (set(keyG) & set(keyS)):
            cows += min(secret_dict[n],guess_dict[n])
        
        return f'{bulls}A{cows}B'