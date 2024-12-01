import db

def is_token_valid(token_str):

    result = db.select("td_tokens","*", {
        "token": token_str
    })

    return len(result) == 1

def get_user_id_by_token(token):

    result = db.select("td_tokens","username", {
        "token": token
    })

    user_name = result[0][0]

    result_id = db.select("td_users", "id", {
        "username" : user_name
    })

    return result_id[0][0]
