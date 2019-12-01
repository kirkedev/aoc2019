from .. import read_input
from ..fuel import fuel_required

print(sum(map(fuel_required, read_input())))
