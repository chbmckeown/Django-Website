build:
	docker build --force-rm $(options) -t kawage:latest .

build-prod:
	$(NAME) build options="--target production"