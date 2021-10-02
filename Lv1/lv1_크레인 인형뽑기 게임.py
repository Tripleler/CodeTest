def solution(board, moves):
    answer = 0
    st = []
    moves = [x-1 for x in moves]
    for col in moves:
        row = 0
        while row < len(board):
            if board[row][col] == 0:
                row += 1
            else:
                st.append(board[row][col])
                board[row][col] = 0
                break
    cnt = 0
    while True:
        if (cnt == (len(st)-1)) | (st == []):
            break
        if st[cnt] == st[cnt+1]:
            del st[cnt:cnt+2]
            answer += 2
            cnt = 0
        else:
            cnt += 1
    return answer
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))