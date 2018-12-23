from clipass.core.models.flags import FlagModel
import random

class LengthModel(FlagModel):

    def __init__(self):
        self.short_name = "l"
        self.long_name = "length"
        self.help = "Password length"
        self.default_value = 10
        super().__init__()


    def __call__(self, *args, **kwargs):
        super().__call__(*args, **kwargs)

        loops = 0
        new_password = ""
        while loops < int(kwargs["value"]):
            new_password += kwargs["password"][random.randint(0, len(kwargs["password"])-1)]
            loops += 1

        return new_password

#init your model here
LengthModel()