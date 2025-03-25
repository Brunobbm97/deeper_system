import json
import os
from datetime import datetime
from config import db
from models import User, UserPreferences

def parse_roles(user_dict):
    roles = []
    for key, value in user_dict.items():
        if key.startswith("is_user_") and value is True:
            role = key.replace("is_user_", "")
            if role not in ["active"]:  # Ignora is_user_active
                roles.append(role)
    return roles

def iso_to_timestamp(iso_str):
    dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
    return dt.timestamp()

def load_users_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    users_raw = data.get("users", [])  # <- PEGA A LISTA DE USUÁRIOS

    users_to_insert = []
    for item in users_raw:
        roles = parse_roles(item)
        prefs = UserPreferences(timezone=item["user_timezone"])
        user = User(
            username=item["user"],
            password=item["password"],
            roles=roles,
            preferences=prefs,
            active=item.get("is_user_active", True),
            created_ts=iso_to_timestamp(item["created_at"])
        )
        users_to_insert.append({
            "username": user.username,
            "password": user.password,
            "roles": user.roles,
            "preferences": {"timezone": user.preferences.timezone},
            "active": user.active,
            "created_ts": user.created_ts
        })

    if users_to_insert:
        db.users.insert_many(users_to_insert)
        print(f"{len(users_to_insert)} usuários inseridos com sucesso.")
    else:
        print("Nenhum usuário para inserir.")

# Execução direta
if __name__ == '__main__':
    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, '../users.json')
    load_users_from_json(json_path)
