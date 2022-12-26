#Creates identity matrix of n dimensions
def create_identity (dim):
    I = []
    
    count = 0
    for i in range(dim):
        row = []
        for j in range(dim):
            if (j == count):
                row.append(1)
            else:
                row.append(0)
                
           
        count  = count + 1
        I.append(row)
    
    return I
def is_matrix(M,m,n):
    

    for i in range(m):
        if len(M[i]) != n:
            return False
        
    return True
        
    
def give_transpose (M):
    
    m = len(M)
    n = len(M[0])
    
    M_t = create_matrix(n, m)
    
    for i in range(n):
        for j in range(m):
            M_t[i][j] = M[j][i]
            
    return M_t

def is_matrix_square (M):
    
    m = len(M)
    n = len(M[0])
    
    if (m == n):
        return True
    
    return False

#Gets any row i, indexing DOES NOT start from 0
def get_row (A, i):
    
    row_vector = A[i]
    
    return row_vector

#Gets any column j, indexing DOES NOT start from 0
def get_column (A, j):
    
    col = []
    dim = len(A)
    
    for i in range(dim):
        col.append(A[i][j])
        
    return col

#Does DOT PRODUCT of 2 vectors
def dot_product (u, v):
    
    if (len(u) != len(v)):
        return None
    
    else: 
        
        dot = 0
        dim = len(u)       
        for i in range(dim):       
            dot = dot + (u[i]*v[i])
        
    
    if round(dot,3) == 0:
        dot = 0
    return dot
        

def create_matrix (r, c ):
    
    M = []
    
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        M.append(row)
        
    return M

def matrix_multiply (A, B):
    
    dim_A_r = len(A)
    dim_A_c = len(A[0])
    dim_B_r = len(B)
    dim_B_c = len(B[0])
    
    AB = create_matrix(dim_A_r, dim_B_c)
    
    if (dim_A_c == dim_B_r):
        
        for i in range(dim_A_r):
            for j in range(dim_B_c):
                row_vect = get_row(A, i)
                col_vect = get_column(B, j)
                
                val = round(dot_product(row_vect, col_vect),6)
                AB[i][j] = val
            
        
        return AB
        
    else:
        return None

def user_matrix (i,j):
    M = []
    
    for i in range(i):
        row_str = input(f'Enter row {i + 1}: ').split()
        row = []
        
        for not_num in row_str:
            row.append(int(not_num))
            
        M.append(row)
        
    return M
    
    
    
def is_pivot (M,i, flag = 0):
    #Only returns None if row is empty
    
    k = len(M[0]) 
    if (flag):
        k = len(M[0]) - 1
    
    for j in range(k):
        if (M[i][j]):
            return j
        
    return None

    
   

def scalar_multiply (row, s):
    
    vector = []
    
    for i in row:
        vector.append(i*s)
    

    
        
    return vector


def scalar_matrix_multiply (M, s):
    
    M_copy = M.copy()
    dim = len(M)
    for i in range(dim):
        M_copy[i] = scalar_multiply(M_copy[i], s)
    
    return M_copy
    

def pivotable (M,i,j):
    #ROW OPERATION
    
    M_copy = []
    dim = len(M)
    factor = (1/M[i][j])
    
    
    for row in range(dim):
        if (row != i):
            M_copy.append(M[row])
        else:
            row = scalar_multiply(M[row], factor)
            M_copy.append(row)
            

    
    return M_copy
    

def row_last (M, i):
    
    i_copy = M[i].copy()
    
    del M[i]
    M.append(i_copy)
    
    return M
    
def is_row_zero (row, flag = 0):
    
    x = len(row)
    
    if flag:
        x = x - 1
        
    for i in (range(x)):
        if (row[i] != 0):
            return False
        
    return True 
    

def proj_sq_matrix (M):
    m = len(M)
    n = len(M[0])
    
    M_split = create_matrix(m, n-1)
    b = get_column(M, n - 1)
    b = give_transpose([b])
    
    
    
    
    for i in range(m):
        for j in range(n - 1):
            M_split[i][j] = M[i][j]

    if (is_system_consistent(M) and is_matrix_square(M_split)):
        return M
    else:
        
        M_split_t = give_transpose(M_split)
        M_square = matrix_multiply(M_split_t, M_split)  
        b_new = matrix_multiply(M_split_t, b)
        
        dim = len(M_square)
        #print(M_square,b,b_new)    
        
        for i in range(dim):
            M_square[i].append(b_new[i][0])
        
    

    return M_square
        

