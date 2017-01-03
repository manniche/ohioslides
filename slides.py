import os

"""An implementation of the slide "presentation" software used by
dbeazley in the video from the PyOhio talk found here:
https://youtu.be/j6VSAsKAj98

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
    """

    The `Slide` class works in a REPL, by first clearing the terminal,
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
    """

    def __init__(self, text):
        """
        ... text for slide goes here
        """
        self.text = text

    def __repr__(self):
        """
        formatting out goes here
        """
        os.system('clear');
        return self.text
