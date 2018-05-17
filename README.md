# Python Project Skeleton

A python project skeleton, to be used as an example to the [bones](https://github.com/marghidanu/bones) project


## Build status

[![Build Status](https://travis-ci.org/marghidanu/bones.svg?branch=master)](https://travis-ci.org/tarekmehrez/python-project-skeleton)


## Get Started

```bash
vagrant up
sudo su -
cd /example_project
python setup.py develop
```

## Notes

- This assumes you will be using Vagrant for your development environment, you can still use ```conda``` or ```virtualenv```
- The used python distribution in the vagrant box is miniconda
- Tests dir structures just follows the ```example_project``` (src) structure
- Changes in modules (names or structure) should be reflected in ```setup.py``` 
