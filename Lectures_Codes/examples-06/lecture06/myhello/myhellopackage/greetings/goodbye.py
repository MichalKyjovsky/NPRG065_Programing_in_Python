# Module initialization code
print(f"Initializing module {__name__} ...")
goodbye_message = f"Goodbye from {__name__}"


# Inter-package dependency. referencing the say_n_times from the same top-level package
from .. conversation_utils import say_n_times


# The only content of the module
def say_goodbye(times: int = 1):
    say_n_times(goodbye_message, times)