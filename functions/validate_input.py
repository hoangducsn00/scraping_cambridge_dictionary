def isValidWord(user_input: str) -> bool:
    try:
        user_input = int(user_input)
        return False
    except ValueError:
        return True
