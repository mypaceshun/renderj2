NAME		= pyrender
VERSION		= ${shell cat ../version}
PACKAGE-NAME	= ${NAME}-${VERSION}
CP		= cp -rf
MKDIR		= mkdir -p

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  deploy       deploy scripts for rpmbuild"
	@echo ""
	@echo "PackageName: ${PACKAGE-NAME}"

.PHONY: deploy
deploy: version README.md
	${MKDIR} ${PACKAGE-NAME}
	${CP} ../pyrender ${PACKAGE-NAME}/
	${CP} ../test ${PACKAGE-NAME}/
	${CP} ../requirements.txt ${PACKAGE-NAME}/
	${CP} ../setup.cfg ${PACKAGE-NAME}/
	${CP} ../setup.py ${PACKAGE-NAME}/
	${CP} ../Makefile ${PACKAGE-NAME}/
	${CP} ../LICENSE ${PACKAGE-NAME}/
	${CP} ../README.md ${PACKAGE-NAME}/
	${CP} ../version ${PACKAGE-NAME}/
	tar zcf ${PACKAGE-NAME}.tar.gz ${PACKAGE-NAME}/
	install -d -m 0755 SOURCES/
	mv ${PACKAGE-NAME}.tar.gz SOURCES/
	rm -rf ${PACKAGE-NAME}

version:
	${CP} ../version .

README.md:
	${CP} ../README.md .
