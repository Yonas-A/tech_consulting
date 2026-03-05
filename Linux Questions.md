## Linux Questions

#### Linux File System \& Navigation

1. List all files (including hidden) in long format with human-readable sizes, sorted by modification time (newest first). Which flags?

   `ls -ahlt` (a: all, h: human readable, l: long list format, t: sort by time )

2. Print the absolute path of your current directory and store it in an environment variable CUR_DIR. Which command or flags?

   `export CUR\_DIR=$(pwd)`

3. Change to your home directory using a shortcut, then in the same command change to the parent of your current directory. Which syntax?

   `cd ~/..`

4. Create the nested directory structure project/{src,bin,docs} in one command. Which flag allows this?

   `mkdir -p project/{src,bin,docs}` (no spaces allowed)

5. First run echo "hello" > file.txt and mkdir archive, then move file.txt into archive/ renaming it to file.bak, prompting before overwrite. Which flag?

   `mv -i file.txt archive/file.bak`

6. First mkdir -p data and echo a > data/a.txt and echo b > data/b.txt, then copy the entire data/ directory to backup/, preserving timestamps and permissions. Which flags?

   `cp -rp data/ backup/` ( r: remove directories and their contents recursively, p: preserve timestamp and permission)

7. First mkdir -p old_logs and echo log1 > old_logs/log1.txt, then remove the non-empty directory old_logs/ without any prompts. Which flags?

   `rm -r old\_logs/`

8. First create an empty file notes.md, then update its modification time to January 1 2022 at 12 PM. Which flag?

   ```sh
   touch notes.md
   touch -m -d '2022-01-01 12:00:00' notes.md
   # m: modify, d: date, touch creates if it doesn't exist
   ```

9. Clear your terminal screen. What keyboard shortcut achieves the same effect?

   `clear` or `ctlr + l`

10. Temporarily set the environment variable EDITOR=vim in your current shell. Which command or syntax ensures it's inherited by child processes?

`export EDITOR=vim`

11. What command shows you the directory hierarchy from / down to your current directory?
    `pwd`

---

#### Permissions & Ownership

1. Set permissions on script.sh so owner has rwx, group has r-x, others none, first using numeric mode, then symbolic mode. Which syntaxes?

   `chmod 750 script.sh` r: 4, w: 2, x: 1 (numeric values)
   `chmod u+rwx,g+rx script.sh` u: user, g: group, o: other, a: all

2. Change owner to alice and group to staff for /var/www/html recursively. Which flag?

   `chown -R alice:staff /var/www/html` R: recursive, new owner:new group

3. Create a symbolic link latest.log pointing to /var/log/syslog. Which flag, and how does a symbolic link differ from a hard link?

   ```shell
   ln -s /var/log/syslog latest.log   # s: flag for symbolic link

   ln /var/log/syslog latest.org   # hard link
   ```

   **Symbolic link**: creates a link that points to the pathname.
   - If the symbolic link file is deleted, the original data remains.

   - If the original file is moved or deleted, the symbolic link won’t work.

   - A soft link can refer to a file on a different file system

   **Hard Link**: hard link points to the physical data on disk.
   - If the original file is deleted, the file data can still be accessed through other hard links.
   - If the original file is moved, hard links still work

4. You have a file owned by root:root at /opt/data.txt. Change its owner to you and group to users, without affecting anything else. Which command?
   `chown yonas:user /opt/data.txt`

---

#### Text Processing, Redirection & Piping

1. First echo A > a.txt, echo B > b.txt, and echo C > c.txt, then concatenate a.txt, b.txt, and c.txt into all.txt and display non-printing characters. Which flags?

   ```shell
   echo A > a.txt
   echo B > b.txt
   echo C > c.txt
   cat a.txt b.txt c.txt > all.txt
   cat -v all.txt # -v: show non printing
   ```

2. Print the literal string Hello, \$USER! (without expanding $USER), then interpret \n as a newline. Which flags?

   ```shell
   echo -e "Hello, \$USER\!\n"
   # escape ! with backslash and use double quotes to prevent shell from expanding $USER
   # or
   echo -e 'hello, \$USER!\n'
   # -e: flag enables the interpretation of backslash escapes line \n
   ```

3. Open a large log file with line numbers displayed using less. Which flag, and what key do you press to search forward for “error”?

   ```shell
   less -N sample.log # -N: line numbers

   # less: is a powerful utility used to view the contents of a text file or command output one screen at a time
   ```

   - press `/` and type error and enter to search for the term `error`

4. Display the manual page for grep and jump directly to the “OPTIONS” section. How do you quit?

   ```shell
   man --pager='less +/OPTIONS' grep
   # jumps to Options section within grep

   # q to quit
   ```

5. First echo -e "a\nb\nc" > A.txt and echo -e "b\nc\nd" > B.txt, then list only the lines common to A.txt and B.txt. Which flag hides lines unique to the first file?

   ```shell
   echo -e "a\nb\nc" > A.txt
   echo -e "b\nc\nd" > B.txt

   comm -12 A.txt B.txt # -1: unique to first file,

   comm -12 <(sort A.txt) <(sort B.txt) # if a and b not sorted
   ```

   **comm**: a utility used to compare two sorted files line by line, producing three columns of output: lines unique to the first file, lines unique to the second file, and lines common to both

6. First echo -e "10\n2\n30\n4" > numbers.txt, then sort the numbers in numeric order. Which flag? How do you reverse the sort?

   ```shell
   echo -e "10\n2\n30\n4" > numbers.txt
   sort -n numbers.txt  # -n: sort according to string numerical value
   sort -nr numbers.txt # r: sort in reverse
   sort -nr -o numbers.txt numbers.txt # o: save to same file, > empties file before sort
   ```

7. Count the number of unique IP addresses in /var/log/nginx/access.log. Sketch a one-liner using pipes.

8. Redirect both stdout and stderr of rsync into sync.log, appending rather than overwriting. How?

---

#### Compression & Archiving

1. First mkdir logs and echo test > logs/a.log and echo err > logs/b.log, then create a gzipped archive logs.tar.gz of logs/ and extract it into restore/. Which flags?

   ```shell
   mkdir logs
   echo test > logs/a.log
   echo err > logs/b.log
   ```

2. Extract archive.zip into dest/ without any prompts. Which flag? How do you list its contents without extracting?
   `unzip -o -d dest/ archive.zip`

3. First touch a.png b.png c.png, then create a zip archive images.zip containing all .png files and prompt for a password. Which flag?

4. Create a tar.bz2 archive of /etc using bzip2 compression. Which flag?
