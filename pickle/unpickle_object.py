import pickle

class example_class:
    a_number = 35
    a_string = "hey"
    a_list = [1, 2, 3]
    a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
    a_tuple = (22, 23)

my_object = example_class()
my_object.a_dict = None
pickle_file = open('test.pkl', 'rb')
my_unpickled_object = pickle.load(pickle_file)  # Unpickling the object
print(
    f"This is a_dict of the unpickled object:\n{my_unpickled_object.a_dict}\n")

