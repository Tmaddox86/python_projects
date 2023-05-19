def hello():
    print("Hello, user!")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food_list):
    if list(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat", food_list[0])
        for food in food_list[1:]:
            print("Next I eat", food)

#Testing the hello() function
hello()

# Testing the pack() function
result = pack("lotion", "toothbrush", "clothes")
print(result)

# Testing the eat_lunch() function
eat_lunch(["sandwhich", "chips", "soda"])