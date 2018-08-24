#!/bin/bash
git config --global user.email "jprado@blablabla.com"
git config --global user.name "Jtan"
cd /tmp
git clone http://gituser:gitpassword@localhost:8888/demo.git
cd demo
git branch master
git checkout master
git commit -m "branch master" --allow-empty
git push --set-upstream origin master
git branch develop
git checkout develop
git commit -m "branch develop" --allow-empty
git push --set-upstream origin develop
