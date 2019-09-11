import unicodedata
import json





# https://www.unicode.org/Public/UNIDATA/Blocks.txt
# find tha name of block

file = open("Blocks.txt","r")
b = {}

for i in file:
    f = i.strip()
    xx = f.split(";")
    point = xx[0].split("..")
    name = xx[1].strip()
    ra =[]

    ra.append(int(point[0],16))
    ra.append(int(point[1],16))

    b[name] = ra

file.close()


def lang_detect(l):

    for er in list(b.keys()):
        if int(b[er][0]) <= int(l) <= int(b[er][1]):
            gy = str(er)
            break
        else:
            gy = "unknown"
    return gy



def name_detect(n):
    try:
        name = unicodedata.name(n)
    except:
        name = "unknown"
    return name




result_dic = {}

file = open("uf12_exist_draft_u12.txt","r")

for i in file:
    a = i.strip()
    result_dic[chr(int(a))] = {}

file.close()


# cat uf12_result_psnr/*.txt > all_u12_psnr_result.txt 
file = open("all_u12_psnr_result.txt","r")


# adding meta info
for i in file:
    v = i.strip()
    if "not similar" not in v:
        x = v.split(":")
        if len(list(result_dic[x[0]].keys())) == 0:
            result_dic[x[0]]["codepoint"] = x[3]
            result_dic[x[0]]["demical"] = int(x[2])
            result_dic[x[0]]["name"] = name_detect(chr(int(x[2])))
            result_dic[x[0]]["black_point"] = int(x[7])
            result_dic[x[0]]["lang"] = lang_detect(int(x[2]))
            sim = []
            m = {}
            m["char"] = x[1]    
            m["codepoint"] = x[5]
            m["demical"] = int(x[4])
            m["name"] = name_detect(chr(int(x[4])))
            m["black_point"] = int(x[8])
            m["lang"] = lang_detect(int(x[4]))
            m["psnr"] = float(x[6])
            sim.append(m)
            result_dic[x[0]]["similar_char"] = sim
        else:
            mm = {}
            mm["char"] = x[1]
            mm["codepoint"]=x[5]
            mm["demical"] = int(x[4])
            mm["name"] = name_detect(chr(int(x[4]))) 
            mm["black_point"] = int(x[8])
            mm["lang"] = lang_detect(int(x[4]))
            mm["psnr"] = float(x[6])
            result_dic[x[0]]["similar_char"].append(mm)
    else:
        w = v.split(":")
        del result_dic[w[0]]



file.close()





fw = open("u12_similar_char_list.json","w")

json.dump(result_dic, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))




