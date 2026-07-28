class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=0
        stack=[
        ]
        operators=["+","-","*","/"]
        for i in tokens:
            if i not in operators:
                stack.append(i)
            else:
                if i =="+":
                    val1= stack.pop()
                    val2= stack.pop()
                    value = int(val1)+int(val2)
                elif i =="*":
                    val1= stack.pop()
                    val2= stack.pop()
                    value = int(val1)*int(val2)
                elif i =="/":
                    val1= stack.pop()
                    val2= stack.pop()
                    if val1 and val2:
                         value = int(val2)/int(val1)
                elif i =="-":
                    val1= stack.pop()
                    val2= stack.pop()
                    value = int(val2)-int(val1)
                stack.append(value)
        result = stack[0]
        return int(result)


        