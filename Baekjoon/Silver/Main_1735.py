os, om = input().split(" ")
ts, tm = input().split(" ")

os, om, ts, tm = int(os), int(om), int(ts), int(tm)

mother = om*tm
son = os*tm + ts*om

while son != 0:
    mother, son = son, mother%son


print((os*tm + ts*om)//mother, om*tm//mother)