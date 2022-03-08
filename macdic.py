manSh = {
    "description" : "A POSIX-compliant command interpreter."
                    "-- historically, the Bourne SHell, now often symlinked to /bin/dash.\n",
    "-ARG" : "\tARG_DESC\n"
}

manAsh = {
    "description" : "The Almquist SHell -- command interpreter. POSIX compliant. \n",
    "-ARG" : "\tARG_DESC\n"
}

manDash = {
    "description" : "Debian Almquist SHell -- command interpreter. Posix compliant."
                    "-- much faster than bash, but not good for interactive use. The default system shell.\n",
    "-ARG" : "\tARG_DESC\n"
}

manBash = {
    "description" : "Bourne Again SHell.\n",
    "-ARG" : "\tARG_DESC\n"
}

manZsh = {
    "description" : "Z SHell -- next generation bash.\n",
    "-c" : "Take the first argument as a command to execute\n"
}

manFish = {
    "description" : "Friendly Interactive Shell -- more user-friendly than bash or zsh!\n",
    "-ARG" : "\tARG_DESC\n"
}


macIndex = {
    "sh" : manSh,
    "dash" : manDash,
    "bash" : manBash,
    "zsh" : manZsh,
    "fish" : manFish,
}
