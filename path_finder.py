import sys


def parse_lines(lines):

    # Retrieve origin node and destination
    path_details = lines[0]
    path_details = path_details.split(" ")
    path_origin = path_details[0]
    path_dest = path_details[1]

    total_path = ""
    # Check through all subsequent lines
    paths = lines[1:]

    return find_head(total_path, paths, path_origin, path_dest)
    
def find_head(total_path, paths, path_origin, path_dest):

    for path in paths:
        path = path[:-1]
        line_split = path.split(" : ")
        new_head = line_split[0]
        path_choices = line_split[1]
        nodes = path_choices.split(" ")
        if path_dest.strip() in nodes:
            if new_head == path_origin:
                return path_origin + path_dest + total_path
            else:
                return find_head(path_dest + total_path, paths, path_origin, new_head)
####################################
# Don't modify the functions below #
####################################

def parse_file(filename):
    try:
        with open(filename, "rU") as f:
            all_lines = f.readlines()
        return parse_lines(all_lines)
    except IOError:
        print "File not found."
        sys.exit()


def main():
    filename = "input_1.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    print parse_file(filename)


if __name__ == "__main__":
    main()
