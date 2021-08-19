def make_album(name_after, n_album, quantity=''):
    album = {'after': name_after, 'name_album': n_album, 'quantity': quantity}
    return album


while True:
    print("\nHi please enter name after and name album.\n(If you to exit, enter 'q')")

    after = input("Enter name after:")
    if after == 'q':
        break

    name_album = input("Enter name album: ")
    if name_album == 'q':
        break

    q_track = input("Enter quantity track (optional): ")
    if q_track == '':
        result = make_album(after, name_album)
    else:
        result = make_album(after, name_album, q_track)

    print(result)

