        sys.exit("Usage: python %s svn_revision_number"
                 " [path_prefix_to_append]" % argv[0])
    new_file_flag = False
        if line.startswith("new file mode"):
            continue # skip
                              "===================================\n"))
            line = line[:-1].replace(" b/", " "+prefix)
            if new_file_flag:
                sys.stdout.write(line.replace("+++ ", "--- "))
                sys.stdout.write("\t(revision 0)\n")
                new_file_flag = False
            sys.stdout.write(line)
        elif line.startswith("--- /dev/null"):
            new_file_flag = True