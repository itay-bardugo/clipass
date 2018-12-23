class PasswordGenerator():
    allowed_chars = "abcdefghiklmnoqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+~:;"

    def __init__(self):
        self.generate()


    def generate(self):
        self._pass = __class__.allowed_chars
        return self.get_password

    @property
    def get_password(self):
        return self._pass

    @get_password.setter
    def set_password(self, password):
        self._pass = password
        return self