
import subprocess

class Compiler:
    def __init__(self,code):
        self.code = code
      
    def run(self):
        try: 
            self.op = subprocess.check_output(
                    ['python', '-c', self.code],
                    stderr=subprocess.STDOUT,
                    universal_newlines=True
                )
        except:
            self.op = "some error"
    def output(self):
        return self.op