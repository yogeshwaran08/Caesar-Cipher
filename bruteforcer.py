import sys

#test case sample
#YKIXKZSKYYGMK

if len(sys.argv) < 2:
   print("Format : python decoder.py enc_msg")
   exit("No Argument provided")

message = sys.argv[1]
Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(Letters)):
   translated = ''
   for ch in message:
      if ch in Letters:
         num = Letters.find(ch)
         num = num - key
         if num < 0:
            num = num + len(Letters)
         translated = translated + Letters[num]
      else:
         translated = translated + ch
   print('Hacking key is %s: %s' % (key, translated))