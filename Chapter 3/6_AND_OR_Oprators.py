# AND - Both Conditions Need True
name='sahil'
age=20
if name=='sahil' and age==20:
    print("True")
else:
    print("False")

name='sahil'
age=20
if name=='abc' and age==20:
    print("True")
else:
    print("False")


# OR - Only One Condition need true
name='sahil'
age=20
if name=='abc' or age==20:
    print("True")
else:
    print("False")