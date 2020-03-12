#!/usr/bin/env python3
# -*-coding:utf-8-*-
# linux-centos7版本下搭建pyenv环境的自动化脚本
import os
import re
import time

__Author__ = "van"


class build_pyenv():
    # 检查是否安装git，未安装就安装git
    def check_git(self):
        cmd = "rpm -qa|grep git-"
        values = (os.popen(cmd)).readlines()
        return_str = []
        for value in values:
            return_value = re.search(pattern="git", string=value)
            if return_value == None:
                pass
            else:
                return_str.append(return_value)
        if return_str == []:
            print("git未安装，正在尝试安装")
            time.sleep(1)
            cmd = "yum -y install git"
            os.system(cmd)
        else:
            print("git已安装，请执行下一步")
            print("当前git版本：")
            cmd = "git version"
            os.system(cmd)
            time.sleep(1)

    # 修改pyenv相关的环境变量并重新加载
    def pyenv_env(self):
        file = "/root/.bashrc"
        with open(file, "r") as f:
            values = f.readlines()
            return_str = []
            for value in values:
                return_value = re.search(pattern="pyenv init -", string=value)
                if return_value == None:
                    pass
                else:
                    return_str.append(return_value)
            if return_str == []:
                print("未配置环境变量，尝试配置环境变量")
                print("先设置pyenv的安装目录")
                with open(file, "a") as f:
                    f.write(
                        "\n" + "export PYENV_ROOT=/opt/pyenv")
                cmd = "source" + ' ' + file
                os.system(cmd)
                time.sleep(1)
                cmd = "curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash"
                os.system(cmd)
                time.sleep(1)
                with open(file, "a") as f:
                    f.write(
                        "\n" + "export PATH=\"/opt/pyenv/bin:$PATH\"" + "\n" + "eval \"$(pyenv init -)\"" + "\n" + "eval \"$(pyenv virtualenv-init -)\"")
                cmd = "source" + ' ' + file
                os.system(cmd)
                print("已完成配置pyenv的环境变量重新加载")
            else:
                print("已配置pyenv的环境变量")


if __name__ == "__main__":
    build_pyenv().check_git()
    build_pyenv().pyenv_env()
