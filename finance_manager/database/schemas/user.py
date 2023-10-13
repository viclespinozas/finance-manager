def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "name": user["name"],
            "last_name": user["last_name"],
            "transactions": user["transactions"]}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]