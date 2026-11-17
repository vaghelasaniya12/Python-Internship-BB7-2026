admin_permissions = {"read", "write", "delete","manage_users"}

editor_permissions = {"read", "write"}

required_permissions = "delete"

if required_permissions in editor_permissions:
    print("Access granted")
else:
    print("Access denied")