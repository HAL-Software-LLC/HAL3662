# config
PYTHON := python3
HOST := 0.0.0.0
PORT := 3662

# directories
DOC := docs
PACKAGE := hal3662
SRC := src
SSL := ssl
VENV := venv

# hal3662 package
MODS := $(PACKAGE)/__init__.py
#MODS += $(PACKAGE)/auth.py
#MODS += $(PACKAGE)/billing.py
MODS += $(PACKAGE)/info.py

# hal3662.calculate package
#MODS += $(PACKAGE)/calculate/__init__.py
#MODS += $(PACKAGE)/calculate/reverse.py

# build everything and deploy flask test server
all: $(MODS)
	mkdir -p $(DOC)
	$(PYTHON) -m pdoc --no-search -o $(DOC) hal3662
	rsync -r $(DOC) $(PACKAGE)/docs
	$(PYTHON) -m compileall $(PACKAGE)
	$(PYTHON) -m flask --app hal3662 run --host=$(HOST) --port=$(PORT)

# build and compile package
build: $(MODS)
	$(PYTHON) -m compileall $(PACKAGE)

# build package and documentation
doc: $(MODS)
	mkdir -p $(DOC)
	$(PYTHON) -m pdoc --no-search -o $(DOC) hal3662
	rsync -r $(DOC) $(PACKAGE)/docs

# discover and run tests
test: $(MODS)
	$(PYTHON) -m unittest discover -s $(PACKAGE) -t .

# create cache files
cache: $(MODS)
	$(PYTHON) -m compileall $(PACKAGE)
	
# copy python module from source directory
$(PACKAGE)/%.py: $(SRC)/%.py
	mkdir -p $(@D)
	cp $< $@

# deploy test website
deploy: $(MODS)
	$(PYTHON) -m flask --app hal3662 run --host=$(HOST) --port=$(PORT)

# create virtual environment (activate with `source venv/bin/activate`)
$(VENV):
	$(PYTHON) -m venv $(VENV)

# install python dependencies in virtual enviornment
reqs: $(VENV) requirements.txt
	$(PYTHON) -m pip install -r requirements.txt

# activate virtual environment
activate:
	source $(VENV)/bin/activate

# do cleanup
clean:
	rm -Rf $(PACKAGE)

# print value of a variable
print-%:
	@echo $* = $($*)
