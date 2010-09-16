GitDiff2SvnDiff v0.1
====================

This is a small python script that converts a given git diff file into a
svn diff file for the same project.

Usage
=====

Input arguments::
  path_to_git_diff_file svn_revision_number [prefix_to_append]

Where::
  * svn_revision - revision number on svn for older version of the files
  * prefix_to_append - optional, you may choose to append a path to each 
 file path

Limitations
===========

It shouldn't work with diffs containing file creations/deletions.
This should be the next version.
