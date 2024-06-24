import argparse
import os
import json
def main():
    parser = argparse.ArgumentParser(description='Parses Json and passes arguments to download-artifacts-sh')
    parser.add_argument("-o", "--organization", default="nsls2-collection-tiled",
                        help="The organization the repository is under")
    parser.add_argument("-a", "--action_run", help="The ID(s) of the workflow that was run in array format")
    parser.add_argument("-f", "--file_name", default="artifact_info",
                        help="jsonfile containg info about all artifacts created from some repository")
    args = parser.parse_args()
    action_ids = args.action_run.split(' ')
    artifact_command = f'''
    gh api \\
            -H \"Accept: application/vnd.github+json\" \\
            -H \"X-GitHub-Api-Version: 2022-11-28\" \\
            /repos/nsls2-conda-envs/nsls2-collection-tiled/actions/artifacts >> {args.file_name}.json
    '''
    os.system(artifact_command)
    f = open(f"{args.file_name}.json")
    data = json.load(f)
    for id in action_ids:
        for element in data['artifacts']:
            if element['workflow_run'].get('id') == int(id) and element['name'][-3:] != 'yml':
                print(element)

if __name__ == "__main__":
    main()