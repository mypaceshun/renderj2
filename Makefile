VENV		= venv
ACTIVATE	= . ./${VENV}/bin/activate
ARGS		= --varsfile test/testvars.yml --varsfile test/testvars2.yml test/testtemplate.j2

.PHONY: usage
usage:
	run              run script used test files
	run ARGS=...     run script used ARGS
	build            build venv directory
	clean            clean venv directory and files
	lint             run lint use flake8
	test             run test script

.PHONY: run
run: activate
	${ACTIVATE} && pyrender/pyrender.py ${ARGS}

.PHONY: build
build: activate

activate: ${VENV}
	@ln -s -v ./${VENV}/bin/activate

${VENV}: requirements.txt
	python3 -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
	rm activate

.PHONY: lint
lint:
	@${ACTIVATE} && flake8 pyrender/*.py || :

.PHONY: test
test:
	@${ACTIVATE} && test/command_test.sh
