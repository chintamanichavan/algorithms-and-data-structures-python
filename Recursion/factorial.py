class Factorial:
    def cal_fact(self, num):

        if num == 0 or num == 1:
            print("The factorial of {} is 1.".format(num))
            return 1

        if num > 1:
            return num * self.cal_fact(num - 1)

def main():
    num = 6
    d = Factorial()
    result = d.cal_fact(num)

if __name__ == '__main__':
    main()
