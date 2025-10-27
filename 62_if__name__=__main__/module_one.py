# ********************************************************
# if __name__ == '__main__'
# ********************************************************



# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules


# pthon interpreter sets "special variables" one of which is __name__
# python will execute the code found within __main__

import module_two


def hello():
    print("Hello!")

if __name__ == '__main__':
    hello()
    # print("running other module directly")
    # pass
# else:
#     print("running other module indirectly")