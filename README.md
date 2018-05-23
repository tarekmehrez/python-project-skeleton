# Python Project Skeleton

A python project skeleton, to be used as an example to the [bones](https://github.com/marghidanu/bones) project


## Build status

[![Build Status](https://travis-ci.org/tarekmehrez/python-project-skeleton.svg?branch=master)](https://travis-ci.org/tarekmehrez/python-project-skeleton)


## Get Started

```bash
vagrant up
sudo su -
cd /example_project
python setup.py develop
# make sure imports are working in the example script and the 
# debug message is printed
./bin/example_script
```

## Notes

- This assumes you will be using Vagrant for your development environment, you can still use ```conda``` or ```virtualenv```
- The used python distribution in the vagrant box is miniconda
- Tests dir structures just follows the ```example_project``` (src) structure
- Changes in modules (names or structure) should be reflected in ```setup.py``` 
