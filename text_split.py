lines_per_file = 1143
smallfile = None
with open('HoLOCRtxtTrunc copy.txt') as bigfile:
    #i=1
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'HoL_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
        #i=i+1
    if smallfile:
        smallfile.close()
# fname='HoLOCRtxtTrunc copy.txt'
# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1
#
# print(file_len(fname))