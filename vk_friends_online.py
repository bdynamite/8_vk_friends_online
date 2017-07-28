import vk
import getpass


APP_ID = 1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    return input('login: ')


def get_user_password():
    return getpass.getpass('password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope = 'friends'
    )
    api = vk.API(session)
    friends_id = api.friends.getOnline(online_mobile1=1)
    friends_info = api.users.get(user_ids=friends_id)
    return friends_info


def output_friends_to_console(friends_online):
    print('online friends: ')
    print('\n'.join([f'{x["first_name"]} {x["last_name"]}' for x in friends_online]))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
