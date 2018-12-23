from .core.commands.args import received_options
from .core.models.flags import FlagModel
from .core.base_flags.max.model import MaxModel
from .core.models.flag_error import FlagError


def generate_password():
    from .core.models.password_generator import PasswordGenerator
    PasswordGenerator = PasswordGenerator()
    output = []

    try:
        while True:
            passwd = PasswordGenerator.generate()
            new_pass = None

            for option, value in received_options.__dict__.items():
                try:
                    Model = FlagModel.all.get(option, False)
                    if not isinstance(Model, FlagModel):
                        raise Exception("your model is not an instance of FlagModel")

                except Exception as e:
                    raise Exception(str(e))

                else:
                    try:
                        new_pass = Model(password=(new_pass or passwd), value=value)
                    except FlagError as e:
                        #one failed, restart.
                        new_pass = None
                        break

            if new_pass is not None:
                if int(output.__len__()) >= int(MaxModel.get_instance().get_default_value()):
                    raise Exception("finished?")
                else:
                    output.append(str(new_pass))
    except:
        loop = 1
        for generated_password in output:
            print(generated_password, end="\n" if loop % 4 == 0 else " ")
            loop += 1
