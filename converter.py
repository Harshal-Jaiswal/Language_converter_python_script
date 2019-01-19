from googletrans import Translator

translator = Translator()
file = open(r"C:/Users/harsh/Desktop/eng.txt",'r')
new = open(r"C:/Users/harsh/Desktop/mar.txt",'w',encoding='utf-8')
for line in file:
    example = str(line)
    try:
    
        
        ex = example.index('>')
        ex1 = example.index("/")
        word = example[ex+1:ex1-1]

        x = translator.translate(word,dest='mr')
        x1=example[:ex+1]+x.text+example[ex1-1:]
        print(x1)
        new.write(x1)
    except:
        new.write(example)
new.close()
