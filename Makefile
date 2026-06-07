clean:
	rm -rf  */.mypy*

COM=generic_com

git:
	git add .
	git commit -m $(COM)
	git push origin $(shell git branch --show-current)