logrotate
=========

Installs logrotate and provides an easy way to setup additional logrotate scripts by specifying a list of directives.

Requirements
------------

None

Role Variables
--------------

**logrotate_scripts**: A list of logrotate scripts and the directives to use for the rotation.

* name - The name of the script that goes into /etc/logrotate.d/ (required)
* rules - A list of rule to specify log rotation (required)
* comment - The comment for a rule block
* paths - A list of paths to point logrotate to for the log rotation (required)
* options - List of directives for logrotate, view the logrotate man page for specifics
* scripts - Dict of scripts for logrotate (see Example below)


Dependencies
------------

None

Example Playbook
----------------
```
- hosts: all
  vars:
    logrotate_scripts:
      - name: "nginx-paths"
        rules:
          - paths:
              - /var/log/nginx/path1.log
              - /var/log/nginx/path2.log
              - /var/log/nginx/path3.log
            options:
              - daily
              - rotate 7
            scripts:
              postrotate: "echo test"
      - name: "nginx-rules"
        rules:
          - comment: daily
            paths:
              - /var/log/nginx/rule1.log
            options:
              - daily
          - comment: weekly
            paths:
              - /var/log/nginx/rule2.log
            options:
              - weekly

  roles:
    - role: ivoamorim.logrotate
```

License
-------

BSD
