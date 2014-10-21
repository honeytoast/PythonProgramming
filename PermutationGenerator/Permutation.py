#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment6

class Permutation:
    def __init__(self, l):
        self.l = sorted(l)

    def __iter__(self):
        while True:
            yield self.l
            # temporary list is made for storing indices and will be used to
            # determine the max index that satisfies conditions for swap
            self.temp = []
            for i in range(len(self.l) - 1):
                # the max index given by this condition our first critical index
                if self.l[i] < self.l[i + 1]:
                    self.temp.append(i)
            #if list is empty the previous permutation is the last
            if self.temp == []:
                raise StopIteration()
            self.x = max(self.temp)
            self.temp = []
            for i in range(len(self.l)):
                # the max index given by this condition our second critical index
                if self.l[self.x] < self.l[i]:
                    self.temp.append(i)
            self.y = max(self.temp)
            # swap values of the two critical indices in the list
            self.l[self.x], self.l[self.y] = self.l[self.y], self.l[self.x]
            # reverse the sublist from the next of the first critical index
            # until the last index in the list
            self.subl = self.l[self.x + 1:]
            self.subl = self.subl[::-1]
            self.l[self.x + 1:] = self.subl
            
def main():
    l = ['a','b','c']

    # print all permutations of the list
    permutations = Permutation(l)
    print('The permutations of {} are:'.format(l))
    for i in permutations:
        print(i)
    
    # print only the first n permutations
    perms = Permutation(l)
    n = 3
    print('The first {} permutations of {} are:'.format(n, l))
    for p in perms:
        print(p)
        n -= 1
        if n == 0:
            break

if __name__ == '__main__':
    main()
