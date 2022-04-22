"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

>>> user0, user1, user2 = User(), User(), User()
>>> user0.get_created_instances()
3
>>> user1.reset_instances_counter()
3
>>> user1.get_created_instances()
0
>>> user2.get_created_instances()
0

Ниже пример использования
"""


def instances_counter(cls):
    class Wrapper(cls):
        # initial counter value
        __instances_amt = 0

        def __init__(self, *args, **kwargs):
            # the function needed to apply the decorator to the class with some number of arguments
            super().__init__(*args, **kwargs)
            # +1 for counter value
            Wrapper.__instances_amt += 1

        # method independent of class instances
        @classmethod
        def get_created_instances(cls):
            return cls.__instances_amt

        @classmethod
        def reset_instances_counter(cls):
            save_amt = cls.__instances_amt
            cls.__instances_amt = 0
            return save_amt

    return Wrapper


@instances_counter
class User:
    pass


if __name__ == '__main__':
    # User.get_created_instances() # 0
    # user, _, _ = User(), User(), User()
    # user.get_created_instances() # 3
    # user.reset_instances_counter() # 3
    # user.get_created_instances() # 0
    import doctest

    print(doctest.testmod())
