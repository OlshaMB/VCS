"""
Tools for print help text in commands
Functions:
    - VCS global help text
    - Init command  help text
    - Add command help text
    - Commit command help text
    - Reset command help text
    - Rollback command help text
    - Checkout command help text
    - Branch command help text
    - Merge command help text

    - Ignore command help text
    - Status command help text
    - Log command help text
    - Check command help text
"""

# Vars with help text
vcs_text = """
// Commit management
vcs init - Initial command
vcs add - Command to add files in tracked list
vcs commit - Command to commit changes
vcs reset - Command to reset last commit

// Branches management
vcs rollback - Command to rollback to last commit
vcs checkout - Switch branches
vcs branch - Command to modify branches
vcs merge - Command to merge branches

// Auxiliary commands
vcs ignore - Command to modify ignore file
vcs log - Command to print info about commits

vcs status - Command to print current vcs status
vcs check - Command to check vcs state

vcs -h | --help - This help
"""

init_text = """
vcs init
    -b "<branch name>" - Create first branch with custom name
    -q | --quiet - Quiet mode. Only errors and warning
    -h | --help- This help
"""

add_text = """
vcs add <file_name> | . | -A
    . = -A - Add all files in current directory to tracked files list
vcs add
    -l - Print all tracked files list
    -c | --clean - Clear tracked files list
    -v | --verbose - Be verbose
    -f | --force - Disregard .ignore file
    -h | --help - This help
"""

commit_text = """
vcs commit -t "<Your commit text>" - Create commit with text
vcs commit -t "<Your commit text>" --hard - Create commit, and remove all previous commits
vcs commit -h | --help - This help
"""

reset_text = """
vcs reset - Reset last commit
vcs reset -v | --verbose - Reset last commit in verbose mode
vcs reset -h | --help - This help
"""

rollback_text = """
vcs rollback - Rollback to last commit
vcs rollback -v | --verbose - Rollback to last commit in verbose mode
vcs reset -h | --help - This help
"""

checkout_text = """
vcs checkout <branch_name> - Switch branch
vcs checkout -b <branch_name> - Create branch and switch
"""

branch_text = """
vcs branch - Print list of branches
vcs branch -l | --list - Print list of branches
vcs branch -n | --new <branch_name> - Create new branch
vcs branch -d | --delete <branch_name> - Remove branch
"""

merge_text = """
vcs merge <branch_name> - Merge branch_name with current branch in rebase mode
"""

ignore_text = """
vcs ignore 
    -n | --new - Create .ignore file with base ignores
    -t | --template - Create .ignore file with base ignores and template
vcs ignore -tl | --template-list - Print list  of templates
vcs ignore -l | --list - Get list of ignores
vcs ignore -h | --help - This help
"""

status_text = """
vcs status - Base command to print status
vcs status -h | --help - This help
"""

log_text = """
vcs log - Print last commit log
    -a | --all - Print all commits
    -v | --verbose - Be verbose
vcs log -h | --help - This help
"""

check_text = """
vcs check
    -c | --commits - Check commits chain in current branch
    -b | --branches - Check is branches valid
vcs check -h | --help - This help
"""
