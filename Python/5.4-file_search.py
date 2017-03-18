__author__ = 'minin'


def file_search(folder, filename):
    path = str(folder[0])

    for element in folder[:]:
        if type(element) == list:
            if file_search(element, filename):
                path = path + "/" + file_search(element, filename)
        else:
            if element == filename:
                path = path + "/" + element

    if path == str(folder[0]):
        return False
    else:
        return path


print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
#print file_search(['D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak']], 'hey.py'],'find.me')
#print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')