# Hackerrank 

# https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    # Write your code here
    lst = []
    final_lst = []
    count = 0
    right = 0
    if(len(s)%3 == 0):
        for i in range(0,len(s),3):
            for j in range(i,i+3):
                lst.append(s[j])
            final_lst.append(lst)
            lst = []
        check_pair = ['S','O','S']
        for i in final_lst:
            if i==check_pair:
                pass
            else:
                if((i[0]!=check_pair[0])):
                    count += 1 
                if((i[1]!=check_pair[1])):
                    count += 1
                if((i[2]!=check_pair[2])):
                    count += 1
                print(count)
        return count
    else:
        return 0
