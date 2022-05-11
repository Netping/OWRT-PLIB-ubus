#!/usr/bin/python3
import os
import platform
import pkg_resources

# Информация о модулях и библиотеках которые должны быть установлены в зависимости от архитектуры устр-ва
arch_info = {
    'x86_64': {
        'modules_info': {},
        'modules_files_dir': '',
        'libs_info': ['ubus.cpython-37.so'],
        'libs_files_dir': '/usr/lib/python3.7/lib-dynload/',
    },
    'mipsel_24kc': {
        'modules_info': {},
        'modules_files_dir': '',
        'libs_info': ['ubus.cpython-36.so'],
        'libs_files_dir': '/usr/lib/python3.6/lib-dynload/',
    },
    'i386_pentium4': {
        'modules_info': {},
        'modules_files_dir': '',
        'libs_info': ['ubus.cpython-37.so'],
        'libs_files_dir': '/usr/lib/python3.7/lib-dynload/',
    },
    'arm_cortex-a7+neon-vfpv4': {
        'modules_info': {},
        'modules_files_dir': '',
        'libs_info': ['ubus.cpython-37.so'],
        'libs_files_dir': '/usr/lib/python3.7/lib-dynload/',
    },
}

def get_arch():
    arch = platform.uname().machine
    return arch

def test_module_lib_exists():
    print("\n")
    arch_section = arch_info[get_arch()]
    for module in arch_section['modules_info']:
        try:
            dist = pkg_resources.get_distribution(module)
            modname, modversion, modlocation = dist.key, dist.version, dist.location
            print(f"{module}: {modname} {modversion} {modlocation}")
            assert module == modname
            assert arch_section['modules_info'][module] == modversion
            assert arch_section['modules_files_dir'] == modlocation
        except:
            print(f"{module} did not pass the test")
            assert False
    for lib in arch_section['libs_info']:
        try:
            print(f"{lib}")
            isexists = os.path.exists(arch_section['libs_files_dir'] + lib)
            assert isexists
        except:
            print(f"{lib} did not pass the test")
            assert False