import argparse


def main():
    parser = argparse.ArgumentParser(description='Parses Json and passes arguments to download-artifacts-sh')
    parser.add_argument("-o", "--organization", default="nsls2-collection-tiled", help="The organization the "                                                                      "repository is under")
    parser.add_argument("-a", "action_run", help="The ID(s) of the workflow that was run in array format")
    args = parser.parse_args()
    print(args.organization)
    print(args.action_run.split(' '))

if __name__ == "__main__":
    main()