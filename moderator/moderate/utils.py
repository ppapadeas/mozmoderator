def is_admin(user):
    """Check if user is member of admin group"""
    return user.groups.filter(name='Admin').exists()
