# config
PYTHON := python3
HOST := 0.0.0.0
PORT := 3662

# directories
DOC := docs
LOG := log
PACKAGE := hal3662
SRC := src
VENV := venv

# hal3662 package
MODS := $(PACKAGE)/__init__.py
#MODS += $(PACKAGE)/auth.py
#MODS += $(PACKAGE)/billing.py

# hal3662.calculate package
#MODS += $(PACKAGE)/calculate/__init__.py
#MODS += $(PACKAGE)/calculate/reverse.py

# documentation
HTML := $(DOC)/hal3662.html

# build everything and run unit tests
all: $(MODS) $(HTML)
	mkdir -p $(LOG)
	$(PYTHON) -m compileall $(PACKAGE) > $(LOG)/compileall.txt
	$(PYTHON) -m unittest discover -t . > $(LOG)/unittest.discover.txt

# build package only
build: $(MODS)

# build package and documentation only
doc: $(MODS) $(HTML)

# discover and run tests
test:
	$(PYTHON) -m unittest discover -t .

# create cache files
cache: $(MODS)
	$(PYTHON) -m compileall $(PACKAGE)
	
# copy python module from source directory
$(PACKAGE)/%.py: $(SRC)/%.py
	mkdir -p $(@D)
	cp $< $@

# create documentation
$(DOC)/hal3662.html:
	mkdir -p $(@D)
	$(PYTHON) -m pydoc hal3662 > $@

# create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

# activate virtual environment
activate:
	source $(VENV)/bin/activate

# do cleanup
clean:
	rm -Rf $(DOC)
	rm -Rf $(LOG)
	rm -Rf $(PACKAGE)
	rm -Rf $(VENV)

# print value of a variable
print-%:
	@echo $* = $($*)
