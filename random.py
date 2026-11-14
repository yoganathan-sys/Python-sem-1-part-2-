import random
a=int(input("enter the number between 1 to 100:"))
q=0
b=False
while not b:
    q+=1
    c=random.randint(1,100)
    print(f"attempt {q}: Generated {c}")

    if c==a:
        b=True
print(f"\n the number {a} was found after {q} attempts!!!")

