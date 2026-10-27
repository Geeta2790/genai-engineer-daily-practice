def divide_number(a,b):
    try:
        result = a/b
        print(result)

    except ZeroDivisionError:
        print("cannot divide by zero")
    except TypeError:
        print("Error: Cannot divide by zero")
    finally:
        print("execution finished")

divide_number(10,2)
divide_number(1,0)
divide_number("10", 2)