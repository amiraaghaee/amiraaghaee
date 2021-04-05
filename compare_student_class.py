
class Health :
    countA_age : 0
    countA_height : 0
    countA_weight : 0
    countB_age : 0
    countB_height : 0 
    countB_weight : 0 

    def __init__(self, numA, numB, A, B):
        self.A = A
        self.B = B
        self.numA = numA
        self.numB = numB 


    def get_cls(self):
        for j in self.A[0]:
               Health.countA_age  += int(self.A[0][j])
        for j in self.A[1]:
               Health.countA_height  += int(self.A[1][j])
        for j in self.A[2]:
               Health.countA_weight  += int(self.A[2][j])
        for j in self.B[0]:
               Health.countB_age  += int(self.B[0][j])
        for j in self.B[1]:
               Health.countB_height  += int(self.B[1][j])
        for j in self.B[2]:
               Health.countB_weight  += int(self.B[2][j])
        Health.countA_age = Health.countA_age/self.numA
        Health.countA_height = Health.countA_height/self.numA
        Health.countA_weight = Health.countA_weight/self.numA
        Health.countB_age = Health.countB_age/self.numB
        Health.countB_height = Health.countB_height/self.numB
        Health.countB_weight = Health.countB_weight/self.numB

        return print("{}\n{}\n{}\n{}\n{}\n{}".format(
               float(Health.countA_age), 
               float(Health.countA_height),
               float(Health.countA_weight),
               float(Health.countB_age),
               float(Health.countB_height),
               float(Health.countB_weight))
               
class Compare(Health):
    def measurement(self):
        if (float(Health.countA_height) > float(Health.count_height)):
            return print('A')
        elif (float(Health.countA_height) < float(Health.count_height)):
            return print('B')
        else:
            if (float(Health.countA_weight) > float(Health.countB_wight)):
                return print('A')
            elif (float(Health.countA_weight) > float(Health.countB_weight)):
                return print('B')
            else:
                return print("Same")
        
                
            

num1 = int(input())

list_student_A = []
for i in range(3):
        inpusts = input()
        numbers = inpusts.split(' ')
        list_student_A.append(numbers)

num2 = int(input())
list_student_B = []
for i in range(3):
        inpusts = input()
        numbers = inpusts.split(' ')
        list_student_B.append(numbers)

vorodi_clss = Health(num1, num2, list_student_A, list_student_B)
vorodi_clss.get_cls()






