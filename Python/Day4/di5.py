default_settings = {    
    "theme": "light",
    "font size": 12,
    "language": "English",
    "notifications": True
}

user_settings = {
    "theme": "dark",
    "font size": 16
}
final_settings = default_settings.copy()
final_settings.update(user_settings)
print("Final Settings:", final_settings)
 