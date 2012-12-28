Malformity
==========

## 1.0 Introduction

Malformity is a Maltego project based upon the [Canari Framework](https://github.com/allfro/canari).
Using this framework greatly simplifies the process of installing local transforms in [Maltego](http://paterva.com/).

The project directory structure is as follows:

* `src/Malformity` directory is where all your stuff goes in terms of auxiliary modules that you may need for your
  modules
* `src/Malformity/transforms` directory is where all your transform modules should be placed.
* `src/Malformity/transforms/common` directory is where you can put some common code for your transforms like result
  parsing, entities, etc.
* `src/Malformity/transforms/common/entities.py` is where you define your custom entities.
* `maltego/` is where you can store your Maltego entity exports.

If you're going to add a new transform in the transforms directory, remember to update the `__all__` variable in
`src/Malformity/transforms/__init__.py`. Otherwise, `canari install-package` won't attempt to install the transform.
Alternatively, `canari create-transform <transform name>` can be used within the `src/Malformity/transforms` directory
to generate a transform module and have it automatically added to the `__init__.py` file.

## 2.0 Installing Malformity

### 2.1 - Supported Platforms
Malformity has been tests on Mac OSX. Tranforms are written in Python version 2.7.

### 2.2 - Requirements
In order to make full use of Malformity, the setup script will download additional modules.

If for some reason these fail, requirements are:
* Canari 0.5
* Mechanize 0.2.5
* BeautifulSoup 3.2.1

### 2.3 - Installation
```bash
$ sudo python setup.py install
```

After completing setup, the command below can be used to install Malformity in Maltego.

```bash
$ canari install-package Malformity
```

## 3.0 Credits
Special thanks is due to the following people:

* Nadeem Douba - For creating the Canari framework and offering great support
* [ohdae](https://github.com/ohdae) - For allowing us to include his entity set in Malformity

# Contact

[@digital4rensics](https://twitter.com/Digital4rensics) - www.digital4rensics.com - Keith@digital4rensics.com