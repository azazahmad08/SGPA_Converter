# Sgpa Converter
# Azaz Ahmad Swapnil
# only for 7 course result count


Course_1_cr = float(input("Enter your First Course Credit :"))
Course_1_res = float(input("Enter your First Course Result :"))
Count1 = (Course_1_cr * Course_1_res)

Course_2_cr = float(input("Enter your Second Course Credit :"))
Course_2_res = float(input("Enter your Second Course Result :"))
Count2 = (Course_2_cr * Course_2_res)

Course_3_cr = float(input("Enter your Third Course Credit :"))
Course_3_res = float(input("Enter your Third Course Result :"))
Count3 = (Course_3_cr * Course_3_res)

Course_4_cr = float(input("Enter your Fourth Course Credit :"))
Course_4_res = float(input("Enter your Fourth Course Result :"))
Count4 = (Course_4_cr * Course_4_res)

Course_5_cr = float(input("Enter your Fifth Course Credit :"))
Course_5_res = float(input("Enter your Fifth Course Result :"))
Count5 = (Course_5_cr * Course_5_res)

Course_6_cr = float(input("Enter your Sixth Course Credit :"))
Course_6_res = float(input("Enter your Sixth Course Result :"))
Count6 = (Course_6_cr * Course_6_res)

Course_7_cr = float(input("Enter your Seventh Course Credit :"))
Course_7_res = float(input("Enter your SeventhCourse Result :"))
Count7 = (Course_7_cr * Course_7_res)
# Now using all the count 1-7 we can calculate the exact sgpa

Sgpa_all = float(Count1 + Count2 + Count3 + Count4 + Count5 + Count6 + Count7)
Sgpa = float(Sgpa_all) / 13

if Sgpa > 3:
    print("Congratulations!! You Got First Class and your SGPA Is: ", Sgpa, )
elif Sgpa > 2:
    print("You got Second Class And your SGPA is :", Sgpa, )
elif Sgpa > 1:
    print("OH No! You got Third Class and your SGPA is: ", Sgpa, )
else:
    print("You got failed! Study Hard", Sgpa, )
Sgpa_total = "{:.2f}".format(Sgpa)
print(Sgpa_total)
print("Thank YOU")
