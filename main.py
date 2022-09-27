# Create a dictionary called `person`, it has three properties, `name` which is a string, `age` which is an integer, `hobbies` which is a list of strings.
person ={
    "name":"dalal",
    "age":30,
    "hobbies":["skiing", "tennis", "swimming", "coding"],}

# Create a function called `change_age` which takes the `person` dictionary and a `number` as arguments, this function changes the age in the dictionary to the `number`. The return value of this function is the updated dictionary.
#can i write this ?def change_age (person, person['age']):


def change_age(person, number):
    person["age"]= number
    return person

print(change_age(person, 21))


# Create a function called `add_hobby` which takes the `person` dictionary and a `hobby` as arguments. This function adds the hobby to the list of `hobbies` inside the person dictionary. The function will return the updated dictionary.


def add_hobby(person, hobby):
    extra_hobby= person["hobbies"]
    extra_hobby.append(hobby)
    return add_hobby
# can also be written person["hobbies"].append (hobby)

print(add_hobby(person, "Table Tennis"))


# CHALLENGE

# Create a function called `add_job` which takes `person` dictionary and `job` which is a string, as arguments. This function checks, if the dictionary does not have a property called `job` then it will add it to the dictionary. The function will return the updated dictionary.


def add_job(person, job):
    if person["job"] in person:
        return person
    else:
         person["job"]= job
    return person
        



# 2. Create a function called `check_hobbies`, which takes a person dictionary as an argument. This function checks the number of hobbies for this person, if it's more than three hobbies, print to the user a message telling them that they're talented.


def check_hobbies(person):
    if len(person["hobbies]") >3
        retun("you are talented")
