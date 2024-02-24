x0, y0 = map(float, input().split())
if ((x0-1)**2 + (y0)**2 <= 2**2) and ((x0-1)**2 + (y0)**2 >= 1**2):
    circle = "yes"
else:
    circle = "no"

if abs(x0-4) <= 2 and abs(abs(y0)-2) <= 3:
    rectangle = "yes"
else:
    rectangle = "no"
if circle == "yes" and rectangle == "no":
    print("yes no")
elif circle == "no" and rectangle == "yes":
    print("no yes")
elif circle == "yes" and rectangle == "yes":
    print("yes yes")
else:
    print("no no")
