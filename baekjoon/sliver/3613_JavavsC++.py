# 알고리즘 분류 : 문자열
# 문제 설명 : 변수명 바꾸기
# 핵심 개념 : 예외 처리, lower(), upper(), capitalize()

def JavatoCpp(variable):
    error = "Error!"
    
    converted_result = []
    
    for idx in range(len(variable)):
        if variable[idx].isupper():
            if idx == 0:
                return error
            else:
                converted_result.append(f"_{variable[idx].lower()}")
        else:
            converted_result.append(variable[idx].lower())
            
    return "".join(converted_result)


def CpptoJava(variable):
    error = "Error!"
    
    converted_result = []
    
    if "__" in variable:
        return error
    if variable[0] == "_" or variable[-1] == "_":
        return error
    if not variable.islower():
        return error
    
    for word in variable.split("_"):
        if not converted_result:
            converted_result.append(word)
        else:
            converted_result.append(word.capitalize()) # capitalize() : 첫글자 대문자, 나머지 소문자로 변환
        
    return "".join(converted_result)


variable = input()
    
if "_" in variable:
    print(CpptoJava(variable))
else:
    print(JavatoCpp(variable))