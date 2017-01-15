__author__ = 'Leonardo'


class Game:
	to_name = ""

	def __init__(self, xml, new_name="Created_In_Python"):
		self.to_name = new_name
		self.getStruct(xml)


	def mkinput(self, t0, options, tabs=1):
		s = ""
		for i in range(tabs):
			s += "    "
		s += "r = input(\"" + str(t0) + "\\n "
		c = 1
		for k in options:
			s += " [" + str(c) + "]-" + k + "\\n "
			c += 1
		s += " [" + str(c)+"]- Go Back \")\n"
		return s

	def getStruct(self, file):
		import xml.dom.minidom
		DOMTree = xml.dom.minidom.parse(file)
		file = DOMTree.documentElement
		places = file.getElementsByTagName("place")
		awsers_list = []
		question_dict = {}
		objt_dict = {}
		places_dict = {}
		for place in places:
			objs = place.getElementsByTagName('obj')
			for obj in objs:
				questions = obj.getElementsByTagName("question")
				for question in questions:
					answers = question.getElementsByTagName('awnser')
					for awnser in answers:
						s = awnser.childNodes[0].data
						if awnser.getAttribute('gold') == 'true':
							s += '\&'
						awsers_list.append(s)
					question_dict[question.getAttribute('title')] = awsers_list
					awsers_list = []
				objt_dict[obj.getAttribute('title')] = question_dict
				question_dict = {}
			places_dict[place.getAttribute('title')] = objt_dict
		self.generate_code(places_dict)

	def generate_code(self, places):
		code = "points = 0\n"
		code += "done = False\n"
		code += "while not done:\n"
		t = list(places)[0]#selects main dict of places e.g: Kitchen
		code += self.mkinput("You are in the " + t + ". What do you  wanna investigate?", places[t].keys())# main dict 1sub dicts keys e.g: Fridge, Closet
		c = 1
		for obj in places[t].keys():#loops thru 1st sub dicts
			if c == 1:
				code += "    if r == '" + str(c) + "':#c\n"
			else:
				code += "    elif r == '" + str(c) + "':#c\n"
			code += "        while not done:\n"
			code += self.mkinput("You are in the "+ obj + ". What you want to do?", places[t][obj], 3)
			d = 1
			for question in places[t][obj].keys():
				if d == 1:
					code += "            if r == '" + str(d) + "':#d\n"
				else:
					code += "            elif r == '" + str(d) + "':#d\n"
				code += self.mkinput("What Now?", places[t][obj][question], 4)
				code += "                while not done:\n"
				e = 1
				for awnser in places[t][obj][question]:
					if e == 1:
						code += "                    if r == '" + str(e) + "':#e\n"
					else:
						code += "                    elif r == '" + str(e) + "':#e\n"
					code += self.mkinput("OK.", [], 6)
					if "\&" in awnser:
						code += "                        points += 100\n"
					code += "                        done = True\n"
					e += 1
				code += "                    elif r == '" + str(e) + "':#e-\n"
				code += "                        done = True\n"
				code += "                done = False\n"
				d += 1
			code += "            elif r == '" + str(d) + "':#d-\n"
			code += "                done = True\n"
			code += "        done = False\n"
			c += 1
		code += "    elif r == '" + str(c) + "':#c-\n"
		code += "        done = True\n"
		code += "print(\"You Made:\" + str(points) + \" points\")"
		self.create_file(self.to_name, code)

	def create_file(self, filename, code):
                #filename = filename + "/" + filename
		filename += ".py"
		file = open(filename, "w+")
		file.write(code)
		file.close()
		import os
		os.system("python " + filename)
