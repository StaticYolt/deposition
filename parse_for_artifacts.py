import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Parses Json and passes arguments to download-artifacts-sh')
    parser.add_argument("-o", "--organization", default="nsls2-collection-tiled",
                        help="The organization the repository is under")
    parser.add_argument("-a", "--action_run", help="The ID(s) of the workflow that was run in array format")
    parser.add_argument("-f", "--file_name", default="artifact_info",
                        help="jsonfile containg info about all artifacts created from some repository")
    args = parser.parse_args()
    print(args.organization)
    action_ids = args.action_run.split(' ')
    artifact_command = f'''
    gh api \\
            -H \"Accept: application/vnd.github+json\" \\
            -H \"X-GitHub-Api-Version: 2022-11-28\" \\
            /repos/nsls2-conda-envs/nsls2-collection-tiled/actions/artifacts >> {args.file_name}.json
    '''
    os.system(artifact_command)
    os.system(f"cat {args.file_name}.json")

if __name__ == "__main__":
    main()