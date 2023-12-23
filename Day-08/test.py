#lists

# student_name = ["mahesh", "jhon", "tim", "micheal"] #change --> mutable
student_name = ()"mahesh", "jhon", "tim", "micheal")  #throws error--> cant change -->immutable
# student_name.append("new_personn")
student_name.remove("tim")
print(student_name)