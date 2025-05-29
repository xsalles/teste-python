import platform
import win32net

def get_local_users():
    users = []
    system_operation = platform.system()
    if system_operation == 'Windows':
        try:
            information_level = 0
            user_list, _, _ = win32net.NetUserEnum(None, information_level)
            for usuario in user_list:
                user_name = usuario['name']
                users.append({"username": user_name})
        except Exception as e:
            print(f"Ocorreu um erro ao listar usuários no Windows: {e}")
    elif system_operation in ('Linux', 'Darwin'):
        import pwd
        user_list = pwd.getpwall()
        for usuario in user_list:
            user_name = usuario.pw_name
            users.append({"username": user_name})
    return users