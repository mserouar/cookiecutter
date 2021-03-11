"""
Validate the variables input by the user.
"""
import re
import sys


# Get the input variables we want to validate
TRAIT_OR_NAME = '{{cookiecutter.trait_or_name}}'.strip()
MODULE_NAME = '{{cookiecutter.module_name}}'.strip()
MODULE_SLUG = '{{cookiecutter.module_slug}}'.strip()
PACKAGE_NAME = '{{cookiecutter.package_name}}'

# Validatation regex
MODULE_NAME_REGEX = r'^[a-zA-Z- ]+[a-zA-Z]$'
MODULE_SLUG_REGEX = r'^[a-z][a-z-]+[a-z]$'
PACKAGE_NAME_REGEX = r'^[a-z]+$'


def main():
	"""Execute the pre_gen_project hook."""
	exit_code = 0

	if not TRAIT_OR_NAME:
		print('ERROR: {!r} is not a valid trait or name!'.format(TRAIT_OR_NAME), file=sys.stderr)
		exit_code = 1

	if not re.match(MODULE_NAME_REGEX, MODULE_NAME):
		print('ERROR: {!r} is not a valid module name!'.format(MODULE_NAME), file=sys.stderr)
		exit_code = 1
	if not re.match(MODULE_SLUG_REGEX, MODULE_SLUG):
		print('ERROR: {!r} is not a valid module slug!'.format(MODULE_SLUG), file=sys.stderr)
		exit_code = 1
	if not re.match(PACKAGE_NAME_REGEX, PACKAGE_NAME):
		print('ERROR: {!r} is not a valid package name!'.format(PACKAGE_NAME), file=sys.stderr)
		exit_code = 1

	return exit_code


if __name__ == '__main__':
	sys.exit(main())
