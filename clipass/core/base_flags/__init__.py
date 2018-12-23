from importlib import import_module

init_flags = [
    "length",
    "max"
]

for module in init_flags:
    x = import_module(".model", "clipass.core.base_flags.{}".format(module))
