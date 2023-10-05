import pandas as pd
import json

# ------------------ EXTRACT -----------------------
# Extrai a lista de IDs de usuários a partir do arquivo CSV.
df = pd.read_csv(r'SDW2023.csv', encoding='utf-8') #enconding='utf-8' -> garanti que os caracteres sejam lidos corretamente
user_ids = df['User ID'].tolist()
print(user_ids)

# Ler um arquivo json e carrega eu conteúdo em uma lista. Arquivo contendo informações dos usuários.
with open(r'users.json', 'r', encoding='utf-8') as file:
    users = json.load(file)

# Função que recebe um ID como entrada e procura por um usuário correspondente.
# Caso não encontre retorna None.
def get_user(id):
    for user in users:
        if user['id'] == id:
            return user
    return None


selected_users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(selected_users, indent=2))

#----------------------- TRANSFORM -----------------------------
# Atualiza as informações dos usuários. Adicionando uma mensagem no campo 'news'
# caso não exista, ele é criado.
def update_user(user, message):
    if 'news' not in user:
        user['news'] = []
    user['news'].append(message)


for user in users:
    if user ['id'] in user_ids:
        message = {
            "id": 280,
            "icon": "novaintegrante_maria_livia.png",
            "description": f"Olha so {user['name']}! Maria Livia fez 7 meses!"
        }
        update_user(user, message)


#---------------------- LOAD ----------------------------------------
# Salva a informações atualizadas dos usuários no arquivo json.
print(json.dumps(selected_users, indent=2))


with open(r'users.json', 'w', encoding='utf-8') as file:
    json.dump(users, file, indent=2, ensure_ascii=False)

print("informações atualizadas e gravadas no arquivo users.json")


