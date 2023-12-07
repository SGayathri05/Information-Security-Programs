Key = { "a":"b", 'c':'d', 'e':'f', 'g':'h', 'i':'j', 'k':'l', 'm':'n', 'o':'p',
        'q':'r', 's':'t', 'u':'v', 'w':'x', 'y':'z', 'z':'y', 'x':'w', 'v':'u',
        't':'s', 'r':'q', 'p':'o', 'n': 'm', 'l':'k', 'j':'i', 'h':'g', 'f':'e',
        'd':'c', 'b':'a', ' ': ' ', '.':'.'     
}

key_list = list(Key.keys())
value_list = list(Key.values())
s = ''

def encrypt(word):
  word = word.lower()
  ls = [value_list.index(i) for i in word]
  ls2 = [key_list[j] for j in ls]
  x = s.join(ls2)
  return (s.join(ls2))

def decrypt(word):
   word = word.lower()
   ls = [value_list.index(i) for i in word]
   ls2 = [key_list[j] for j in ls]
   return (s.join(ls2))

word = input("Word: ")
x = encrypt(word)
print("Encryption: ", x)
print("Decryption: ", decrypt(x))
