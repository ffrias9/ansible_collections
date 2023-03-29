# AWX Ansible Collection

This Ansible collection allows for easy interaction with an AWX server via Ansible playbooks.

## Installation
For install this Ansible collection, execute de following command:
```sh
ansible-galaxy collection install ffrias9.awx_jobs
```

## Requirements
The requirements are specified in [requeriments.txt](https://raw.githubusercontent.com/ffrias9/ansible_collections/main/ffrias9/awx_jobs/docs/requirements.txt)
It is important to have the python "requests" library installed:
```sh
python3 -m pip install requests
```

## Running
You need to create a playbook that may be briefly similar to this one
```yaml
---
- name: AWX jobs
  hosts: localhost
  become: true
  tasks:

    # For execute a job
    - name: Execute AWX job
      ffrias9.awx_jobs.job:
        url: "{{ url }}"
        api_v: "{{ api_v }}"
        user: "{{ user }}"
        password: "{{ passwd }}"
        job: "{{ j_id }}"
        credential: "{{ cred_id }}"

    # For execute a workflow
    - name: Executa a workflow template
      ffrias9.awx_jobs.workflow:
        url: "{{ url }}"
        api_v: "{{ api_v }}"
        user: "{{ user }}"
        password: "{{ passwd }}"
        job: "{{ w_id }}"
```

Variable file content:
```yaml
url: http://172.26.26.18
api_v: 2
user: admin
passwd: admin
j_id: 27
w_id: 23
cred_id: 9
```

## Authors
-  **Francisco José Frías Martín** - _Initial work_ - [ffrias9](https://github.com/ffrias9)

## License
This project is licensed under the MIT License.
