GitDiff2SvnDiff v0.2
====================

This is a small python script that converts a given git diff file into an
svn diff file for the same project.

Usage
=====

Input arguments::
  python gitdiff2svndiff.py svn_revision_number [prefix_to_append]

Where::
  * svn_revision - revision number on svn for older version of the files
  * prefix_to_append - optional, you may choose to append a path to each
    file path

Shortcut for last commit ("git show"-diff to svn-diff)::
  ./gitsvnshow
OBS!: Only works with git-svn repos and if your HEAD^ commit is already on svn.

Limitations
===========

It shouldn't work with diffs containing file deletions. Changing paths for
files is untested. This should be the next version.

