dirdup
======

A duplicate finder across multiple systems. The project is incomplete. Help
and patches are welcome.


How to use
==========

The dirdup workflow is:

* Add one or more storages (declare them for dirdup management)
* Index them (take the size, mtime and md5sum hash of each file under it)
* Find duplicates (works on the index, not the real files)
* You do your work: either clean the files or accept the duplicates
* Tell dirdup of what you did.
* Refresh the indexes
* Repeat from "Find duplicates" until done

Example
-------

Scenario: You have a copy of some home files at work and viceversa. You
modified them in either place and now you lost track of the current state of
your data. You need to make some sense of it.

Please notice: do not confuse *home*, the place where you live (or the PC you
have *at home*), with the *home* directory *at home* or *at work*. To
distinguish both in this example, let's use `home-pc` for the hostname and
`homedir` to alias the directory for your user under `/home`.

1. You create an empty directory which will be your dirdup "session". Using a
   USB flash memory is the best way to exemplify this. Let's say /USB is the
   path to your USB thumb drive.

  ```
  you@home-pc:~$ cd /USB
  you@home-pc:/USB$ mkdir dirdup-session
  you@home-pc:/USB$ cd dirdup-session
  you@home-pc:/USB/dirdup-session$
  ```

1. At home add your home directory and index it. Indexing will take quite some
   time because it takes the size, mtime and MD5 hash of each file. Let the
   indexing run overnight.

   ```
   you@home-pc:/USB/dirdup-session$ dirdup-add homedir /home/you
   you@home-pc:/USB/dirdup-session$ dirdup-index homedir
   ```

1. At work, do the same. Remember you have a *home* directory at work too.
   We can call both *homedir* because dirdup uses different namespaces for
   each device. Dirdup will detect what host are you in and use that
   namespace.

   ```
   you@work-pc:/USB/dirdup-session$ dirdup-add homedir /home/you
   you@work-pc:/USB/dirdup-session$ dirdup-index homedir
   ```

   You are using your USB which you are carrying it with you at home and work,
   so you will have both declarations now:

   ```
   you@work-pc:/USB/dirdup-session$ find accesses -type f
   accesses/home-pc/home-pc/homedir
   accesses/work-pc/work-pc/homedir
   you@work-pc:/USB/dirdup-session$ cat accesses/home-pc/home-pc/homedir
   file:/home/you
   ```

1. Now you can ask dirdup to find duplicates wherever you have the indexes.
   Dirdup will be able to find duplicate files or directories you have spanned
   across *home-pc* and *work-pc*. In other words, if you have the same file
   in both computers, dirdup will be able to find it.
   
   ```
   # This section is under construction; dirdup-finddup is still being developed.
   you@work-pc:/USR/dirdup-session$ dirdup-finddup work:homedir home:homedir
   ```

# Please stay tuned as dirdup continues being developed

