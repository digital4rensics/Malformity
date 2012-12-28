__author__ = 'ndouba'
 
# What: A fast track script to convert Maltego entities into canari class files.
# Howto: Export your entities into a mtz file and then run this script against it.
 
 
from xml.etree.cElementTree import XML
from zipfile import ZipFile
from re import sub
from sys import argv
 
zip = ZipFile(argv[1])
entities = filter(lambda x: x.endswith('.entity'), zip.namelist())
 
 
def normalize_fn(fn):
    # Get rid of starting underscores or numbers and bad chars for var names in python
    return sub(r'[^A-Za-z0-9]', '', sub(r'^[^A-Za-z]+', '', fn))
 
 
nses = dict()
 
for e in entities:
    xml = XML(zip.open(e).read())
    id_ = xml.get('id')
 
    ens = id_.split('.')
 
    base_classname = None
    namespace = '.'.join(ens[:-1])
    name = ens[-1]
    classname = name
 
    if namespace not in nses:
        base_classname = '%sEntity' % (''.join([ n.title() for n in ens[:-1] ]))
        nses[namespace] = base_classname
 
        print 'class %s(Entity):\n    namespace = %s\n\n' % (base_classname, repr(namespace))
    else:
        base_classname = nses[namespace]
 
 
    for f in xml.findall('Properties/Fields/Field'):
        fields = [
            'name=%s' % repr(f.get('name')),
            'propname=%s' % repr(normalize_fn(f.get('name'))),
            'displayname=%s' % repr(f.get('displayName'))
 
        ]
        print '@EntityField(%s)' % ', '.join(fields)
 
    print 'class %s(%s):\n    pass\n\n' % (classname, base_classname)