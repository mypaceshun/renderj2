DOCKER-IMAGE		= rpmbuild
DOCKER-CONTAINER	= rpmbuild
RPM-DIRECTORY		= rpm

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} TARGET"
	@echo ""
	@echo "Targets:"
	@echo "  build          build docker image"
	@echo "  run            run docker container"
	@echo "  clean          remove docker container"
	@echo "  deploy         deploy ${RPM-DIRECTORY}.tar.gz for ${DOCKER-IMAGE}"

.PHONY: build
build: deploy
	docker build -t ${DOCKER-IMAGE} .

.PHONY: run
run: build
	docker run --name ${DOCKER-CONTAINER} --rm ${DOCKER-IMAGE}

.PHONY: clean
clean:
	@docker container rm ${DOCKER-CONTAINER} >/dev/null 2>&1 || :
	@rm -rf ${RPM-DIRECTORY}.tar.gz

.PHONY: deploy
deploy: ${RPM-DIRECTORY}.tar.gz

${RPM-DIRECTORY}.tar.gz: CMD.sh ../${RPM-DIRECTORY}
	cp -rf ../${RPM-DIRECTORY} .
	cp -p CMD.sh ${RPM-DIRECTORY}/
	tar zcf ${RPM-DIRECTORY}.tar.gz ${RPM-DIRECTORY}
	rm -rf ${RPM-DIRECTORY}
