class Car:
    Brand = ''
    Model = ''
    Year = ''

x = Car
x.Brand = 'Audi'
x.Model = 'A1'
x.Year = '2025'

print(x.Brand)
print(x.Model)
print(x.Year)

# Teams = [""] * 10
# Results = [[0 for i in range(3)] for j in range(len(Teams))]