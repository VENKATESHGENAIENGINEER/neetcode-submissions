class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horiznal_map={0:[],1:[],2:[],3:[],4:[],
        5:[],6:[],7:[],8:[]}
        square_map={"square1":[],
        "square2":[],"square3":[],"square4":[],"square5":[]
        ,"square6":[],"square7":[],"square8":[],"square9":[]}
        

        if len(board)!=9:
            return False
        for i in range(len(board)):
            if len(board[i])!=9:
                return False
            if is_digit_or_dot(list_str=board[i]) is False:
                return False
            if is_duplicate(board[i]) is False:
                return False
          
            
            if i<3:
                chunks = split_list(list_str=board[i])
                a1,a2,a3=chunks[0],chunks[1],chunks[2]
                
                square_map["square1"].append(a1)
                square_map["square2"].append(a2)
                square_map["square3"].append(a3)

            if i>2 and i<6:
                chunks = split_list(list_str=board[i])
                a1,a2,a3=chunks[0],chunks[1],chunks[2]
                square_map["square4"].append(a1)
                square_map["square5"].append(a2)
                square_map["square6"].append(a3)
            if i>5 and i<9:
                chunks = split_list(list_str=board[i])
                a1,a2,a3=chunks[0],chunks[1],chunks[2]
                square_map["square7"].append(a1)
                square_map["square8"].append(a2)
                square_map["square9"].append(a3)
            length= board[i]
            for j in range(len(length)):
                val = board[i]
                val1 = val[j]
                horiznal_map[j].append(val1)
        print(horiznal_map)

        for key,value in square_map.items():

            flat_list = [item for sublist in value for item in sublist]

            if is_duplicate(flat_list) is False:
                return False


        for key,value in horiznal_map.items():

            if is_duplicate(value) is False:
               return False





            
        
        return True 





def  is_digit_or_dot(list_str:List[str]) -> bool:
    for i in range(len(list_str)):
        if list_str[i] not in ["1","2","3","4","5","6","7","8","9","."]:
            return False
    return True
def is_duplicate(list_str:List[str]) -> bool:
    dict_map={}
    new_list = [x for x in list_str if x != '.']

    for i in range(len(new_list)):
        if new_list[i] in dict_map:
            return False
        else:
            dict_map[new_list[i]]=1
    return True
def split_list(list_str:List[str]) ->list:
    size=3
    chunks = [list_str[i:i + size] for i in range(0, len(list_str), size)]
    return chunks



        
