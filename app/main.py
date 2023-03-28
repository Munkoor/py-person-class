class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_objs = []

    for human in people:
        person = Person(human["name"], human["age"])
        people_objs.append(person)

    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]

        if human.get("husband"):
            Person.people[human["name"]].husband = Person.people[
                human["husband"]]

    return people_objs
