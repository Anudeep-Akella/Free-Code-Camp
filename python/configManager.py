def add_setting(all_settings,settings):
    key,value = settings[0].lower(),settings[1].lower()

    if key in all_settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    all_settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
    

def update_setting(all_settings,settings):
    key,value = settings[0].lower(),settings[1].lower()

    if key in all_settings:
        all_settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(all_settings,setting):
    
    key = setting.lower()
    if key in all_settings:
        del all_settings[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"

def view_settings(all_settings):
    if not all_settings:
        return "No settings available."

    print("Current User Settings:")
    return "Current User Settings:\n" + "\n".join(f"{k.capitalize()}: {v}" for k,v in all_settings.items()) + "\n"

test_settings = {'theme':'dark','volume':'medium'}
