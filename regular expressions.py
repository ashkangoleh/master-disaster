import re




text = '''this is text for test 
reqular expressions.
have a fun
'''


text = re.sub(
    r'\s{2,}',' ',text
)


print(text)