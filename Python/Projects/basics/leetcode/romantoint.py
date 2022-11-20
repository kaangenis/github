class Solution(object):
    def romanToInt(self):

        roman_List = ["I", "V", "X", "L", "C", "D", "M"]
        int_List = [1,5,10,50,100,500,1000]

        empty_List = []

        sys_In = str(input("Enter String Value: "))

        for a in sys_In:
            if sys_In == 1:
                print("I")
            elif sys_In == 5:
                print("V")
            elif sys_In == 10:
                print("X")
            elif sys_In == 50:
                print("L")
            elif sys_In == 100:
                print("C")
            elif sys_In == 500:
                print("D")
            elif sys_In == 1000:
                print("M")

            print(a)





Solution.romanToInt(self=Solution)
