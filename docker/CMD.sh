#!/usr/bin/env bash

ls -alhd /rpm/**
cd /rpm
rpmbuild --define '_topdir /rpm' -bb SPECS/*.spec
