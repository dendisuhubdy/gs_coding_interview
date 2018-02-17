import math

def takeClosest(num,collection):
   return min(collection,key=lambda x:abs(x-num))

def bestavg(scores):
    score_list = []
    for score in scores:
        value = math.floor(float(score[1]))
        if value != 100.0:
            score_list.append(value)
    avg = sum(score_list)/len(score_list)
    #closest = takeClosest(avg, score_list)
    max_avg = max(score_list)
    print(score_list)
    print(max_avtg

if __name__=="__main__":
    scores = [["sarah", "87"], ["Bobby", "100"], ["Elisa", "64"],
              ["Charles", "22"]]
    bestavg(scores)
