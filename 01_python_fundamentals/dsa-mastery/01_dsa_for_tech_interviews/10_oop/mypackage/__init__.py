
# Control what gets imported with "from mypackage import *"
__all__ = ['math_operations', 'string_operations']

# Package-level initialization code
print("Initializing mypackage")

# You can also import important items at package level
from .math_operations import add, multiply # type: ignore
from .string_operations import to_upper # type: ignore

# Package-level variables
__version__ = "1.0.0"
__author__ = "Your Name"