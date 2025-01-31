students = ["Alice", "Bob", "Charlie", "David"]
grades = [85,92,78,90]

students_grade = list(zip(students, grades))
#print(students_grade)

sentence = "Python is fun and Python is powerful"
sentence_words = set(sentence.split())
sentence_words = set()
#print(sentence_words)

states = ["Texas", "California", "Florida"]
cities = ["Houston", "Los Angeles", "Miami"]

state_cities = dict(zip(states,cities))
#print(state_cities)

#Grouping Cities Under States

group = {}
for state, city in state_cities.items():
    if state not in group:
        group[state] = []
        group[state].append(city)
print(group['Florida'])