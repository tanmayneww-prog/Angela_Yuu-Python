def calculate_love_score(name1 , name2):
    combined_names = name1 + name2
    lower_name = combined_names.lower()
     
    t = lower_name.count("t")
    r = lower_name.count("r")
    u = lower_name.count("u")
    e = lower_name.count("e")
        
    l = lower_name.count("l")
    o = lower_name.count("o")
    v = lower_name.count("v")
    e = lower_name.count("e")
    first_digit = t + r + u + e 
    second_digit = l + o + v + e 
    score = int(str(first_digit)+ str(second_digit))
    print(score)
calculate_love_score("alex", "robert")