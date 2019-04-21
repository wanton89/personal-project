#!/usr/bin/python

from ansible.module_utils.basic import *
from git import Repo

def main():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        commit_id=dict(type='str', required=True),
        repo=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=module_args)
    if len(module.params['commit_id']) < 7:
        module.fail_json(msg=('Invalid commit id %s', module.params['commit_id']))

    working_directory = Repo(module.params['repo'])
    base_commit = str(working_directory.commit(module.params['commit_id']).parents[0])

    #commits = working_directory.iter_commits(base_commit + '..HEAD')
    working_directory.git.revert(base_commit + '..HEAD',
        no_edit = True,
        no_commit= True)
    module.exit_json(changed=False, meta="commits")


if __name__ == '__main__':
    main()
