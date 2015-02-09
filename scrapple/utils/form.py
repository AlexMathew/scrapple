"""
scrapple.utils.form
~~~~~~~~~~~~~~~~~~~

Functions related to form handling.
"""

import os
import json
import itertools


def form_to_json(form):
	config = dict()
	if form['project_name'] == "":
		raise Exception('Project name cannot be empty.')
	if form['selector_type'] not in ["css", "xpath"]:
		raise Exception('Selector type has to css or xpath')
	config['project_name'] = form['project_name']
	config['selector_type'] = form['selector_type']
	config['scraping'] = dict()
	if form['url'] == "":
		raise Exception('URL cannot be empty')
	config['scraping']['url'] = form['url']
	config['scraping']['data'] = list()
	for i in itertools.count(start=1):
		try:
			data = {
				'field': form['field_' + str(i)],
				'selector': form['selector_' + str(i)],
				'attr': form['attribute_' + str(i)]
			}
			config['scraping']['data'].append(data)
		except KeyError:
			break
	# TODO : Crawler 'next' parameter handling
	with open(os.path.join(os.getcwd(), form['project_name'] + '.json'), 'w') as f:
		json.dump(config, f)
	return
