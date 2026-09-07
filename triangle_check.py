def triangle():
  s1 = int(input("enter a no for first side")
  s2 = int(input("enter a no for second side")
  s3 = int(input("enter a no for third side")

if(s1 == s2 and s2 == s3):
    print("equilateral triangle")
elif(s1 == s2 or s1 == s3):
    print("isosceles triangle")
else:
  print("scalene triangle")
