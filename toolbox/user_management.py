"""
Toy class for managing user identities with basic example methods.
"""
class userManager:

    def __init__(self):
        pass

    def reverse_name(self, name):
        return ''.join(reversed(name))


if __name__ == "__main__":
    umanager = userManager()
    print(umanager.reverse_name('HONG'))