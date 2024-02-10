# Zackary Cleveland PHYS3000 P1.A

# Provided information
gpa_init = 3.5
credits_init = 66
credits_this_semester = 16
credits_total = credits_init + credits_this_semester

# GPA from WIT grading scale
a = 4.0
b_plus = 3.33
b_minus = 2.67

# Calculation of semseter final gpa
gpa_final = (a + (2 * b_plus) + b_minus)/4

# Calculation of cumulative gpa
gpa_cumulative = (gpa_init * (credits_init/credits_total)) + (gpa_final * (credits_this_semester/credits_total))

print("The students semester final GPA is:", gpa_final, ", and the cumulative GPA is now:", gpa_cumulative)