#!/usr/bin/python


DOCUMENTATION = '''
---
module: job

Description: This ansible plugin allows you to run AWX jobs from a playbook

Options:
  url:
    description:vAWX server url
    required: true
  api_v:
    description: Here you must indicate the version of the api
    required: true
  user:
    description: Username from AWX server
    required: true
  password:
    description: AWX user password
    required: true
  job:
    description: Id of the job you want to run
    required: true
  credentials:
    description: Job credentials id
    required: true
'''
EXAMPLES = '''
ffrias9.awx_jobs.job:
  url: http://172.26.26.28
  api_v: 2
  user: admin
  password: admin
  job: 27
  credential: 9
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module_args = dict(
            url=dict(required=True, type='str'),
            api_v=dict(required=True, type='str'),
            user=dict(required=True, type='str'),
            password=dict(required=True, type='str'),
            job=dict(required=True, type='str'),
            credential=dict(required=True, type='str')
            )

    module = AnsibleModule(
            argument_spec=module_args,
            supports_check_mode=False
            )

    auth = (module.params['user'], module.params['password'])
    url = module.params['url'] + "/api/v" + module.params['api_v'] + "/job_templates/" + module.params['job'] + "/launch/"
    credential = module.params['credential']
    payload = {"extra_vars": {}, "credentials": [credential]}

    try:
        import requests
    except:
        module.fail_json(msg='Python library "requests" not found. Please, install it manually.')

    result = requests.post(url, auth=auth, json=payload)

    if result.status_code == 201:
        result = dict(
            changed=True,
            Response='Success launch job ' + module.params['job']
            )
        module.exit_json(**result)
    elif result.status_code == 401:
        module.fail_json(msg='Error401 - Incorrect login credentials')
    elif result.status_code == 400:
        module.fail_json(msg='Error400 - Invalid request')
    elif result.status_code == 404:
        module.fail_json(msg='Error404 - Incorrect job id or api version')
    else:
        module.fail_json(msg=f'Error launch job {result}')


if __name__ == '__main__':
    main()
