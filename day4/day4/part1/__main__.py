import sys
from .. import is_increasing
from .. import has_double
from .. import parse_input


numbers = parse_input(sys.stdin)
matches = filter(lambda number: is_increasing(number) and has_double(number), numbers)
print(sum(1 for match in matches))
