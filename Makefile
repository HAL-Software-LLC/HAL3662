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

# more config
CERT := $(VENV)/ssl/cert.pem
KEY := $(VENV)/ssl/key.pem

# hal3662 package
MODS := $(PACKAGE)/__init__.py
#MODS += $(PACKAGE)/auth.py
#MODS += $(PACKAGE)/billing.py

# hal3662.calculate package
#MODS += $(PACKAGE)/calculate/__init__.py
#MODS += $(PACKAGE)/calculate/reverse.py

# documentation
HTML := $(DOC)/hal3662.html

# build everything and deploy flask test server
all: $(MODS) $(HTML) $(CERT)
	$(PYTHON) -m compileall $(PACKAGE)
	$(PYTHON) -m flask --app hal3662 run --host=$(HOST) --port=$(PORT) --cert=$(CERT) --key=$(KEY)

# build package only
build: $(MODS)
	$(PYTHON) -m compileall $(PACKAGE)

# build package and documentation only
doc: $(MODS) $(HTML)

# discover and run tests
test: $(MODS)
	$(PYTHON) -m unittest discover -t .

# create cache files
cache: $(MODS)
	$(PYTHON) -m compileall $(PACKAGE)
	
# copy python module from source directory
$(PACKAGE)/%.py: $(SRC)/%.py
	mkdir -p $(@D)
	cp $< $@

# create documentation
$(DOC)/hal3662.html: $(PACKAGE)/__init__.py
	mkdir -p $(@D)
	$(PYTHON) -m pydoc hal3662 > $@

# deploy test website
deploy: $(MODS) $(CERT)
	$(PYTHON) -m flask --app hal3662 run --host=$(HOST) --port=$(PORT) --cert=$(CERT) --key=$(KEY)

# generate certificate for test website
$(VENV)/ssl/cert.pem: $(VENV)
	mkdir -p $(VENV)/ssl
	openssl req -x509 -newkey rsa:4096 -keyout $(@D)/key.pem -out $(@D)/cert.pem -sha256 -days 365 -nodes

# create virtual environment
$(VENV):
	$(PYTHON) -m venv $(VENV)

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
