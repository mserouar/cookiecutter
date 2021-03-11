"""
Initialize a new Git repository for the project and install the base module in development mode.
"""
import os
import subprocess
import sys
import textwrap
import traceback


IS_LINUX = sys.platform.startswith('linux')
BASH_ENV = None
EXECUTABLE = None
if IS_LINUX:
	EXECUTABLE = 'bash'
	BASH_ENV = os.environ.copy()
	BASH_ENV.update(BASH_ENV='/usr/local/bin/virtualenvwrapper.sh')


def get_python_executable(version):
	"""
	Return Python executable path for the given version. On Linux, there is no check to assert that
	the given version actually exists.

	:param str version: MAJOR.MINOR version.
	:return: Executable path.
	:rtype: str
	:raises RuntimeError: The given version of Python was not found.
	"""
	if IS_LINUX:
		return 'python{}'.format(version)

	# The launcher is required on Windows as there is no executable with the version in the name
	# and other versions may not be on the PATH.
	try:
		response = subprocess.run(
			'py -{} -c "import sys; print(sys.executable)"'.format(version),
			stdout=subprocess.PIPE,
			check=True,
			universal_newlines=True,
			# shell=True is required on Windows to get the output of py, without it, nothing is
			# captured.
			shell=True
			)
	except subprocess.CalledProcessError:
		raise RuntimeError('python executable not found: {}'.format(version))

	return response.stdout.strip()

def init_local_repository():
	"""
	Init a new local Git repository in the template project, make an initial commit then tag the
	initial commit as "0.0.0".
	"""
	command = (
		'git init . '
		'&& git add . '
		'&& git commit -m "Initial Python CLI Module template" '
		'&& git tag -m "{{cookiecutter.module_name}} version 0.0.0" 0.0.0'
		)
	try:
		subprocess.run(command, check=True, shell=True)
	except subprocess.CalledProcessError:
		raise RuntimeError('Git repository could not be initialized')

def init_venv():
	"""
	Init a new virtualenv for the project, activate it then install the empty project in development
	mode.
	"""
	venv_command = {{cookiecutter.virtual_env}}_venv_command()
	command = '{venv_command} && pip install -e .[dev]'.format(venv_command=venv_command)

	try:
		subprocess.run(command, check=True, shell=True, executable=EXECUTABLE, env=BASH_ENV)
	except subprocess.CalledProcessError:
		raise RuntimeError('virtualenv could not be initialized with {{cookiecutter.virtual_env}}')

def print_error(exc):
	"""Print a chained exception without traceback."""
	if exc.__context__ is not None:
		print_error(exc.__context__)

	traceback.print_exception(None, exc, None, chain=False)

# --------------------------------------------------------------------------------------------------
# Vitualenv commands
# --------------------------------------------------------------------------------------------------
def conda_venv_command():
	"""Return the command to create and activate a virtualenv with Anaconda."""
	cmd = 'conda create -y --name {{cookiecutter.module_slug}} python={{cookiecutter.python_version}}'

	if IS_LINUX:
		return '{} && source activate {{cookiecutter.module_slug}}'.format(cmd)

	return '{} && activate {{cookiecutter.module_slug}}'.format(cmd)

def virtualenvwrapper_venv_command():
	"""Return the command to create and activate a virtualenv with virtualenvwrapper."""
	exe_path = get_python_executable('{{cookiecutter.python_version}}')
	cmd = (
		'mkvirtualenv --python {exe_path} {{cookiecutter.module_slug}} '
		'&& workon {{cookiecutter.module_slug}}'.format(exe_path=exe_path)
		)

	if IS_LINUX:
		# Compatibility with the pyenv plugin
		return 'eval "$(pyenv init -)" && pyenv virtualenvwrapper ; {}'.format(cmd)

	return cmd

def venv_venv_command():
	"""Return the command to create and activate a virtualenv with venv."""
	if IS_LINUX:
		cmd = 'python{{cookiecutter.python_version}} -m venv venv && . venv/bin/activate '
	else:
		cmd = 'py -{{cookiecutter.python_version}} && venv\\Scripts\\activate.bat'

	return '{} && python -m pip install --upgrade pip'.format(cmd)

# --------------------------------------------------------------------------------------------------
# Execute the hooks
# --------------------------------------------------------------------------------------------------
def main():
	"""Execute the post_gen_project hook."""
	{% if cookiecutter.init_git_repository|lower == "y" %}
	try:
		# Try to initialize a new Git repository
		init_local_repository()
	except RuntimeError as exc:
		print_error(exc)
		print(textwrap.dedent('''
			Don't worry, your project is still usable!

			However, you need to do some manual steps before you can begin all the good work:
			- create a new Git repository in your newly created project with your favorite tool
			- make an initial commit with the empty project
			- tag that commit as "0.0.0" with the message "{{cookiecutter.module_name}} version 0.0.0"
			- create a Python virtual environment and active it
			- install the project in development mode: pip install -e {{cookiecutter.module_slug}}[dev]
			'''))
		return
	{% endif %}

	{% if cookiecutter.init_virtual_env|lower == "y" %}
	try:
		# Try to initialize a new virtualenv
		init_venv()
	except RuntimeError as exc:
		print_error(exc)
		print(textwrap.dedent('''
			Don't worry, your project is still usable!

			However, you need to do some manual steps before you can begin all the good work:
			- create a Python virtual environment and active it
			- install the project in development mode: pip install -e {{cookiecutter.module_slug}}[dev]
			'''))
		return
	{% endif %}

	# Message that all went well
	print('\nThe project has been correctly initialized and is ready to use!')

	{% if cookiecutter.init_virtual_env|lower == "y" %}
	# Specific message to activate the virtualenv
	{% if cookiecutter.virtual_env == "conda" %}
	cmd = 'conda activate {{cookiecutter.module_slug}}'
	{% elif cookiecutter.virtual_env == "venv" %}
	if IS_LINUX:
		cmd = 'cd {{cookiecutter.module_slug}} && . venv/bin/activate'
	else:
		cmd = 'cd {{cookiecutter.module_slug}} && venv\\Scripts\\activate.bat'
	{% elif cookiecutter.virtual_env == "virtualenvwrapper" %}
	cmd = 'workon {{cookiecutter.module_slug}}'
	{% endif %}
	print('To activate your project virtual environment:', cmd)
	{% endif %}


if __name__ == '__main__':
	main()
