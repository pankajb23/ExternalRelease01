from setuptools import setup, find_packages
setup(
    name = 'Pipeline02',
    version = '1.0',
    packages = find_packages(include = ('pipeline02*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.8.7'],
    entry_points = {
'console_scripts' : [
'main = pipeline02.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
