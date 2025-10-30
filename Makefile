.PHONY: build check upload upload-test clean

build:
	python -m build --no-isolation

check:
	twine check dist/*

upload:
	# Requires TWINE_USERNAME=__token__ and TWINE_PASSWORD=
	twine upload dist/*

upload-test:
	# Requires TWINE_USERNAME=__token__ and TWINE_PASSWORD=
	twine upload -r testpypi dist/*

clean:
	rm -rf dist build *.egg-info

