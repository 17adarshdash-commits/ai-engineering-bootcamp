def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

profile(Name = "Adarsh", Age = 19, Branch = "CSE AI", College = "MIT, Bengaluru")