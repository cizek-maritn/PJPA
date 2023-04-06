# -*- coding: utf-8 -*-

if __name__ == '__main__':
    f= open("large.txt", "r", encoding='utf-8-sig')
    text=f.read()
    f.close()
    #test_dict1 = {'a' : 1, 'c' : 1, 'm' : 1}
    #test_dict2 = {'a' : 2, 'm' : 1, 'c' : 0}

    #res = {key: test_dict2[key] - test_dict1.get(key, 0) for key in test_dict2.keys()}

    #print(str(res))
    text_arr=text.split('\n')
    door_count=int(text_arr[0])
    index=1
    results=""
    #print(text_arr)
    for i in range(door_count):
        lines=int(text_arr[index])
        index+=1
        dict_zac={}
        dict_kon={}
        for j in range(lines):
            zac=text_arr[index+j][0]
            kon=text_arr[index+j][text_arr[index+j].__len__()-1]
            if (dict_zac.__contains__(zac)):
                dict_zac.update({zac: dict_zac.__getitem__(zac)+1})
            else:
                dict_zac.update({zac: 1})
                if not (dict_kon.__contains__(zac)):
                    dict_kon.update({zac: 0})
            if (dict_kon.__contains__(kon)):
                dict_kon.update({kon: dict_kon.__getitem__(kon)+1})
            else:
                dict_kon.update({kon: 1})
                if not (dict_zac.__contains__(kon)):
                    dict_zac.update({kon: 0})
        index+=lines
        #print(res)
        #print(dict_zac)
        #print(dict_kon)
        if (dict_zac==dict_kon):
            results+=str(lines)+" "+"True" + '\n'
        else:
            res = {key: dict_kon[key] - dict_zac.get(key, 0) for key in dict_kon.keys()}
            pos=0
            neg=0
            for key in res.keys():
                if (res.get(key, 0)>0):
                    pos+=res.get(key, 0)
                elif (res.get(key, 0)<0):
                    neg+=res.get(key, 0)
            if (neg<-1) or (pos>1):
                results+=str(lines)+" "+"False" + '\n'
            else:
                results+=str(lines)+" "+"True" + '\n'
    results=results[:-1]
    w = open("vysledky.txt", "w", encoding='utf-8-sig')
    w.write(results)
    w.close()