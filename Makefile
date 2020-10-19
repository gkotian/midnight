build:
	@docker build -t midnight .

run: build
	@docker run --rm midnight

.PHONY: build run
