rm -rf build/*
rm -f dist/*
python setup.py sdist bdist_wheel
twine upload dist/*
