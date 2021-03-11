Welcome to {{cookiecutter.module_name}}'s documentation!
{{'=' * (28 + cookiecutter.module_name|length)}}

{{cookiecutter.short_description|wordwrap(100)}}

.. toctree::
	:maxdepth: 2
	:caption: Contents

	quickstart
	cli
	qualityassessment

.. toctree::
	:maxdepth: 2
	:caption: Specifications

	inputformats
	outputformats

.. toctree::
	:maxdepth: 3
	:caption: API Reference

	api/{{cookiecutter.package_name}}
