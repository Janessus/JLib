import os.path

###########################################################################
#                          -- Config Section --                           #
###########################################################################


def getConfigVars():
    cfg = open("config.ini", "r")
    vars = cfg.readlines()

    start = vars.index("[variables_start]\n")
    end = vars.index("[variables_end]\n")

    return removeNewlineFromList(vars[start + 1:end])


###########################################################################


def getConfigPaths():
    cfg = open("config.ini", "r")
    vars = cfg.readlines()

    start = vars.index("[paths_start]\n")
    end = vars.index("[paths_end]\n")

    return removeNewlineFromList(vars[start + 1:end])


###########################################################################


def getConfigVar(var):
    variables = getConfigVars()
    for i in variables:
        if not i.find(var) == -1:
            return float(i.split("=")[1])
