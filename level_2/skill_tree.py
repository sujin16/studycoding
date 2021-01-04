def solution(skill, skill_trees):
    answer=0
    cur_string =''
    check =True
    
    for tree in skill_trees:
        arr =list(skill)
        for i,string in enumerate(tree):
            if string in skill:
                if string == arr[0]: cur_string =arr.pop(0)
                else:
                    check =False
                    i = len(tree) 
        if check ==True: answer+=1
        check =True
        cur_string =''
        
    return answer




skill="CBD"
skill_trees =["AEO"]
print(solution(skill,skill_trees))