import json
import numpy as np
import time




file = open("u12_similar_char_list.json","r")


dic_data = json.load(file)

sim_dic = dic_data.copy()

# Delete characters with black pixels less than 10 pixels 

for i in list(dic_data.keys()):
    if dic_data[i]["black_pixels"] < 10:
        del sim_dic[i]
    else:
        del_index = []
        for k in range(len(dic_data[i]["similar_char"])):
            if dic_data[i]["similar_char"][k]["black_pixels"] < 10:
                del_index.append(k)

        if len(del_index) != 0:
            sim_list = np.delete(sim_dic[i]["similar_char"],del_index).tolist()
            sim_dic[i]["similar_char"] = []
            sim_dic[i]["similar_char"].extend(sim_list)
            if len(sim_dic[i]["similar_char"]) == 0:
                del sim_dic[i]






sim_dic2 = sim_dic.copy()

# Delete characters with delta more than 7

for i in list(sim_dic.keys()):

    del_index = []
    for k in range(len(sim_dic[i]["similar_char"])):
       if sim_dic[i]["similar_char"][k]["delta"] >= 7:
            del_index.append(k)

    if len(del_index) != 0:
       sim_list = np.delete(sim_dic2[i]["similar_char"],del_index).tolist()
       sim_dic2[i]["similar_char"] = []
       sim_dic2[i]["similar_char"].extend(sim_list)
       if len(sim_dic2[i]["similar_char"]) == 0:
            del sim_dic2[i]







fw = open("simchar.json","w")

json.dump(sim_dic2, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))



