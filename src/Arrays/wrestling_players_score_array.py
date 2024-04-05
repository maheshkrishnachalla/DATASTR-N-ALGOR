"""
sumo game
"""
import random
from timeit import default_timer as timer


class Solution:

    def sumo_win(self, arr: [int]) -> [int]:
        if len(arr) == 1 or len(arr) == 0:
            return arr
        else:
            while len(arr) > 1:
                first_max = max(arr)
                arr.remove(first_max)
                second_max = max(arr)
                arr.remove(second_max)
                d = first_max - second_max
                print()
                print("f_max : {first_max}, s_max : {second_max} ,difference : {d}".format(first_max=first_max,second_max=second_max,d=d))
                if d > 0:
                    arr.append(d)
                print("output :", arr)
            return arr


if __name__ == '__main__':
    arr = random.sample(range(1, 200), 10) #[2, 7, 4, 1, 8, 1, 1, 5, 16]
    s = Solution()
    print()
    print("input :",arr)
    start = timer()
    res = s.sumo_win(arr=arr)
    end = timer()
    #print(res) #9
    print("time :", end - start, " secs")
