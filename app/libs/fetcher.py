import json
import urllib
import subprocess

def get_file_url(group, name, version, ar):
  return 'http://repo1.maven.org/maven2/{0}/{1}/{2}/{1}-{2}.{3}'.format(group.replace('.', '/'), name, version, ar)


def get_jar(url):
  subprocess.call('wget '+ url, shell=True)

def mavensha1(group, name, version, ar):
	try:
		link = get_file_url(group, name, version, ar) + '.sha1'
		f = urllib.urlopen(link)
		cksum = f.read()
		int(cksum, 16) # will throw an error if cksum is not a hexadecimal string
		return cksum
	except ValueError:
		return None


with open('dependencies.json') as data_file:
    dependencies = json.load(data_file)

for dependency in dependencies:
    group, name, version = dependency['path'].split(':',3)

    for ar in ['aar','jar']:
        if mavensha1(group, name, version, ar) != None:
            get_jar(get_file_url(group, name, version, ar))
