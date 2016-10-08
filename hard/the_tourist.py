import sys
import os


file_name = sys.argv[1]
if not os.access(file_name, os.R_OK):
    print "File does not exist"
    exit()

def cnvt(incm):
    ret = []
    for i in incm:
        if type(i) == list:
            ret.append(cnvt(i))
        else:
            ret.append(int(i))
    return ret

raw_routes = []
with open(file_name, 'r') as data:
    for string in data:
        tmp = string[:-1].split('|')
        tmp = [i.strip().split(' ') for i in tmp]
        tmp = cnvt(tmp)
        raw_routes.append(tmp)


class WayHolder:
    def __init__(self, id):
        self.id = id
        self.naighbour = []
        self.way_history = []
    def __str__(self):
        return '%s\n%s\n%s\n\n' % (self.id, self.naighbour, self.way_history)

def fabric(data):
    result = []
    point_counter = 0
    for i in data:
        #check both point way 4 detect max numb of points 
        if max(i[0],i[1]) > point_counter:
            point_counter = max(i[0],i[1])
    for i in range(point_counter):
        result.append(WayHolder(i+1))
    for i in data:
        result[i[0]-1].naighbour.append([i[1],i[2]])
        result[i[1]-1].naighbour.append([i[0],i[2]])
    return result

def jumper(pts, pos = 1, hist = ((1,),0),mpl=0):
    mpl+=3
    print '>'*mpl,'S ',pos,hist,pts[pos-1].naighbour
    if {i[0] for i in pts[pos-1].naighbour}.issubset(set(hist[0])):
        pts[pos-1].way_history.append(hist)
        print '>'*mpl,'write in ', pos, '? ', hist
    else:
        for nb_point in pts[pos-1].naighbour:
            print '>'*mpl,pos,' nb_pnt ', nb_point,'hist',hist
            if nb_point[0] not in hist[0]:
                tmp = (hist[0] + (nb_point[0],),hist[1] + nb_point[1])
                pts = jumper(pts,nb_point[0],tmp,mpl)
                print '<'*mpl,'hist',hist
    print '>'*mpl, ' func out', ' p',pos
    return pts

def handling(source_list):
    point_amount = len(source_list)
    lph = source_list[-1].way_history # last point history
    way_coasts = [way[1]  for way in lph if len(way[0]) == point_amount]
    return max(way_coasts)

# ******* RUN *******  #

print handling(jumper(fabric(raw_routes[2])))

bck_dt = jumper(fabric(raw_routes[2]))

for jojo in bck_dt:
    print jojo
