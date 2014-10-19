from lxml import etree
import sys

def transform_field(f,depth):
	name=""
	if len(f.get('name'))==0:
		name=f.get('show')
	else: 
		name=f.get("showname")
	print ("-"*depth),name

def parse_field(field,depth=0):
	transform_field(field,depth)

	for f in field.getchildren():
		parse_field(f,depth+1)

tree=etree.parse(open(sys.argv[1]))
field=tree.xpath('/pdml/packet/proto[@name=\'mq\']')[0]

parse_field(field)

