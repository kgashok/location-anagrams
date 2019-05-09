def is_anagram(flist, word2): 
    #letterseq1 = sorted(list(word1.lower()))
    letterseq2 = sorted(list(word2.lower()))
    #return letterseq1 == letterseq2
    return flist == letterseq2
    
def group_locations_by (alist): 
    rlist = []
    for place in alist:
        for rl in rlist: 
            cslist = rl[0]
            if is_anagram(cslist, place):
                rl.append(place)
                #print(rl)
                break
        else:
            rlist.append([
                sorted(list(place.lower())),
                place.capitalize()
            ])

    return rlist
    

filename = "2017-2 UNLOCODE CodeList.txt"
#filename = "short_test.txt"

'''with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line

content = [x.strip() for x in content][10]
'''
lines = open(filename).read().split('\n')
places = []
invalid = 0

for line in lines: 
    try:
        tokens = line.split(" ")
        # print (tokens)
        loc = tokens[5].replace("'", "") or tokens[4].replace(",", "")
        if loc not in places:
            if loc.isalpha(): 
            #print("adding", loc, "...")
                places.append(loc)
            else:
                invalid += 1
                #print ("Ignoring nonAlpha:", loc, "in", line)
    except:
        invalid += 1
        #print ("Could not parse:", line)

# print(places)
print("Ignored", invalid, "lines")
print(len(places), "distinct places")

res = group_locations_by(places)

res.sort(key=len, reverse=True)
for rl in res:
    if len(rl) > 2:
        print(rl[1:])

