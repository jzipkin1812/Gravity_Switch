onefile:
	pyinstaller --onefile src/gravityswitch.py --paths src --add-data "src/lib/assets:assets"
macOS:
	pyinstaller --windowed src/gravityswitch.py --paths src --add-data "src/lib/assets:assets"
clean:
	rm -rf build
	rm -rf dist
	rm gravityswitch.spec