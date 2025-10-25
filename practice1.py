### 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？



from itertools import permutations
import math

### method 1
print("--------" + "Method 1 " + "------")
def practice1234():
        print("1234s")
        count = 0
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if( i != k ) and (i != j) and (j != k):
                        print (i*100+j*10+k)
                        count +=1
        print("total: "+ str(count))

# if __name__== "__main__":
#         practice1234()


### method 2
print("--------" + "practice 1 Method 2 " + "------")

# Define the digits
digits = [1, 2, 3, 4]

# Get all permutations of length 3
three_digit_numbers = permutations(digits, 3)

# Convert permutations to numbers and print them
for perm in three_digit_numbers:
    # Join the digits to form a number
    number = int(''.join(map(str, perm)))
    print(number)

# Count the number of three-digit numbers
total_count = len(list(permutations(digits, 3)))
print(f"Total unique three-digit numbers: {total_count}")

##explanantion: 
#1.1 map() 会根据提供的函数对指定序列做映射。 map(function, iterable, ...)
#1.2 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
#2.1 string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串

print("--------" + "practice 2 Method 1 " + "------")
### 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

#method 
def profitCalculate():
    i = int(input('净利润:'))
    arr = [1000000,600000,400000,200000,100000,0]
    rat = [0.01,0.015,0.03,0.05,0.075,0.1]
    r = 0
    for idx in range(0,6):
        if i>arr[idx]:
            r+=(i-arr[idx])*rat[idx]
            print ((i-arr[idx])*rat[idx])
            i=arr[idx]
    print (r)

# profitCalculate()


print("--------" + "practice 3 Method 1 " + "------")
### 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
def squareCalculate(amount):
    for idx in range(1, amount):
        sq1 =  math.sqrt(idx + 100)
        # print(math.modf(sq1))
        if math.modf(sq1)[0] != 0 :
            continue
        else:
            sq2 = math.sqrt(idx + 100 + 168)
            if math.modf(sq2)[0] != 0 :
                continue
            else:
                print(idx)

squareCalculate(100)