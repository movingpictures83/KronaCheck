import sys

class KronaCheckPlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
     for line in self.infile:
      contents = line.strip().split('\t')
      for i in range(len(contents)):
        if (contents[i].startswith("(Kingdom)")):
            if (i <= 3):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Phylum)")):
            if (i <= 4):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Class)")):
            if (i <= 5):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Order)")):
            if (i <= 6):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Family)")):
            if (i <= 7):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Genus)")):
            if (i <= 8):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
        if (contents[i].startswith("(Species)")):
            if (i <= 9):
                print("WARNING: FOUND "+contents[i]+" AT POSITION "+str(i))
