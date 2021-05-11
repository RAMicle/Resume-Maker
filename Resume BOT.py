print("                      Hello User\nMy Name Resume BOT And I am Here To Help You Build Your Resume")
print("               Please Do As Instructed\n\n")

Enter = input("Write Anything And Press Enter: ")

print("\n")

print("                 Some Considerations\n")
print("1. Limit your resume to one or two pages.")
print("2. Do not include birth date, health status or social security number.")
print("3. Limit the use of personal pronouns such as (I). Begin sentences with action verbs.")
print("4. Be honest but avoid writing anything negative in your resume.")
print("5. Make your resume error free. Have someone proof read it for you.")
print("6. Use a simple, easy to read font style, 10-14 point.")
print("7. Write All The Things Asked Here In An Organised Form Like In a Resume.")
print("8. After The Resume Is Built You Just Have To Assemble Them.")
print("9. Use high quality paper.")
print("\n")

Enter2 = input("Write Anything And Press Enter: ")

print("\n")

print("(Write Your Name.)")
Name = input("Tell Me Your Name: ")
print("\n")

print("(Write About Yourself.)")
About = input("Tell Me About Yourself: ")
print("\n")

print("(Write Your Contact Number(s), If More Than One, Separate Using (/).)")
Contact = input("Tell Me Your Contact Number: ")
print("\n")

print("(Write Your Email Address.)")
Email = input("Tell Me Your Email Address: ")
print("\n")

print("(Write Your Address.)")
Address = input("Tell Me Your Address: ")
print("\n")

print("(Write Your Date Of Birth.)")
DOB = input("Tell Me Your Date Of Birth: ")
print("\n")

print("(Write Your Nationality.)")
Nationality = input("What Is Your Nationality: ")
print("\n")

print("(Write Your Marital Status.)")
Marital_Status = input("What Is Your Marital Status: ")
print("\n")

print("(Write The Languages You Know.)")
Languages = input("Tell Me The Languages You Know: ")
print("\n")

print("(Write Your Skills Like Painting, Graphic Designing, Video Editing etc.)")
Skills = input("Tell Me Your Skills: ")
print("\n")

print("(Write Your Soft Skills Like Adaptability, Leadership, Teamwork, Problem Solving etc.)")
Soft_Skills = input("Tell Me Your Soft Skills: ")
print("\n")

print("(Write Your Hobbies.)")
Hobbies = input("Tell Me Your Hobbies: ")
print("\n")

print("(Write Your Achievements Like Awards etc.)")
Achievements = input("Tell Me Your Achievements: ")
print("\n")

print("(Write The Courses You Have Done Like Photo Shop, Video Editing etc.)")
Course = input("Tell Me The Courses You Have Done: ")
print("\n")

print("(Write The Extra-Curricular You Have Done.)")
Activities = input("Tell Me The Extra-Curricular Activities You Have Done: ")
print("\n")

print("(Write Your Education (Also Mention The Year).)")
Education = input("Tell Me Your Education: ")
print("\n")

print("(Write Your Work Experience (If Any) (Also Mention The Year And The Month.)")
Work = input("Tell Me Your Work Experience: ")
print("\n")

print("(Write The Internships You Have Done (If Any) (Also Mention The Year And The Month).)")
Internships = input("Tell Me The Internships You Have Done: ")
print("\n")

print("(Write Your Links Like LinkedIn, BEHANCE etc.)")
Links = input("Tell Me Your Links: ")
print("\n")

print("Your Resume Is Being Built....")
print("\n")

print("(Write 1 To 10 Without Any Spaces And Comas)")
Captcha = input("Captcha: ")
if Captcha == "12345678910":
    print("\n")
    print("Here Is Your Resume")
    print("\n")
    print("NAME\n\n" + Name + "\n\n")
    print("ABOUT ME\n\n" + About + "\n\n")
    print("CONTACTS\n\n" + Contact + "\n\n" + Email + "\n\n" + Address + "\n\n")
    print("PERSONAL DETAILS\n\n" + DOB + "\n\n" + Nationality + "\n\n" + Marital_Status + "\n\n")
    print("EDUCATION\n\n" + Education + "\n\n")
    print("LANGUAGES\n\n" + Languages + "\n\n")
    print("SKILLS\n\n" + Skills + "\n\n")
    print("SOFT SKILLS\n\n" + Soft_Skills + "\n\n")
    print("WORK EXPERIENCE\n\n" + Work + "\n\n")
    print("INTERNSHIPS\n\n" + Internships + "\n\n")
    print("HOBBIES\n\n" + Hobbies + "\n\n")
    print("ACHIEVEMENTS\n\n" + Achievements + "\n\n")
    print("COURSE\n\n" + Course + "\n\n")
    print("EXTRA CURRICULAR ACTIVITIES\n\n" + Activities + "\n\n")
    print("LINKS\n\n" + Links + "\n\n")
else:
    print("\n")
    print("Sorry Captcha Verification Failed")