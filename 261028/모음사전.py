#https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    answer_list = []
    char_list = ['A', 'E', 'I', 'O', 'U']
    
    def find_word(curr_word, answer_list):
        #print(curr_word)
        #if curr_word != "" and curr_word not in answer_list: #어차피 중복 생성 안함
        if curr_word != "":
            answer_list.append(curr_word)
            
        if len(curr_word) == len(char_list): return
            
        for i, c in enumerate(char_list):
            curr_word += c
            find_word(curr_word, answer_list)
            curr_word= curr_word[:-1]
    
    find_word("", answer_list)
    
    for i in range(len(answer_list)):
        if answer_list[i] == word:
            answer = i + 1
    
    return answer
