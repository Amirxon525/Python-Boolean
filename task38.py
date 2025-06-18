logged_in = True
session_time = 90

is_not_active = logged_in == False or session_time == 0 
print(is_not_active)