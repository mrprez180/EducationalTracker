



def test():
    score = 0
    angles = 0
    proofs = 0
    lines = 0 
    polygons = 0 
    trig = 0
    
    #Test questions
    #Angles
    q1 = "What is the term for two angles that add up to 180 degrees? "
    q2 = "Angle a and angle b create a circle. Angle a is 274 degrees. What is the value of angle b? "
    q3 = "What is the term for two angles that add up to 90 degrees? "
    q4 = "True or False. Vertical Angles always have different values. "
    q5 = "Angle x and angle y form a right angle. Angle x is 38 degrees. What is the value of angle y? "
    #Proofs
    q6 = "To perform a basic calculation (addition, subtraction, multiplication, or division), which must you use? A postulate, a property, or a theorem? "
    q7 = "True or false. You can prove congruent triangles using the Side-Side-Angle Postulate. "
    q8 = "Right triangles can be proven congruent if its _____ and at least one of its legs are congruent. "
    q9 = "A quadrilateral is automatically a _____ if its diagonals share a midpoint. "
    q10 = "A quadrilateral is automatically a _____ if its diagonals are congruent. "
    #Lines
    q11 = "What is the name of a line with a point on one end and that goes on inifinitely on the other end? "
    q12 = "Line segment AC is 7 inches long and has a point at B. AB is 2.75 inches long. How many inches is BC? "
    q13 = "True or false. Both sides of a line segment's midpoint are congruent. "
    q14 = "What term is used to descrive multiple lines that will never intersect? "
    q15 = "What term is used to describe two lines that form a 90 degree angle? "
    #Polygons
    q16 = "What is the term for a polygon that is both a rhombus and a rectangle? "
    q17 = "A polygon with no inverse angles is called _____. "
    q18 = "A polygon with at least one inverse angle is called _____. "
    q19 = "How many sides are in a nonagon? "
    q20 = "True or false. An ellipse is a polygon. "
    #trigonometry
    q21 = "True or false. The tangent of angle is equal to the length of the hypotenuse divided by the length of the opposite side. "
    q22 = "Angle a’s hypotenuse has a length of 24, and its adjacent side has a length of 6. What is the cosine of angle a? "
    q23 = "Angle b’s opposite side has a length of 7, and its hypotenuse has a length of 35. What is the sine of angle b? "
    q24 = "True or false. Regardless of side lengths, each angle measure has specific values for tangent, sine, and cosine. "
    q25 = "True or false. The value of angle a divided by the sine of a in triangle ABC is equal to the value of angle b divided by the sine of b in triangle ABC. "
    
    print()
    a1 = input(q1)
    if a1 == "supplementary" or a1 == "Supplementary":
        score += 1
        angles += 1
    a2 = input(q2)
    if a2 == "86" or a2 == "86 degrees":
        score += 1
        angles += 1
    a3 = input(q3)
    if a3 == "Complementary" or a3 == "complementary":
        score += 1
        angles += 1
    a4 = input(q4)
    if a4 == "False" or a4 == "false":
        score += 1
        angles += 1
    a5 = input(q5)
    if a5 == "52" or a5 == "52 degrees":
        score += 1
        angles += 1
    a6 = input(q6)
    if a6 == "Property" or  a6 == "property":
        score += 1
        proofs += 1
    a7 = input(q7)
    if a7 == "False" or a7 == "false":
        score += 1
        proofs += 1
    a8 = input(q8)
    if a8 == "Hypotenuse" or a8 == "hypotenuse":
        score += 1
        proofs += 1
    a9 = input(q9)
    if a9 == "Rhombus" or a9 == "rhombus":
        score += 1
        proofs += 1
    a10 = input(q10)
    if a10 == "Rectangle" or a10 == "rectangle":
        score += 1
        proofs += 1
    a11 = input(q11)
    if a11 == "Ray" or a11 == "ray":
        score += 1
        lines += 1
    a12 = input(q12)
    if a12 == "4.25" or a12 == "4.25 inches" or a12 == "4.25 in":
        score += 1
        lines += 1
    a13 = input(q13)
    if a13 == "True" or a13 == "true":
        score += 1
        lines += 1
    a14 = input(q14)
    if a14 == "Parallel" or a14 == "parallel":
        score += 1
        lines += 1
    a15 = input(q15)
    if a15 == "Perpendicular" or a15 == "perpendicular":
        score += 1
        lines += 1
    a16 = input(q16)
    if a16 == "Square" or input(q16) == "square":
        score += 1
        polygons += 1
    a17 = input(q17)
    if a17 == "Convex" or a17 == "convex":
        score += 1
        polygons += 1
    a18 = input(q18)
    if a18 == "Concave" or a18 == "concave":
        score += 1
        polygons += 1
    a19 = input(q19)
    if a19 == "9" or a19 == "9 sides" or a19 == "Nine" or a19 == "nine":
        score += 1
        polygons += 1
    a20 = input(q20)
    if a20 == "False" or a20 == "false":
        score += 1
        polygons += 1
    a21 = input(q21)
    if a21 == "False" or a21 == "False":
        score += 1
        trig += 1
    a22 = input (q22)    
    if a22 == "0.25":
        score += 1
        trig += 1
    a23 = input(q22)
    if a23 == "0.2":
        score += 1
        trig += 1
    a24 = input(q24)
    if a24 == "True" or a24 == "true":
        score += 1
        trig += 1
    a25 = input(q25)
    if a25== "True" or a25 == "true":
        score += 1
        trig += 1
    
        
    print("You got a score of " + str(score) + " out of 25")
    print("You scored " + str(angles) + " out of 5 on the angle section")
    print("You scored " + str(proofs) + " out of 5 on the proofs section")
    print("You scored " + str(lines) + " out of 5 on the lines section")
    print("You scored " + str(polygons) + " out of 5 on the polygons section")
    print("You scored " + str(trig) + " out of 5 on the trigonometry section")
    if angles < 3:
        print("You have to work on angles!")
    if proofs < 3:
        print("You have to work on proofs!")
    if lines < 3:
        print("You have to work on lines!")
    if polygons < 3:
        print("You have to work on polygons!")
    if trig < 3:
        print("You have to work on trigonometry!")

print("Welcome to Placeholdername")
print("This application is meant to determine your proficiency in Geometry")
print("From there we can determine what actions to take to help improve your score")
print()

#1st part is to determine proficiency in geometry by measuring it via a pretest

#2nd part is to help and provide necessary resources to improve that score

#pretest section

print("Please take this pretest to determine your current ability in Geometry")
ready =  input("Type 'yes' if you are ready to begin: ")

if ready == "yes" or "YES" or "Yes" or "yEs" or "yeS" or "YEs" or "yES" or "YeS":
    test()
        
