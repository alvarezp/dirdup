dirdup
======

A duplicate finder across multiple systems. The project is incomplete. Help
and patches are welcome.

At this moment, version 0.0 has been released. This is just to prove the
concept and let myself start working on my personal folders.

The following 0.0.x versions should be more arbitrary changes for concept
changes, etc. Commands and output may (and will) break.

Proper development should start now to get to version 0.1 until we get to
version 1.0.

What's next:
* Improve the index format to speed up its load time and make it friendlier
  for Dropbox storage. Currently, each change implies the reupload of the
  whole for a storage.
* Fix the command-line API. Currently, command names and options were taken
  on the fly, so, it's headed to being a mess.
* Implement other possible uses, like locating files based on name and size.
* Fix terminology. Use the words "storage" and "index" as opposed to previous
  attempts like "seed" and fix term-consistency issues.
* Rename the whole project and repo. Dirdup is an inconvenient name.


How to use
==========

The dirdup workflow is:

1. Use `dirdup-add` to add (declare) one or more storages. Do this under
   each system where you have a storage.
1. Use `dirdup-refresh` to index each of them. Thsi will take the size, mtime
   and MD5 hash of each file under it.
1. Use `dirdup-find` to find duplicates and locate files.
1. Erase some files, move them... Do this manually.
1. Refresh the indexes with `dirdup-refresh` to let dirdup know the new state.
1. Repeat from step 3.

Example
-------

Scenario: You have a copy of some home files at work and viceversa. You
modified them in either place and now you lost track of the current state of
your data. You need to make some sense of it.

Please notice: this example uses *home* with two meanings: the place where you
live (like the PC you have *at home*), and the *home* directory, which may be
*at home* or *at work*. To distinguish both in this example, let's use
`home-pc` for the hostname and `homedir` to alias the directory for your user
under `/home`.

1. You create an empty directory which will be your dirdup "session". Using a
   USB flash memory is the best way to exemplify this. Let's say /USB is the
   path to your USB thumb drive.

  ```
  you@home-pc:~$ **cd /USB**
  you@home-pc:/USB$ **mkdir dirdup-session**
  you@home-pc:/USB$ **cd dirdup-session**
  you@home-pc:/USB/dirdup-session$
  ```

1. At home add your home directory and index it. Indexing will take quite some
   time because it takes the size, mtime and MD5 hash of each file. Let the
   indexing run overnight.

   ```
   you@home-pc:/USB/dirdup-session$ **dirdup-add homedir /home/you**
   you@home-pc:/USB/dirdup-session$ **dirdup-refresh homedir**
   ```

   Don't worry if you cancel *dirdup-refresh*. The half-finished index is kept
   on disk. It will not be generally used, but *dirdup-refresh* will use
   

1. At work, do the same. Remember you have a *home* directory at work too.
   We can call both *homedir* because dirdup uses different namespaces for
   each device. Dirdup will detect what host are you in and use that
   namespace.

   ```
   you@work-pc:/USB/dirdup-session$ **dirdup-add homedir /home/you**
   you@work-pc:/USB/dirdup-session$ **dirdup-refresh homedir**
   ```

   You are using your USB which you are carrying it with you at home and work,
   so you will have both declarations now. Verify it with:

   ```
   you@work-pc:/USB/dirdup-session$ **find accesses -type f**
   accesses/home-pc/home-pc/homedir
   accesses/work-pc/work-pc/homedir
   you@work-pc:/USB/dirdup-session$ **cat accesses/home-pc/home-pc/homedir**
   file:/home/you
   ```

1. With these indexes, if you have the same file in both computers, dirdup will
   be able to detect it.
   
   ```
   # This section is under construction; dirdup-find is still being developed.
   you@work-pc:/USR/dirdup-session$ **dirdup-find --type ff**
   ```

# Please stay tuned as dirdup continues being developed

