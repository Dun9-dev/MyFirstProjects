def send_message(messages):
    """Вывод сообщений, и перемещение уже отправленных сообщений"""
    while messages:
        current_msg = messages.pop()
        print(f"Content message: {current_msg}")
        compl_msg.append(current_msg)


uncompl_msg = ['test2', 'test3', 'test4', 'test5', 'test6']
compl_msg = []
send_message(uncompl_msg[:])
print(compl_msg)
print(uncompl_msg)
