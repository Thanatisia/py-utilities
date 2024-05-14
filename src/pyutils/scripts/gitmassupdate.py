#!python
"""
Enter all git repositories in the current working directory and pull the latest changes
"""
import os
import sys
from pyutils.libraries.subprocess import sync_exec, PIPE, DEVNULL
from pyutils.libraries.treelib import tree_traversal, path_separator

def network_check():
    """
    Check if host system's internet is working
    """
    # Initialize Variables
    rc:int = -1
    stdout = ""
    stderr = ""
    cmd_list = ["ping", "-c", "5", "8.8.8.8"]

    # Open subprocess to check the host's network connectivity
    stdout, stderr, rc = sync_exec(cmd_list, stdout=DEVNULL, stderr=DEVNULL)

    # Return result
    return [stdout, stderr, rc]

def find_all_git_repositories(find_dir=".", type="d", name=".git"):
    """
    Get all directories with the ".git" directory within
    """
    # Initialize Variables
    find_git_dirs = ["find", find_dir, "-type", "d", "-name", ".git"] # TODO: Replace the use of "find" by using os.walk to walk and traverse the entire tree to search
    cut_git_dir_paths = ["cut", "-d", '/', "-f2"]
    all_git_dirs = []

    # Open subprocess to find all directories with the ".git" directory
    stdout, stderr, rc = sync_exec(find_git_dirs, stdout=PIPE, stderr=PIPE)

    # Split subprocess result by the newline separator ("\n") into a list
    stdout_spl = stdout.split("\n")

    # Iterate through list and
    # Filter the results and split by the path delimiter "/"
    for i in range(len(stdout_spl)):
        # Get current line
        curr_line = stdout_spl[i]

        # Split current paths into elements and obtain the name
        dir_name = path_separator.join(curr_line.split(path_separator)[:-1])

        # Append git directory name into list
        all_git_dirs.append(dir_name)

    # Return
    return all_git_dirs

def get_git_branch():
    """
    Get current branch
    """
    # Initialize Variables
    get_git_branches = ["git", "branch"]
    selected_git_branch = ""

    # Open subprocess to get git branches
    all_branches, stderr, rc = sync_exec(get_git_branches, stdout=PIPE, stderr=PIPE)

    # Split all branches into a list
    all_branches_spl = all_branches.split("\n")

    # Find selected git branch
    for i in range(len(all_branches_spl)):
        # Get current git branch
        curr_git_branch = all_branches_spl[i]

        # Check if branch is selected ("*" delimiter)
        if curr_git_branch.startswith("*"):
            # Remove the delimiter from the string
            selected_git_branch = curr_git_branch.split("*")[1].strip()

            # Completed; Break the iteration
            break

    # Return
    return selected_git_branch

def pull_latest_changes(curr_git_branch):
    """
    Pull the latest changes in this repository's selected branch
    """
    # Initialize Variables
    git_pull = ["git", "pull", "origin", curr_git_branch]

    # Open subprocess pipe to pull the latest changes
    stdout, stderr, rc = sync_exec(git_pull)

    # Return
    return [stdout, stderr, rc]

def main():
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    # Initialize Variables
    top_level_root_dir = "."

    # Switch case obtain arguments based on number of arguments provided
    match argc:
        case 1:
            top_level_root_dir = argv[0]

    # Check if network is available
    stdout, stderr, network_available = network_check()
    print("[i] Network availability: {}".format(network_available))
    if (network_available == 0):
        # Success
        print("{}".format("[+] Host system's internet is working properly."))

        # Get all directories with the ".git" directory within
        all_dirs = find_all_git_repositories(top_level_root_dir)

        # Enter all directories and pull latest changes
        for i in range(len(all_dirs)):
            # Get current directory
            curr_dir = all_dirs[i]

            # Null Validation: Check if current directory is empty
            if len(curr_dir) > 0:
                # Get current working directory
                cwd = os.getcwd()

                # Change directory into git directory
                os.chdir(curr_dir)

                # Get current branch
                curr_git_branch = get_git_branch()

                print("[i] Pulling branch {} of repository {}".format(curr_git_branch, curr_dir))

                # Pull latest change
                stdout, stderr, rc = pull_latest_changes(curr_git_branch)

                if rc == 0:
                    print("[+] Updated {} to the latest version".format(curr_dir))
                else:
                    print("[-] Error updating {} to the latest version".format(curr_dir))

                # Move back 1 directory
                os.chdir(cwd)

                print("")
    else:
        print("{}".format("[X] Host system's internet is not working."))

if __name__ == "__main__":
    main()


