# What was that?

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("""
*** Escape Sequences ***
\\\\\t Backslash (\\)
\\
\\\'\t Single-quote(\')
\'
\\\"\t Double-quote(\")
\"
\\a\t ASCII bell (BEL)
\a
\\b\t ASCII backspace (BS)
\b
\\f\t ASCII formfeed (FF)
\f f
\\n\t ASCII linefeed (LF)
\t
\\N\{name\}\t Character named name in the Unicode database (Unicode only)
\\r\t Carriage Return (CR)
\r
\\t\t Horizontal Tab
\\uxxxx\t Chaacter with 16-bit hex value xxxx
\\Uxxxxxxxx\t Character with 32-bit hex value xxxxxxxx
\\v\t ASCII vertical tab (VT)
\v
\\ooo\t Character with octal value ooo
\\xhh\t Character with hex value hh
""")
