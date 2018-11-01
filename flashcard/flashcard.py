''' Proggy to do basic learning of thingies in the terminal. '''

import click
import random

# used to tell Click that -h is shorthand for help
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

class QAItem():
  def __init__(self, string):
    stringsplit = string.split(',')
    self.question = stringsplit[0]
    self.answer = stringsplit[1]
    if len(stringsplit) > 2:
      self.details = stringsplit[2]
    else:
      self.details = ''

def display_question(question):
  click.clear()
  click.echo('QUESTION:')
  click.echo(question)

def display_answer(answer, user_answer, details):
  color = 'green' if answer == user_answer else 'white'
  click.echo(click.style(user_answer, fg=color))
  if answer != user_answer:
    click.echo('Correct answer: {}'.format(answer))
  click.echo(details)

# START CLI COMMANDS
@click.command(context_settings=CONTEXT_SETTINGS)
# required arguments
@click.argument('in-file', type=click.File('r'), required=True)

# optional arguments
@click.option('--ignore-case', '-i', is_flag=True,
              help='Ignores letter case when searching and matching.')
# other required arguments
@click.version_option(version='1.0.0')

# main entry point function
def cli(in_file, ignore_case):
  qas = [QAItem(x.strip()) for x in in_file.readlines()]
  while True:
    shuffley = random.shuffle(qas)

    for item in shuffley:
      display_question(item.question)
      user_answer = input('> ')

      if ignore_case:
        user_answer = user_answer.lower()
        item.answer = item.answer.lower()

      display_answer(item.answer, user_answer, item.details)
      input('Press any key to continue...')
    keep_going = input('Finished. Replay? (y/n) ')
    if keep_going.lower().startswith('y'):
      continue
    else:
      break
  click.echo('Finished now.')

  