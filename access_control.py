def audit_log(func):
    """Decorator to log authorization start and completion."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control):
    # Logic: CONTROL_NUM * 3 + len(FAVORITE_ARTIST)
    # 9 * 3 + 6 = 33
    return control * 3 + 6

@audit_log
def validate_access(level):
    # Logic: threshold = CONTROL_NUM * 5
    # 9 * 5 = 45
    threshold = 9 * 5
    if level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"
