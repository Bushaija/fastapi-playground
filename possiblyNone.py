from typing import Optional, Union


# def say_hi(name: Optional[str] = None)
def say_hi(name: Union[str, None] = None):
    return (f"hey, {name}!" if name is not None else "Hello world")

print (say_hi('riwa'))
print (say_hi())

