import os

"""An implementation of the slide "presentation" software used by
dbeazley in the video from the PyOhio talk found here:
https://youtu.be/j6VSAsKAj98

Great talk, by the way. Go see it!

Usage is:

>>> from slides import Slide
>>> a_text = '''# A Header
...
... Some text with **ordinary** markup _inside_
... spanning multiple lines
...
... and with paragraphs
'''
>>> a = Slide( a_text )
>>> list_of_slides = [a]
>>> i = iter( list_of_slides )
>>> next(i)

Following the invocation of the last command, the REPL will clear the
screen and print out the formatted text inside an ascii box.
"""


class Slide(object):
    """The `Slide` class works in a REPL, by first clearing the terminal,
    then printing the next slide object text formatted in a box.

    One thing dbeazley did was:

    +--------------+
    | Slide header |
    |              |
    | slide text   |
    | slide text   |
    +--------------+

    >>> reasons = ['everywhere', 'flexible', 'performance', 'fun']
    >>> i = iter(reasons)
    >>> next(i)

    On the execution of the last statement, the screen clears and the
    slide referenced by 'everywhere' shows.

    Ideas:
        - use the `textwrap` module to format the box
        - use http://misc.flogisoft.com/bash/tip_colors_and_formatting
          for formatting text to most terms
    How:
        - did dbeazley increase the header? I suspect that iTerm,
          being a *graphical* terminal has some functionality for
          this, probably along the lines sketched out in
          http://superuser.com/questions/877010/increase-decrease-font-size-in-iterm2

    """

    def __init__(self, heading, text):
        """
        ... text for slide goes here
        """
        self.patterns = {'*': '\33[1m',
                         '_': '\33[4m',
                         'END': '\33[0m'}
        self.heading = heading
        self.text = text
        self.formatted = self._format_text(text)
        self.slide_text = self._draw_box()

    def _format_text(self, text):
        """
        takes the text as input and converts
        *text* to ascii bold text
        /text/ to ascii italic text
        _text_ to ascii underlined text

        returns the formatted text string
        """
        ret_text = []
        in_it = False
        for c in text:
            if c in self.patterns:
                if in_it:
                    c = self.patterns.get('END')
                    in_it = False
                else:
                    in_it = True
                    c = self.patterns.get(c)
            ret_text.append(self.patterns.get(c, c))
            
        ret_text = (''.join(ret_text)).split('\n')

        return ret_text

    def _split_line(self, line, width):
        return [line[i:i+width] for i in range(0, len(line), width)]


    def _split_msg(self, msg, width):
        lines = msg
        split_lines = [self._split_line(line, width-2) for line in lines]
        return [item for sublist in split_lines for item in sublist]


    def _draw_box(self, max_width=80):
        count = len(max(self.text.split('\n'), key=len)) + 2

        if count > max_width:
            count = max_width

        tb = "+" + "-" * count + "+"

        hdr = "\n| \33[7m{0}\33[0m |\n|{1}|".format(self.heading.ljust(count-2), "".ljust(count))
        msg = "\n".join("| " + x.ljust(count-2) + " |" for x in self._split_msg(self.formatted, count))

        return "{0}{1}\n{2}\n{0}".format(tb, hdr, msg)



    def __repr__(self):
        """
        formatting out goes here
        """
        os.system('clear');
        return self.slide_text
