from ...flags import parser

class FlagModel():
    _pass = ""
    all = {}

    def __init__(self, long_name="", short_name="", help_str="", default_value=False):
        self.long_name = getattr(self, "long_name", False) or long_name
        self.short_name = getattr(self, "short_name", False) or short_name
        self.help = getattr(self, "help", False) or help_str
        self.default_value = getattr(self, "default_value", False) or default_value
        super().__init__()

        if __class__.all.get(self.long_name, False):
            raise Exception("Flag '{}' already exists.".format(self.long_name))

        optionals_params_kwargs = {}
        if self.help:
            optionals_params_kwargs["help"] = self.help

        if self.default_value:
            optionals_params_kwargs["default"] = self.default_value

        try:
            parser.add_option(
                "-{}".format(self.short_name),
                "--{}".format(self.long_name),
                **optionals_params_kwargs
            )
        except Exception as e:
            print(str(e))
        else:
            __class__.all[self.long_name] = self

    def get_all(self):
        return self.all

    def __call__(self, *args, **kwargs):
        """return true or false according to your flag logic"""
        if kwargs["value"]:
            self.default_value = kwargs["value"]

        return kwargs.get("password", False)
