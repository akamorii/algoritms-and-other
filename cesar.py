
alph = [chr(i) for i in range(97, 123)]

def cesar(text, shift:int = 0, sifr:bool = True) -> str:
    alph_index = lambda char: abs(97 - (ord(char)))
    res = [alph[alph_index(text[i])+shift] for i in range(len(text))]
    return ''.join(res)
    
    

if __name__ == "__main__":
    # print(alph)
    # print(abs(97 - (ord("a"))))
    print(cesar("hello", 2))
