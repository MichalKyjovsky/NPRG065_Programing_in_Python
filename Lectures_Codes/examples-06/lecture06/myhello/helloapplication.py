# FEATURES package definition, package initialization, importing packages, inter-package references

# Structure of the myhellopackage
#
# myhellopackage (package)
# |
# +-- greetings (subpackage)
# |   |
# |   +-- goodbye (module)
# |   |
# |   +-- hello (module)
# |
# +-- conversation_utils (module)
#
# goodbye references conversation_utils using the inter-package import


# Import hello module
import myhellopackage.greetings.hello

# Import goodbye module
from myhellopackage.greetings import goodbye

# Import say_n_times from conversation_utils module
from myhellopackage.conversation_utils import say_n_times


# Access say_hello, it is necessary to use full name
myhellopackage.greetings.hello.say_hello()

# Access goodbye directly, thanks to the from directive
goodbye.say_goodbye()
goodbye.say_goodbye(times=5)

# Access say_n_times directly, thanks to the from directive
say_n_times("My message", times=10)