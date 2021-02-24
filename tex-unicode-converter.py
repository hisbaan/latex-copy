#!/usr/bin/env python3

# NOTE could do all of this or just find and replace
# with a lot of if statement.
# Find and replace would probably be a lot more efficient
def convert(tex: str) -> str:
    """Convert passed in TeX to unicode

    >>> convert('\\forall x \\in \\R')
    '∀x∈ℝ'
    """
    for i in range(len(tex)):
        if tex[i] == '\\':
            command, length = get_command(tex, i)
            # TODO do if operations here like:
            # if command == '\\forall': ... replace
    output = tex
    return output


def get_command(tex: str, index: int) -> (str, int):
    """Return the TeX command starting at the current index

    >>> get_command('01\\forall', 2)
    '\\forall'
    >>> get_command('01\\forall\\exists', 2)
    '\\forall'
    >>> get_command('01\\forall \\exists', 2)
    '\\forall'
    """
    command_so_far = ''

    for i in range(index, len(tex)):
        if tex[i] == ' ' or (tex[i] == '\\' and i > index + 1):
            return command_so_far

        command_so_far += tex[i]

    return command_so_far


# Option 2: as written at the start of the file
# FIXME find out how to replace \\
def convert_replace(tex: str) -> str:
    # quantifiers
    tex.replace('\\forall', '∀')
    tex.replace('\\exists', '∃')

    # comparison operators
    tex.replace('\\geq', '≥')
    tex.replace('\\leq', '≥')
    tex.replace('\\neq', '≠')
    tex.replace('\\equiv', '≡')
    tex.replace('\\nequiv', '≢')

    # blackboard letters
    # ℝ and the like

    # set notation
    # in, not in, contains, does not contain

    # greek letters
    # the entire alphabet rip... twice. Do all lowers, then all uppers
    return tex
