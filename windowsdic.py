helpCmd = {
    "description" : "MS DOS command interpreter\n",
    "/c" : "\tCarries out the command specified by string and then stops.\n",
    "/k" : "\tCarries out the command specified by string and continues.\n",
    "/s" : "\tModifies the treatment of string after /c or /k.\n",
    "/q" : "\tTurns the echo off.\n",
    "/d" : "\tDisables execution of AutoRun commands.\n",
    "/a" : "\tFormats internal command output to a pipe or a file as American National Standards Institute (ANSI).\n",
    "/u" : "\tFormats internal command output to a pipe or a file as Unicode.\n",
    #"/t:{<b><f> | <f>}" : "\tSets the background (b) and foreground (f) colors.\n",
        # <b> and <f> are single hex digits; use a regex maybe
    "/e:on" : "\tEnables command extensions.\n",
    "/e:off" : "\tDisables commands extensions.\n",
    "/f:on" : "\tEnables file and directory name completion.\n",
    "f:off" : "\tDisables file and directory name completion.\n",
    "v:on" : "\tEnables delayed environment variable expansion.\n",
    "v:off" : "\tDisables delayed environment variable expansion.\n",
    "/?" : "\tDisplays help at the command prompt.\n"
}

helpPowershell = {
    "description" : "POWERSHELL_DESC\n",
    "-ARG" : "\tARG_DESC\n"
}
helpCscript = {
    "description" : "CSCIRPT_DESC\n",
    "-ARG" : "\tARG_DESC\n"
}
helpWscript = {
    "description" : "WSCRIPT_DESC\n",
    "-ARG" : "\tARG_DESC\n"
}

helpWmiprvse = {
    "description" : "WMIPRVSE_DESC\n",
    "-ARG" : "\tARG_DESC\n"
}

helpWmic = {
    "description" : "WMIC_DESC\n",
    "-ARG" : "\tARG_DESC\n"
}

windowsIndex = {
    "cmd.exe" : helpCmd,
    "powershell.exe" : helpPowershell,
    "cscript.exe" : helpCscript,
    "wscript.exe" : helpWscript,
    "wmiprvse.exe" : helpWmiprvse,
    "wmic.exe" : helpWmic
}
