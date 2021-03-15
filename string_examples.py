s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''   # \ IS special for \n \r \t \b \f  \uXXXX \UXXXXXXXX  etc
s5 = r'spam\n'  # \ is not special

print(len(s1), len(s2), len(s3), len(s4), len(s5))
print('There\'s a good reason')
print("There's a good reason")
print("I \"think\" you can figure it out")
print('I "think" you can figure it out')

print("""There's a "good" reason for this""")

query = """
select *
from tests
where date > '2021/03/01'
"""
print(query)


