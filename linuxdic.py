manSh = {
    "description" : "A POSIX-compliant command interpreter.\n"
                    "-- historically the Bourne SHell, now often symlinked to /bin/dash.\n",
    "-ARG" : "\tARG_DESC\n"
}

manAsh = {
    "description" : "The Almquist SHell -- command interpreter. POSIX compliant. \n",
    "-ARG" : "\tARG_DESC\n"
}

manDash = {
    "description" : "Debian Almquist SHell -- command interpreter. POSIX compliant \n"
                    "-- much faster than bash, but not good for interactive use. The default system shell.\n",
    "-ARG" : "\tARG_DESC\n"
}

manBash = {
    "description" : "Bourne Again Shell\n",
    "-ARG" : "\tARG_DESC\n"
}

manZsh = {
    "description" : "Z SHell -- next generation bash\n",
    "-ARG" : "\tARG_DESC\n"
}

manFish = {
    "description" : "Friendly Interactive Shell -- more user-friendly than bash or zsh!\n",
    "-ARG" : "\tARG_DESC\n"
}


boolAnd = {
    "description" : "Boolean AND operator.\n"
}

stdIn = {
    "description" : "A single hyphen - represents standard input, or stdin.\n"
}


linuxIndex = {
    "sh" : manSh,
    "ash" : manAsh,
    "dash" : manDash,
    "bash" : manBash,
    "zsh" : manZsh,
    "fish" : manFish,

    "&&" : boolAnd,
    "-" : stdIn
}
