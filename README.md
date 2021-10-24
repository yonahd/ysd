[![python version](https://img.shields.io/badge/python-3.9-blue)](https://img.shields.io/badge/python-3.9-blue)
# Yaml Schema Definition

### Overview: 
Helps keep yaml file schemas aligned

##### Running the validator:
```
python yaml-validator/main.py -v yamls/example-values.yaml -r yamls/example-rules.yaml 
```

#### Example rule file:
```yaml
required: // field must exist and type must match
  env: str
  enabled: bool
  replicas: int
  db:
    name: str
    test1:
      user: str
optional: // if field exists type must match
  disk: str
  metrics: bool 
```


#### Example yaml file (helm values file):
```yaml
network:
  service:
    port: 8060
enabled: true
image:
  app: my-app:build
replicas: 1
env: dev
disk: local
db:
  name: "my_db"
  app:
    user:
      vault:
        enabled: "true"
  test1:
    user: "user2"
    password: "abc"
resources:
  requests:
    memory: "300M"
  limits:
    memory: "400M"
```

Example output:
```buildoutcfg
---Checking required fields---
SUCCESS: Rule for field env exists
SUCCESS: Rule for field enabled exists
SUCCESS: Rule for field replicas exists
SUCCESS: Rule for field db.name exists
SUCCESS: Rule for field db.test1.user exists
---Checking optional fields---
SUCCESS: Rule for field disk exists
Field metrics does not exist -- optional
```

Enforcing yaml structure - fields cannot exist if it doesn't have a rule:
```commandline
# add enforce flag -e
python yaml-validator/main.py -v yamls/example-values.yaml -r yamls/example-rules.yaml -e
```
Example output:
```buildoutcfg
---Checking fields exist---
FAILED: Rule for field network doesn't exist
SUCCESS: Rule for field enabled exists
FAILED: Rule for field image doesn't exist
SUCCESS: Rule for field replicas exists
SUCCESS: Rule for field env exists
SUCCESS: Rule for field disk exists
SUCCESS: Rule for field db.name exists
FAILED: Rule for field db.app doesn't exist
SUCCESS: Rule for field db.test1.user exists
FAILED: Rule for field db.test1.password doesn't exist
FAILED: Rule for field resources doesn't exist
```

