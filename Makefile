VENV		= pyrenderenv
ACTIVATE	= . ./${VENV}/bin/activate
ARGS		= --varsfile test/testvars.yml --varsfile test/testvars2.yml test/testtemplate.j2
DISTDIR		=
LIBDIR		= /var/lib
BINDIR		= /bin
PIPENV          = pipenv
TARGET          = testpypi

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "  run              run script used test files"
	@echo "    ARGS=...       run script used ARGS"
	@echo "  dev              build venv directory"
	@echo "  clean            clean venv directory and files"
	@echo "  lint             run lint use flake8"
	@echo "  test             run test script"
	@echo ""
	@echo "  build            build wheel package and tar archive"
	@echo "  upload           upload to ${TARGET}"
	@echo "    TARGET=pypi    upload to pypi"
	@echo ""
	@echo "  install          install pyrender command"
	@echo "    DISTDIR=...    install target directory"
	@echo ""
	@echo "  rpm              make rpm package used docker"

.PHONY: build
build:
	${MAKE} -s clean
	${PIPENV} run python setup.py bdist_wheel sdist --format=gztar,zip
	${PIPENV} run twine check dist/*


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
rpm: product
	cd rpm && ${MAKE} deploy
	cd docker && ${MAKE} run

product:
	mkdir -p product/RPMS

.PHONY: wheel
wheel: activate
	@${MAKE} lint
	@${MAKE} test
	${ACTIVATE} && python setup.py bdist_wheel

.PHONY: run
run: activate
	${ACTIVATE} && pyrender/pyrender.py ${ARGS}

.PHONY: dev
dev: activate

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
