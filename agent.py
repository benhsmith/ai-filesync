import os
from abc import ABC, abstractmethod
import json
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

class Object:
    def __init__(self, name):
        self.name = name

    def type(self) -> str:
        """
        Return the type of the object as a string.
        """
        return self.name

class Door(Object):
    def __init__(self, room):
        """
        Initialize a Room object.

        :param name: The name of the room.
        """
        super().__init__("Door")
        self.room = room

    def get_room(self):
        return self.room

class Room(Object):
    def __init__(self, name):
        """
        Initialize a Room object.

        :param name: The name of the room.
        """
        super().__init__("Room")
        self.name = name
        self.objects = {}  # Store objects in a dictionary by name

    def add_object(self, obj_name, obj_instance: Object):
        """
        Add an object to the room.

        :param obj_name: The name of the object.
        :param obj_instance: An instance of a class inheriting from Object.
        """
        self.objects[obj_name] = obj_instance

    def get_object(self, obj_name):
        """
        Get an object from the room by its name.

        :param obj_name: The name of the object to get.
        :return: The object instance if found, None otherwise.
        """
        return self.objects.get(obj_name, None)

    def remove_object(self, obj_name):
        """
        Remove an object from the room by its name.

        :param obj_name: The name of the object to remove.
        """
        if obj_name in self.objects:
            del self.objects[obj_name]

    def list_objects(self):
        """
        List all objects in the room.

        :return: A list of dictionaries containing object names and types.
        """
        return [{"name": name, "type": obj.type()} for name, obj in self.objects.items()]

    def __str__(self):
        """
        Return a string representation of the room and its objects.

        :return: A string describing the room and its objects.
        """
        return json.dumps({"room_name": self.name, "objects": self.list_objects()})

def describe_room(room):
    prompt = f"""
        I will provide a json object containing name and contents of a room.
        Describe this room and its contents briefly to someone has just stepped into the room. 
        This is the json object:
        {room}
    """

    #print (room)
    #print(prompt)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content

def get_user_action(room, response):
    output_format = '{"name": "OBJECT_NAME", "verb": "VERB"}'

    prompt = f"""
        I will provide a json object describing the contents of a room and a freeform string which
        you are to parse.
        Respond with a json object of the form {output_format} where OBJECT_NAME
        is a name in the json object I will provide and VERB is the verb that acted upon OBJECT_NAME in the freeform string. Output only json.
        This is the json description: 
        {room}
        This is the freeform string "{response}"
    """
    #print(prompt)
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

if __name__ == "__main__":
    furniture = Object("Furniture")

    entrance = Room("Entryway")
    entrance.add_object("shoe rack", furniture)
    living = Room("Living Room")
    living.add_object("sofa", furniture)
    living.add_object("book case", furniture)
    kitchen = Room("Kitchen")
    kitchen.add_object("stove", furniture)
    kitchen.add_object("refrigerator", furniture)
    kitchen.add_object("sink", furniture)
    kitchen.add_object("dishwasher", furniture)

    entrance.add_object("kitchen", Door(kitchen))
    entrance.add_object("living room", Door(living))

    print(describe_room(entrance))
    response = input("What would you like to do?\n")
    action = get_user_action(entrance, response)
    print(action)