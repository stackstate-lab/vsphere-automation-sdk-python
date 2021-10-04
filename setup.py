#!/usr/bin/env python

import os

from setuptools import setup

setup(name='vsphere-automation-sdk',
      version='1.69.0-4fb7d48',
      description='VMware vSphere Automation SDK for Python',
      url='https://github.com/vmware/vsphere-automation-sdk-python',
      author='VMware, Inc.',
      license='MIT',
      package=['lib'],
      include_package_data=True,
      install_requires=[
          'lxml >= 4.3.0',
          'pyVmomi >= 6.7',
          'vapi-runtime == 2.25.0',
          'vapi-client-bindings == 3.6.0',
          'vapi-common-client == 2.25.0',
          'vmc-client-bindings == 1.52.0',
          'nsx-python-sdk == 3.1.2.1.1',
          'nsx-policy-python-sdk == 3.1.2.1.1',
          'nsx-vmc-policy-python-sdk == 3.1.2.1.1',
          'nsx-vmc-aws-integration-python-sdk == 3.1.2.1.1',
          'vmc-draas-client-bindings == 1.18.0',
      ]
      )