def ref (A, flag1 = 0):
    
    
    
    A_copy = A.copy()
    dim = len(A)
    
    #We find the pivot
        #We make that pivot pivotable
        #For that pivot, we find elimination matrices for ALL elements under that
        #that pivot (LOOP REQUIRED, in range (pivot row to last row))
        #We reduce A_copy for needed eliminations, and move to next pivot
        
        #ROW FULL OF ZEROES:
            #1. All rows below row of zeros are also rows of zeros : break
            #2. In case, there are non-zero rows below our row of zeros, then we
                #shift row of zeroes to the end and we don't increment in our row
                #value
                
        #NOTE: is_pivot function returns j value if there is a pivot, and None
                #if entire row is zeroes
    q = 0
    if (flag1):
        q = 1            
                
    i = 0
    while (i < dim):
        
        
        flag = False
        
        j = is_pivot(A_copy, i,q)
        
        
        
        if (j != None):
        
            A_copy = pivotable(A_copy, i, j)
            #Assuming it turns j
            
            for k in range(i + 1, dim):
                #Iterates through all elements below pivot i,j
                
                E = create_identity(dim)
                E[k][i] = - A_copy[k][j]
                
                A_copy = matrix_multiply(E, A_copy)
        
            i = i + 1
            
        
        
        else:
        #WE FOUND A ROW FULL OF ZEROS (NO PIVOT)
            
            flag = True
            #All rows below full of zeroes too
            for p in range(i, dim):
                k = 0
                if (flag1):
                    k = 1
                
                if (is_row_zero(A_copy[p],k)):
                    pass
                else:
                    flag = False
                    A_copy = row_last(A_copy, i)
                    break
                    #Non-zero row found
        
       
                
        if (flag):
            break
            
    
    A_copy.sort(reverse = True)

    return A_copy
        

def rref (M, flag2 = 0):
    
    k2 = 0
    if (flag2):
        k2 = 1
    
    A = ref(M,k2)
    A_copy = A.copy()
    count = 0
    
    '''
    print(count)
    for row in A_copy:
        print(row)
    print()
    '''
    
    dim = len(A)
    #no of rows
    
    for i in range(dim - 1, -1, -1):
        
        #Iterates from bottom index value to topmost
        
        j = is_pivot(A_copy,i,k2)
        #We check whether bottom row is 0 or not
         
        
        if (is_row_zero(A_copy[i],k2) == True):
            continue
            #found a zero row,  move upwards
            
        else:
            count = count + 1
            j = is_pivot(A_copy, i,k2)
            
            for k in range (i - 1, -1, -1):
                
                E = create_identity(dim)
                E[k][i] = - A_copy[k][j]
                
                A_copy = matrix_multiply(E, A_copy)
        
            '''
            print(" ")
            print(count, i, j)
            for row in A_copy:
                print(row)
            print()
            print("ELI ",k,j)
            for row in E:
                print(row)
            
            '''
    return A_copy


#1. Function that finds free variables (depends on consistency)


def is_system_consistent(S):
    #augumentation assumed
    
    S_ = rref(S,1)
    
    n = len(S)
    
    for i in range(n-1,-1,-1):
        
        if (is_row_zero(S_[i],1)):
            last = S_[i][-1]
            if (last != 0):
                return False
            
    return True


    
def free_variables (S):
    
    dim = len(S)
    free = {}
    for i in range(dim):
        free[i] = []
    
    for i in range(dim):
        
        
        j = is_pivot(S, i)
        
        if (j == None):
            continue
        else:
            for k in range(j + 1, dim):
                if (S[i][k]):
                    free[i] = free[i] + [k]
                    
                    
    return free


def give_solutions (A):
    
    S = A
    

    
    solution = []
    
    if (is_system_consistent(S)):
        if is_matrix_square(S):
            pass
        else:
            S=proj_sq_matrix(S)

        
        S = rref(S,1)
        
        free = free_variables(S)
        free_l = []
        dim = len(S)
        
        for i in range(dim):
            j = is_pivot(S, i)
            
            if(j == None):
                continue
            else:
                #pivot variable = rhs constant - all free variables
                pivot_variable = (j+1)
                rhs_constant = S[i][-1]
                
                free_list = free[i]
                free_list_neg = []
                
                for u in free_list:
                    
                    if (S[i][u] < 0):
                        free_vari = ' + ' + str(round((-S[i][u]),2)) + '(x' + str(u + 1) + ')'
                    else:    
                        free_vari = ' - ' + str(round((S[i][u]),2)) + '(x' + str(u + 1) + ')'
                    free_list_neg.append(free_vari)
                    
                
                o = [pivot_variable]    
                o.append(str(' = ' + str(round(rhs_constant,2)) + ''.join(free_list_neg) ))
                
                solution.append(o)
                
                
                
                for k in free.keys():
                    for i in free[k]:
                        if (i not in free_l):
                            free_l.append(i)
                            
        free_l.sort()

         
        for x in free_l:
            solution.append([x+1,' = Free'])
                    
        solution.sort()
        
        for i in solution:
            print("x" + str(i[0]) + i[1])
        
                
    else:
        print("\nInconsistent System")
        n = input("\nDO YOU WANT LEAST SQUARE SOLUTIONS? (YES OR NO) ").lower()
        print()
        if (n == "yes"):
            
            S = proj_sq_matrix(A)
            return give_solutions(S)
        
        else:
            return None
        
        

    
    
    
    
    
    
