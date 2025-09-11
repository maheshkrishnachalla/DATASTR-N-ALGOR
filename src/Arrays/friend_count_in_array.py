"""
Given a 2D array of user IDs, find the number of friends a user has. Note that users can have none or multiple friends.
Constraints

The input variable user_ids is a 2D array of user IDs.
Each element in the user_ids array is a list of integers representing the user IDs.
The user IDs can be any positive or negative integer value.
The user_ids array can have any number of rows and columns.
The user IDs within each row can be in any order.
The user_ids array can contain duplicate user IDs.
The output variable is a dictionary (Dict[int, int])
where the keys are the user IDs and the values are the count of friends for each user.

Input: [[4, -3, 15], [15, 22, 4], [-3, 4, 22]]
Output: {"4": 3, "-3": 2, "15": 2, "22": 2}

Input: [[3, 7, 8, 7], [8, 3], [7, 8, 7, 3]]
Output: {"3": 3, "7": 4, "8": 3}

Input: [[-10, 20], [30, -10], [20, 30], [20, -10]]
Output: {"20": 3, "30": 2, "-10": 3}
"""

def count_friends(user_ids):
    """
    :type user_ids: List[List[int]]
    :rtype: Dict[int, int]
    """
    dt = {}
    for users in user_ids:
        for i in users:
            if i in dt.keys():
                dt[i] = dt[i]+1
            else:
                dt[i] = 1
    return dt


user_ids = [[-10, 20], [30, -10], [20, 30], [20, -10]]#[[3, 7, 8, 7], [8, 3], [7, 8, 7, 3]]#[[4, -3, 15], [15, 22, 4], [-3, 4, 22]]
result = count_friends(user_ids=user_ids)
print(result)