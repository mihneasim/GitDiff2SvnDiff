import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: python %s git_diff_file svn_revision_number"
                 " [path_prefix_to_append]" % sys.argv[0])
    prefix = ""
    if len(sys.argv) == 4:
        prefix = sys.argv[3]
        if prefix[-1] != "/":
            prefix += "/"
    revision = int(sys.argv[2])
    git_diff = open(sys.argv[1], "r")
    new_file_flag = False
    for line in git_diff:
        if line.startswith("new file mode"):
            continue # skip
        if line.startswith("diff --git a/"):
            chunks = line.split(" ")
            sys.stdout.write("Index: ")
            sys.stdout.write(prefix + chunks[2][chunks[2].find("/")+1:] + "\n")
        elif line.startswith("index "):
            sys.stdout.write(("================================"
                              "===================================\n"))
        elif line.startswith("--- a/"):
            line = line[:-1]
            sys.stdout.write(line.replace(" a/", " "+prefix))
            sys.stdout.write("\t(revision %d)\n" % revision)
        elif line.startswith("+++ b/"):
            line = line[:-1].replace(" b/", " "+prefix)
            if new_file_flag:
                sys.stdout.write(line.replace("+++ ", "--- "))
                sys.stdout.write("\t(revision 0)\n")
                new_file_flag = False
            sys.stdout.write(line)
            sys.stdout.write("\t(working copy)\n")
        elif line.startswith("--- /dev/null"):
            new_file_flag = True
        else:
            sys.stdout.write(line)
    git_diff.close()
