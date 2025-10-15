Question_1 = int(input("""
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
: """))
Question_2 = int(input("""
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
: """))
Question_3 = int(input("""
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
: """))

answers = [Question_1, Question_2, Question_3]

houses = {
 "Gryffindor": 0,
"Ravenclaw": 0,
"Hufflepuff": 0,
"Slytherin": 0
}

   
if Question_1 == 1:
    houses["Gryffindor"] += 1
    houses["Ravenclaw"] += 1
elif Question_1 == 2:
    houses["Hufflepuff"] += 1
    houses["Slytherin"] += 1
else:
    print("wrong input")

if Question_2 == 1: 
    houses["Hufflepuff"] += 2
elif Question_2 == 2: 
    houses["Slytherin"] += 2
elif Question_2 == 3: 
    houses["Ravenclaw"] += 2
elif Question_2 == 4: 
    houses["Gryffindor"] += 2
else:
    print("wrong input")
    
if Question_3 == 1: 
    houses["Slytherin"] += 4
elif Question_3 == 2: 
    houses["Hufflepuff"] += 4
elif Question_3 == 3: 
    houses["Ravenclaw"] += 4
elif Question_3 == 4: 
    houses["Gryffindor"] += 4
else:
    print("wrong input")
    
print("House scores:", houses)
sum = max(houses, key=houses.get)
print(f"Your house is {sum}")