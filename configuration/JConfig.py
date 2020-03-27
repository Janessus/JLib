import os


absCfgPath = "/home/janes/PycharmProjects/DownloadsFolderCleaner/config.ini"


def getValidSuffixes():
    cfg = open(absCfgPath, "r")
    lines = cfg.readlines()
    cfg.close()

    suffixStart = lines.index("[suffix_start]\n")
    suffixEnd = lines.index("[suffix_end]\n")

    return list(map(lambda x: x.strip(), lines[suffixStart + 1:suffixEnd]))


def dirExisting(path):
    if os.path.isdir(path):
        return True
    else:
        return False


def removeNewlineFromList(list):
    for i in range(list.count("\n")):
        list.remove("\n")

    result = []
    for j in list:
        result.append(j.strip())

    return result


def getConfigPaths():
    cfg = open(absCfgPath, "r")
    vars = cfg.readlines()
    cfg.close()

    start = vars.index("[paths_start]\n")
    end = vars.index("[paths_end]\n")

    return removeNewlineFromList(vars[start + 1:end])


def getConfigVars():
    cfg = open(absCfgPath, "r")
    vars = cfg.readlines()
    cfg.close()

    start = vars.index("[variables_start]\n")
    end = vars.index("[variables_end]\n")

    return removeNewlineFromList(vars[start + 1:end])


def getStrings():
        cfg = open(absCfgPath, "r")
        lines = cfg.readlines()
        cfg.close()

        start = lines.index("[strings_start]\n")
        end = lines.index("[strings_end]\n")

        return removeNewlineFromList(lines[start + 1:end])


def getString(name):
    cfg = open(absCfgPath, "r")
    lines = cfg.readlines()
    cfg.close()

    start = lines.index("[strings_start]\n")
    end = lines.index("[strings_end]\n")

    strings = getStrings()
    for s in strings:
        if not s.find(name) == -1:
            return str(s.split("=")[1][1:-1])


def getConfigVar(var):
    variables = getConfigVars()
    for i in variables:
        if not i.find(var) == -1:
            return float(i.split("=")[1])
