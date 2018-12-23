from ...models.flags import FlagModel


class MaxModel(FlagModel):
    __instance = None

    def __init__(self):
        if __class__.__instance is not None:
            raise ("Singleton!")

        self.short_name = "m"
        self.long_name = "max"
        self.help = "max passwords"
        self.default_value = 16
        super().__init__()

        __class__.__instance = self

    @staticmethod
    def get_instance():
        if __class__.__instance is None:
            __class__.__init__()
        return __class__.__instance

    def get_default_value(self):
        return self.default_value

    def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)


MaxModel()
