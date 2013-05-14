#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
__credits__ = ['Special thanks to Ohdae for the original entity creation. https://github.com/ohdae']

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'MalformityEntity',
#    'MyMalformityEntity',
#    'InsiderThreat',
#    'AdvancedTargetedAttacker',
#    'OpportunityAttacker',
#    'OrganizedCrime',
#    'ZombieHost',
#    'CompromisedHost',
#    'BotnetDNSNode',
#    'C2',
    'ServiceName',
    'Hash',
#   'FilePath',
#    'HiddenFile',
    'RegistryEntry',
#    'UserAccount',
    'MaliciousProcess',
#    'BrowserCookie',
    'HTTPRequest',
    'Filename',
#    'MaliciousWebsite',
#    'Certificate',
#    'Exploit',
#    'ExploitationChain',
#    'Phishing',
    'UserAgent'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyMalformityEntity will
have an entity type name of Malformity.MyMalformityEntity. When adding a new entity in Maltego, you will have to specify this
name (Malformity.MyMalformityEntity) in the 'Unique entity type' field.
"""
class MalformityEntity(Entity):
    namespace = 'malformity'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
TODO: define as many custom fields and entity types as you wish:)
"""    
#@EntityField(name='Malformity.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
#@EntityField(name='Malformity.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
#class MyMalformityEntity(MalformityEntity):
#    """
#    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
#    'my.fancy.EntityType'
#    """
#    # name = my.fancy.EntityType
#    pass
    
#@EntityField(name='malformity.insiderthreat', propname='propertiesinsiderthreat', displayname='Insider Threat')
#class InsiderThreat(MalformityEntity):
#    pass


#@EntityField(name='malformity.advancedtargetedattacker', propname='propertiesadvancedtargetedattacker', displayname='Advanced Targeted Attacker')
#class AdvancedTargetedAttacker(MalformityEntity):
#    pass


#@EntityField(name='malformity.opportunityattacker', propname='propertiesopportunityattacker', displayname='Opportunity Attacker')
#class OpportunityAttacker(MalformityEntity):
#    pass


#@EntityField(name='malformity.organizedcrime', propname='propertiesorganizedcrime', displayname='Organized Crime')
#class OrganizedCrime(MalformityEntity):
#    pass


#@EntityField(name='malformity.zombie', propname='propertieszombie', displayname='Zombie')
#class ZombieHost(MalformityEntity):
#    pass


#@EntityField(name='malformity.compromisedhost', propname='propertiescompromisedhost', displayname='Compromised Host')
#class CompromisedHost(MalformityEntity):
#    pass


#@EntityField(name='malformity.botnetdnsrelay', propname='propertiesbotnetdnsrelay', displayname='Botnet DNS Relay')
#class BotnetDNSNode(MalformityEntity):
#    pass


#@EntityField(name='malformity.c2', propname='propertiesc2', displayname='C2')
#class C2(MalformityEntity):
#    pass
    

@EntityField(name='properties.servicename', propname='servicename', displayname='Service Name')
class ServiceName(MalformityEntity):
    pass


@EntityField(name='properties.hash', propname='hash', displayname='Hash')
class Hash(MalformityEntity):
    pass


#@EntityField(name='malformity.filepath', propname='propertiesfilepath', displayname='File Path')
#class FilePath(MalformityEntity):
#    pass


#@EntityField(name='malformity.hiddenfile', propname='propertieshiddenfile', displayname='Hidden File')
#class HiddenFile(MalformityEntity):
#    pass


@EntityField(name='properties.registryentry', propname='registryentry', displayname='Registry Entry')
class RegistryEntry(MalformityEntity):
    pass


#@EntityField(name='malformity.useraccount', propname='propertiesuseraccount', displayname='User Account')
#class UserAccount(MalformityEntity):
#    pass


@EntityField(name='properties.maliciousprocess', propname='maliciousprocess', displayname='Malicious Process')
class MaliciousProcess(MalformityEntity):
    pass


#@EntityField(name='malformity.browsercookie', propname='propertiesbrowsercookie', displayname='Browser Cookie')
#class BrowserCookie(MalformityEntity):
#    pass


@EntityField(name='properties.httprequest', propname='httprequest', displayname='HTTP Request')
class HTTPRequest(MalformityEntity):
    pass


@EntityField(name='properties.filename', propname='filename', displayname='Filename')
class Filename(MalformityEntity):
    pass


#@EntityField(name='malformity.maliciouswebsite', propname='propertiesmaliciouswebsite', displayname='Malicious Host')
#class MaliciousWebsite(MalformityEntity):
#    pass


#@EntityField(name='malformity.certificate', propname='propertiescertificate', displayname='Certificate')
#class Certificate(MalformityEntity):
#    pass


#@EntityField(name='malformity.exploit', propname='propertiesexploit', displayname='Exploit')
#class Exploit(MalformityEntity):
#    pass


#@EntityField(name='malformity.exploitationchain', propname='propertiesexploitationchain', displayname='Exploitation Chain')
#class ExploitationChain(MalformityEntity):
#    pass


#@EntityField(name='malformity.phishing', propname='propertiesphishing', displayname='Phishing')
#class Phishing(MalformityEntity):
#    pass


@EntityField(name='properties.useragent', propname='useragent', displayname='User Agent')
class UserAgent(MalformityEntity):
	pass
