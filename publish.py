#!/usr/bin/env python

"""Helps me to build, tag and push docker image."""

import shlex
import subprocess
import sys

stdout = subprocess.run(shlex.split('poetry version --no-ansi'), capture_output=True).stdout
image, tag = stdout.decode('utf-8').strip().split(' ')

print(f'Image: {image}')
print(f'Tag: {tag}')

if input('Continue? [y/N] ').strip().lower() not in ['y', 'yes']:
    sys.exit()

# Build
subprocess.run(shlex.split(f'docker image build -t {image} .'))

# Tag
subprocess.run(shlex.split(f'docker image tag {image} 2tunnels/{image}:latest'))
subprocess.run(shlex.split(f'docker image tag {image} 2tunnels/{image}:{tag}'))

# Push
subprocess.run(shlex.split(f'docker image push 2tunnels/{image}:latest'))
subprocess.run(shlex.split(f'docker image push 2tunnels/{image}:{tag}'))

print('Done! 🤘')
