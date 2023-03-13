import time

banner = r'''
  _____   ____     ____    _____  __       __ _________   _____         ___      _____   ________
 /       /     \   |   \   |        \     /       |      |      \      /   \    /           |
|        |     |   |    |  |____     \___/        |      |_______|    |_____|  |            |
|        |     |   |    |  |         /   \        |      |        \   |     |  |            |
 \_____   \___/    |___/   |____  __/     \__     |      |        |   |     |   \_____      |
'''


def time_inserter():
    now = time.time()
    print_time = time.ctime(now)
    return print_time
