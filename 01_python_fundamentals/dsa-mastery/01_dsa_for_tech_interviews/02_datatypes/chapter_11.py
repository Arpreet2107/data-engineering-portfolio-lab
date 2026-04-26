import arrow

brewing_time = arrow.utcnow()#.shift(minutes=5)
brewing_time.to("Europe/Prague").format("YYYY-MM-DD HH:mm:ss")

from collections import namedtuple
chaiProfile = namedtuple("ChaiProfile",["flavor","aroma"])
