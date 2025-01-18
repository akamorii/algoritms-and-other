
# X + (x+shift+iteration-tomod)%mod
vigenere_square = [[chr((((97)+(((97)+k+((123-97)-(123-i))-19)%26)))) for i in range(97, 123)] for k in range(0,26)]
# alph2 = [[j for j in range(0,26)] chr((((97+j)+(((97+j)+((123-97)-(123-i))-19)%26)))) for i in range(97, 123)]

def vigenere_sifr(keyword:str="key", text:str="hello", viginer_square=vigenere_square,encrypt=True ):
    chr_to_i = {x: chr(x+97) for x in range(26)} # 0:a
    
    i_to_chr = {chr(x+97):x  for x in range(26)} # a:0
    
    convert_to_num = lambda txt: [i_to_chr[x] for x in txt]
    
    num_key = convert_to_num(keyword)
    num_text = convert_to_num(text)
    
    
    
    
    # return chr_to_i
    

# for i in range(26):
#     val = 97
#     # iter = (123-97)-(123-i)
#     iter = i
#     shift = 3
#     test = [chr((((val)+(((val)+iter-19)%26))))]
#     test2 = (val+((val+shift+iter-19)%26))
#     print(test2)

# zxc = [[(i*2+j) for i in range (0,10)] for j in range(0,10)]

# print(alph)

# for i in vigenere_square:
#     print(i)

if __name__ == "__main__":
    print(vigenere_sifr())