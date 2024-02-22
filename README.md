# ReplaceText
A simple GUI tool I use to replace text. Useful for working with broken databases that have poorly hondled UTF-8 characters.

Does one thing and does it reasonably well.

Comes pre-populated with Czech replacement options, edit the source if you wish to add more pre-populated options.

## Installing
Simply download the python file and run it using `python ReplaceText.py`.

Alernatively, make it executable on Linux and Mac OS using `chmod +x ReplaceText.py` in the appropriate folder.

## Usage
The tool takes an input in the main text field and then applies substitution rules in the following format:

`[C>c][%>@]`

will replace all `C`'s with `c`'s and `%`'s with `@`'s.

Pointy brackets (i.e. `>`) in a rule will likely break the program, do not use them.
