def check_winner(board,mark):
    if((board[0][0]==mark and board[0][1]== mark and board[0][2]==mark )or

            (board[1][0]==mark and board[1][1]==mark and board[1][2]==mark )or

            (board[2][0]==mark and board[2][1]==mark and board[2][2]==mark )or 

            (board[0][0]==mark and board[1][0]==mark and board[2][0]== mark )or

            (board[0][1]==mark and board[1][2]==mark and board[2][1]==mark )or 

            (board[0][2]==mark and board[1][2]==mark and board[2][2]==mark )or 

            (board[0][0]==mark and board[1][1]==mark and board[2][2]==mark )or

            (board[0][1]==mark and board[1][1]==mark and board[2][0]==mark )):
            return True
def func(a):
    for i in a:
        for j in i:
            print(j,' ',end=(''))
        print()
a=[['-','-','-'],['-','-','-'],['-','-','-']]
i=1
while(i<=9):
    p='X'
    if(i%2==0):
        p='O'
    print(p,"'s turn:")
    print('give position row col (0-2 0-2)')
    n=input()
    n,m=[int(y) for y in n.split()]
    if a[n][m]=='-':
        a[n][m]=p
    else:
        i=i-1;
        print('invalid')
    func(a);
    if i>4:
        if(check_winner(a,p)==True):
            print(p,' is winner')
            break
    i+=1












