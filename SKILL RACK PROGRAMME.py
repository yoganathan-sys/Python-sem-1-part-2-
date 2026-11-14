A=input("")
B=input("")
GDP=input()
try:
    GDP_Value=float(GDP)
    GDP_formatted=f"{GDP_Value:.2f}"
except ValueError:
    GDP_formatted=GDP
print(f"The capital of {A.capitalize()}is {B}and it's GDP is {GDP_formatted}")
