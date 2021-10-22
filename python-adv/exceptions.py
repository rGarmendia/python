try:
    f = open("hello_world.txt")
    chivo = hallo
except Exception as e:
    print(e)
finally:
    print(f.read())

