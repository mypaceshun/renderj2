#!/usr/bin/env bash

cd /home/rpmbuilder/rpm
rpmbuild --define '_topdir /home/rpmbuilder/rpm' -ba SPECS/*.spec
