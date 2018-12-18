VENV		= pyrenderenv
ACTIVATE	= . ./${VENV}/bin/activate
ARGS		= --varsfile test/testvars.yml --varsfile test/testvars2.yml test/testtemplate.j2
DISTDIR		=
LIBDIR		= /var/lib
BINDIR		= /bin

.PHONY: usage
usage:
	@echo "run              run script used test files"
	@echo "run ARGS=...     run script used ARGS"
	@echo "build            build venv directory"
	@echo "clean            clean venv directory and files"
	@echo "lint             run lint use flake8"
	@echo "test             run test script"

.PHONY: install
install:
	install -d -m 0755 ${DISTDIR}${LIBDIR}/pyrender
	install requirements.txt ${DISTDIR}${LIBDIR}/pyrender/
	cd ${DISTDIR}${LIBDIR}/pyrender/ && python3 -m venv ${VENV}
	. ${DISTDIR}${LIBDIR}/pyrender/${VENV}/bin/activate && pip install --upgrade pip setuptools wheel
	. ${DISTDIR}${LIBDIR}/pyrender/${VENV}/bin/activate && pip install -r ${DISTDIR}${LIBDIR}/pyrender/requirements.txt
	. ${DISTDIR}${LIBDIR}/pyrender/${VENV}/bin/activate && python setup.py install
	install -d -m 0755 ${DISTDIR}${BINDIR}/
	mv ${DISTDIR}${LIBDIR}/pyrender/${VENV}/bin/pyrender ${DISTDIR}${BINDIR}/pyrender


.PHONY: rpm
rpm:
	cd rpm && ${MAKE} deploy
	cd docker && ${MAKE} run

.PHONY: wheel
wheel: activate
	@${MAKE} lint
	@${MAKE} test
	${ACTIVATE} && python setup.py bdist_wheel

.PHONY: run
run: activate
	${ACTIVATE} && pyrender/pyrender.py ${ARGS}

activate: ${VENV}
	@ln -s -v ./${VENV}/bin/activate

${VENV}: requirements.txt
	python3 -m venv ${VENV}
	${ACTIVATE} && pip install --upgrade pip setuptools wheel
	${ACTIVATE} && pip install --upgrade -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
	rm -rf activate
	rm -rf build dist pyrender.egg-info
	cd docker && ${MAKE} clean
	cd rpm && ${MAKE} clean

.PHONY: lint
lint: activate
	@${ACTIVATE} && flake8 pyrender/*.py || :
	${ACTIVATE} && python setup.py flake8

.PHONY: test
test: activate
	@${ACTIVATE} && test/command_test.sh
	${ACTIVATE} && python setup.py check
