#ORIGINAL PROGRAM
is_human_there = input("Is human present yes/no: ").lower()
is_daylight_there = input("Is daylight there yes/no: ").lower()
if   is_human_there == "yes" and is_daylight_there == "no" :
    print(" turn the light on")
else:
    print("turn the light off")


#EXAMPLE 2

eye_issue = input("If eye issue yes/no: ").upper()
skin_issue = input("If skin issue yes/no: ").upper()

if eye_issue == "YES" and skin_issue == "NO":
    print("Go to ophthalmologist")
elif eye_issue == "NO" and skin_issue == "YES":
    print("Go to dermatologist")
elif eye_issue == "YES" and skin_issue == "YES":
    print("Consult both ophthalmologist and dermatologist")
else:
    print("Think yourself!!!!!!!!!!!!!!!")
