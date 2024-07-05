fruits = {"apple": 60, "avocado": 40, "watermellon": 15, "grapes": 200}

filted_fruits = filter(lambda t: t[1] > 50, fruits.items())


filted_fruits_dict = dict(filted_fruits)


print(filted_fruits_dict)
