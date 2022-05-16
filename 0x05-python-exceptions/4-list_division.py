#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    my_list = []
    num = 0
    app = 0

    for i in range(0, list_lenght):
        try:
            app = my_list_1[i] / my_list_2[i]
            num += 1
        except IndexError:
            print("out of range")
            app = 0
        except ZeroDivisionError:
            print("division by 0")
            app = 0
        except TypeError:
            print("wrong type")
            app = 0
        finally:
            my_list.append(app)

    return my_list
