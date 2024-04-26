# config
PYTHON := python3
HOST := 0.0.0.0
PORT := 3662

# directories
INSTALL := .
DOC := docs
LOG := log
PACKAGE := hal3662
SRC := src
VENV := venv

# hal3662 package
MODS := $(PACKAGE)/__init__.py
MODS += $(PACKAGE)/auth.py
MODS += $(PACKAGE)/billing.py

# hal3662.calculate package
MODS += $(PACKAGE)/calculate/__init__.py
MODS += $(PACKAGE)/calculate/reverse.py

# documentation
HTML := $(patsubst %.py,%.html,$(MODS))

# build everything and run unit tests
all: $(MODS) #$(HTML)
	$(PYTHON) -m compileall $(PACKAGE) > $(LOG)/compileall.txt
	$(PYTHON) -m unittest discover -t $(INSTALL)/$(PACKAGE) > $(LOG)/unittest.discover.txt

# copy python module from source directory
$(PACKAGE)/%.py: $(SRC)/%.py
	mkdir -p $(@D)
	cp $< $@

# generate documentation for package
$(DOC)/%.html: $(SRC)/%/__init__.py
	mkdir -p $(@D)

# discover and run tests
test:
	$(PYTHON) -m unittest discover -t $(INSTALL)/$(PACKAGE)

# create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	$(PYTHON) -m pip install -r requirements.txt

# create cache files
cache:
	$(PYTHON) -m compileall $(PACKAGE)
	
# do cleanup
clean:
	rm -Rf $(LOG)
	rm -Rf $(PACKAGE)
	rm -Rf $(VENV)

# print value of a variable
print-%:
	@echo $* = $($*)
