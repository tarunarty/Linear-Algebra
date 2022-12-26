import potato

print('                       WELCOME TO LINEAR ALGEBRA TOOLKIT')
print('                       _________________________________')



i = ''

while (i != '7'):
    print('\n1. Dot product\n2. Scalar Multiplication of Matrix\n3. Matrix Multiplication')
    print('4. Row Echelon Form\n5. Reduced Row Echelon Form \n6. System Solving (Least Square Solution also available)')
    print('7. Exit')
    
    i = input('ENTER CHOICE NUMBER: ')
    print()
    
    if (i == '1'):
        a = list(map(int,input("ENTER vector 1: ").split(' ')))
        b = list(map(int,input("ENTER vector 2: ").split(' ')))
        print()
        
        print('ANSWER: ',potato.dot_product(a, b))
        print('_________________________________')
    
    elif (i == '2'):
        m = int(input("ENTER number of rows: "))
        n = int(input("ENTER number of columns: "))
        print()
        
        flag = 1
        
        while flag:
        
            M = potato.user_matrix(m, n)
            print()
            
            if (potato.is_matrix(M,m,n)):
                flag = 0
            else:
                print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
        
        s = float(input("ENTER scalar: "))
        print()
        
        M = potato.scalar_matrix_multiply(M, s)
        
        for row in M:
            print(row)
        print()
        print('_________________________________')
    elif(i == '3'):
        
        flag_m = 1
        
        while flag_m:
        
            m = int(input("ENTER number of rows for matrix 1: "))
            n = int(input("ENTER number of columns for matrix 1: "))
            print()
            
            flag = 1
            
            while flag:
            
                A = potato.user_matrix(m, n)
                print()
                
                if (potato.is_matrix(A,m,n)):
                    flag = 0
                else:
                    print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
                    
            print()
            
            n_ = int(input("ENTER number of rows for matrix 2: "))
            p = int(input("ENTER number of columns for matrix 2: "))
            print()
            
            flag = 1
            
            while flag:
            
                B = potato.user_matrix(n_, p)
                print()
                
                if (potato.is_matrix(B,n_,p)):
                    flag = 0
                else:
                    print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
        
            if n == n_:
                flag_m = 0
                ANS = potato.matrix_multiply(A, B)
                for row in ANS:
                    print(row)
                print('_________________________________') 
                    
                
                
            else:
                print("\nINCOMPATIBLE DIMENSIONS")
                print()
                
            
        
        
        
    elif(i == '4'):
        
        m = int(input("ENTER number of rows: "))
        n = int(input("ENTER number of columns: "))
        print()
        
        flag = 1
        
        while flag:
        
            M = potato.user_matrix(m, n)
            print()
            
            if (potato.is_matrix(M,m,n)):
                flag = 0
            else:
                print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
        
        A = potato.ref(M)
        print()
        for row in A:
            print(row)
        
        
        print('_________________________________') 
        
    elif(i == '5'):
        
        m = int(input("ENTER number of rows: "))
        n = int(input("ENTER number of columns: "))
        print()
        
        flag = 1
        
        while flag:
        
            M = potato.user_matrix(m, n)
            print()
            
            if (potato.is_matrix(M,m,n)):
                flag = 0
            else:
                print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
        
        A = potato.rref(M)
        print()
        for row in A:
            print(row)
        
        
        print('_________________________________') 
        
        
    elif (i == '6'):
        
        print("ENTER CO-EFFICIENT MATRIX: ")
        
        m = int(input("ENTER number of rows: "))
        n = int(input("ENTER number of columns: "))
        print()
        
        flag = 1
        
        while flag:
        
            M = potato.user_matrix(m, n)
            print()
            
            if (potato.is_matrix(M,m,n)):
                flag = 0
            else:
                print("ERROR, INPUT IS NOT MATRIX OF GIVEN DIMENSIONS")
        
        print()
        
        print('ENTER vector of constants: ')
        
        for i in range(m):
            k = float(input(f'ENTER constant {i + 1}: '))
            M[i].append(k)
            
        print()
        
        B = potato.give_solutions(M)
        print('_________________________________')
    else:
        
        print("CHOOSE A NUMBER BETWEEN 1 and 7")
        
        
        
