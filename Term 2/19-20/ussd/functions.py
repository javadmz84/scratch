from . import pages


def page_0():
    p = {
        '1': page_1,
    }
    print(pages.page_0)
    replay = input('replay: ')
    print("################")
    p[replay]()

def page_1():
    print(pages.page_1)
