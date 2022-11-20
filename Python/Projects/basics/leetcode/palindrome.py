class Solution(object):
    def palin(self, x):

        x = str(input("Input The Number: "))

        number_Reverse = x[::-1]

        print("Your number is:  ", x)
        print("Your numbers reversed value is: ", number_Reverse)

        if x == number_Reverse:
            print("Your number is a Palindrome Number.")
        else:
            print("Your Number Is Not a Palindrome Number.")


        """
        :type x: int
        :rtype: bool
        """

