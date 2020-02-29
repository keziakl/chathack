'''
REPL main runner for chathack chatbot
'''
import argparse
import cmd
import logging
import sys
logging.basicConfig()
logger = logging.getLogger(__name__)

# Uncomment me to see which REPL commands are being run!
# logger.setLevel(logging.DEBUG)

from daskalos import Daskalos

# Modular ASCII font from http://patorjk.com/software/taag/
HEADER = "A warm hello from Daskalos"

class REPL(cmd.Cmd):
    """Simple REPL to handle the conversation with the chatbot."""
    prompt = '> '
    doc_header = ''
    misc_header = ''
    undoc_header = ''
    ruler = '-'

    def __init__(self, creative=False):
        super().__init__()

        self.daskalos = Daskalos()
        self.name = self.daskalos.name
        
        self.bot_prompt = "Oi! "
        
        self.greeting = self.daskalos.greeting()
        self.intro = self.daskalos.intro() + '\n' + self.bot_prompt + self.greeting

    def cmdloop(self, intro=None):
        return super().cmdloop(intro)

    def preloop(self):
        print(HEADER)

    def postloop(self):
        goodbye = self.daskalos.goodbye()
        print(self.bot_says(goodbye))

    def emptyline(self):
        return super().emptyline()

    def default(self, line):
        if line == ":quit":
            return True
        else:
            response = self.daskalos.process(line)
            print(self.bot_says(response))

    def precmd(self, line):
        return super().precmd(line)

    def postcmd(self, stop, line):
        if line == ':quit':
            return True

        return super().postcmd(stop, line)

    def bot_says(self, response):
        return response


def process_command_line():
    
    #parser = argparse.ArgumentParser(description=pa6_description)
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    '''
    Permits interaction with Daskalos
    '''
    class Tee(object):
      # Modified from https://stackoverflow.com/questions/34366763/input-redirection-with-python
      def __init__(self, input_handle, output_handle):
        self.input = input_handle
        self.output = output_handle

      def readline(self):
        result = self.input.readline()
        self.output.write(result)
        self.output.write('\n')
        self.output.flush()

        return result

      # Forward all other attribute references to the input object.
      def __getattr__(self, attr):
        return getattr(self.input, attr)

    if not sys.stdin.isatty():
      sys.stdin = Tee(input_handle=sys.stdin, output_handle=sys.stdout)


    args = process_command_line()
    repl = REPL()
    repl.cmdloop()
