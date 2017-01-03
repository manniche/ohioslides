
from slides import Slide
a_text = '''some text with **ordinary** _markup_
spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple lines spanning multiple 

and with paragraphs'''
a = Slide('A header', a_text)

print(a)
