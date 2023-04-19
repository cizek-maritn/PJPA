
def merge_tuples(line_a, line_b, line_c):
    
    max_size=line_a.__len__() + line_b.__len__() + line_c.__len__()
    ids=[[0 for i in range(4)] for j in range(max_size)]
    ids[0][0]=line_a[0][0]
    ids[0][1]=line_a[0][1]

    counter=1
    for i in range(line_a.__len__()):
        add_id=1
        for j in range(counter):
            if (ids[j][0]==line_a[i][0]):
                ids[j][1]=line_a[i][1]
                add_id=0
        if (add_id==1):
            ids[counter][0]=line_a[i][0]
            ids[counter][1]=line_a[i][1]
            counter+=1

    for i in range(line_b.__len__()):
        add_id=1
        for j in range(counter):
            if (ids[j][0]==line_b[i][0]):
                ids[j][2]=line_b[i][1]
                add_id=0
        if (add_id==1):
            ids[counter][0]=line_b[i][0]
            ids[counter][2]=line_b[i][1]
            counter+=1

    for i in range(line_c.__len__()):
        add_id=1
        for j in range(counter):
            if (ids[j][0]==line_c[i][0]):
                ids[j][3]=line_c[i][1]
                add_id=0
        if (add_id==1):
            ids[counter][0]=line_c[i][0]
            ids[counter][3]=line_c[i][1]
            counter+=1

    #print(ids)

    final={}

    for i in range(counter):
        final.update({ids[i][0]: ids[i][1:]})

    #print(final[3])

    return final

def simple_visual_test():
    
    
    line_a = ((1, 3), (3, 4), (10, 2))
    line_b = ((1, 2), (2, 4), (5, 2))
    line_c = ((1, 5), (3, 2), (7, 3))
    print(merge_tuples(line_a, line_b, line_c))

if __name__ == "__main__":
    simple_visual_test()
    #expected_result = {1: [3, 2, 5],
    #                   2: [0, 4, 0],
    #                   3: [4, 0, 2],
    #                   5: [0, 2, 0],
    #                   7: [0, 0, 3],
    #                   10: [2, 0, 0]}
    #print(expected_result[2])
    
