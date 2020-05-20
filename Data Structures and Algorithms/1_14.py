"""
************************************************************
**** 1.14. Sorting Objects Without Native Comparison Support
************************************************************


#########
# Problem
#########
# You want to sort objects of the same class,
# but they don’t natively support comparison operations.


#########
# Solution
#########
# The built-in `sorted()` function takes a key argument that can be passed a callable
# that will return some value in the object that sorted will use to compare the objects.
"""

from operator import attrgetter

# You have a sequence of `User` instances in your application,
# and you want to sort them by their `user_id` attribute,
# you would supply a callable that takes a `User` instance as input and returns the `user_id`


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f'User id is: {self.user_id}'


users = [User(1), User(24), User(12)]

# TODO
# Sort user instances(users) above by `user_id` using `lambda` expr
# Sort user instances(users) above by `user_id` using faster `attrgetter`
# Extract the `min` of `users` by `user_id` value and involving `attrgetter`
# Extract the `max` of `users` by `user_id` value and involving `attrgetter`


if __name__ == '__main__':
    print(sorted(users, key=lambda u: u.user_id))
