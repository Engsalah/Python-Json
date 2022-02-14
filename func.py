import json
class Func:

    def __init__(self):
        self.user_messages()

    # This function shows some option for the user
    def user_messages(self):
        print("choose one of the following options : ")
        print("Write '1' to read all the data : ")
        print("Write '2' to change a value of a specific key : ")
        #print("Write '3' Create a new Json file : ")

        # To make sure the user input is an integer
        try:
            user_input = int(input())
            # Send the user_input to the function called input_check()
            self.input_check(user_input)
        except:
            print("Invalid option!!")
            self.user_messages()

    # This function checks on the user_input and calls another function
    # based on the value of the user_input
    def input_check(self,input_number):
        # Method to check if the input_number is an integer or not
        if isinstance(input_number, int) == True:
            if input_number == 1:
                self.func1_read()
            elif input_number == 2:
                self.func2_value()
            else:
                print("Invalid option!!")
                self.user_messages()
        else:
            print("Invalid option!!")
            self.user_messages()
    # This function asks the user if he wants to end the program or continue
    def loop_fun(self):
        self.user_input = input("Do you want to exit the program ? Y/N").upper()
        if self.user_input == 'Y':
            print("exit")
        elif self.user_input == 'N':
            self.user_messages()
        else:
            print("Invalid option!!")
            #self.loop_fun()


    # This function reads all the keys and values of the json file
    def func1_read(self):
        # Open and load the file with read option
        js_file = open("data.json", "r")
        json_object = json.load(js_file)
        # enumerate() is a function to read the keys and values of the json file
        for i1, (key1, value1) in enumerate(json_object.items()):
            # we check if the value is not a dictionary
            if type(value1) != dict:
                print((i1+1), key1, ":", value1)
            else:
                # if the value is a dictionary,
                # then we will consider it as a new dictionary
                for i2, (key2, value2) in enumerate(value1.items()):
                    print((i2+1+i1), key2, ":",value2)
        js_file.close()
        self.loop_fun()

    # This function to write a new value in the json file
    def func2_value(self):
        # open the file and load it with read option
        js_file = open("data.json", "r")
        # write all the content of the file in a variable called json_object
        json_object = json.load(js_file)
        # Close the file
        js_file.close()
        # Ask the user, which key value he wants to change
        find_key = input("Write the key name to set a new value : ")
        # Check the if that key is exist or not
        new_js_ob = json_object["address"]
        try:
            if json_object.get(find_key) != None:
                new_value = input("Set the new value of '" + json_object.get(find_key) + "' :")
                # change the key value to the new value
                json_object[find_key] = new_value
                print("Changed successfully!")
                self.write_data(json_object)
            elif new_js_ob.get(find_key) != None:
                new_value2 = input("Set the new value of '" + new_js_ob.get(find_key) + "' :")
                new_js_ob[find_key] = new_value2
                json_object["address"] = new_js_ob
                self.write_data(json_object)
                print("Changed successfully!")
            else:
                self.loop_fun()
        except:
                print("Error!!")
                self.loop_fun()

    def write_data(self,js_ob):
        # open the file one more time but this time with write option
        js_file2 = open("data.json", "w")
        # we append the content from json_object to the data.json
        json.dump(js_ob, js_file2)
        js_file2.close()
        self.loop_fun()
