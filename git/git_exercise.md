### Git Exercise

---

#### Basic

1. What is the difference between git init and git clone?
   - git init initializes a directory
   - git clone copies existing git directory
2. What does the .git/ folder contain?
   - it contains all the version control, the file structure, the snapshots and tree structure for that git repository

3. Explain the difference between tracked, untracked, and staged files.
   - tracked files are files whose changes are being tracked by git. They are either in the last commit or have been added to the staging area
   - untracked files are files whose existance isn't recognized by git yet
   - staged files are files that have been tracked and by git and are ready to be commited to the snapshot
4. Why do we need to configure user\.name and user.email in Git?
   - so that any changes performed can be tracked to the specific user who made those changes

#### Branching & Merging

1. What is the purpose of using branches in Git?
   - so that we can separate different changes and have the ability to work on the same file across different local repositories without affecting the main codebase
2. How do you create a new branch and switch to it in one command?
   - `git checkout -b branchname`
3. What happens when two developers modify the same line in a file and try to merge their branches?
   - merge conflict happens where they will need to resolve the conflict to proceed with the merge
4. How can you view all existing branches in your repo?
   - `git branch` to view local branches
     - `git branch -r` view remote branches
     - `git branch -a` view local and remote branches

#### Collaboration

1. What is the difference between git fetch and git pull?
   - `git fetch` downloads remote for viewing purpose only without modifying local repository
   - `git pull` fetches and merges remote changes to local repository
2. How does a pull request (PR) on GitHub differ from a local git merge?
   - a pull request is a proposal to merge a change from a feature branch to a target branch with the approval of a reviewer.
   - `git merge` is a command that integrates change from a feature branch to target branch within a local repository
3. What is the purpose of tags in Git? When would you use one?
   - creates important static points in a repository's hisotry to mark milestones and releases.
4. Why is a .gitignore file important in projects?
   - specifies files and directories that should not be tracked and included in the repository. It eliminates unnecessary, generated and sensitive files from being commited

#### Undoing & Inspecting

1. How do you discard local changes in a file before committing?
   - `git rm filename `
2. What is the difference between git reset and git revert?
   - `git reset` moves the current branch pointer to a specified commit with `--soft`, `--hard` or `--mixed` options allowing the user to affect changes to the commit and the local changes.
     - `--soft` moves branch pointer to specified commit keeping changes as staged
     - `--hard` moves branch pointer to specified commit and discards local changes
     - `--mixed` moves branch pointer to specified commit keeping changes as unstaged
   - `git revert` undo changes introduced by a specified commit, by creating a new commit to reverse those changes
3. Which command shows the detailed changes introduced in a specific commit?
   - `git show <commit hash>`
