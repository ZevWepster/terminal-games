import random
import time

print('Welkom bij Zevs Bere Gezellige BINGO! ')
print('Druk op ENTER om je antwoord te bevestigen. ')
time.sleep(1)


def begin():
  try:
    amount_rounds = int(input(
      "Hoeveel rondes wil je spelen?: "))  # <--(try kan niet zonder except)
  except ValueError:  #<-- creert loop bij andere invoer dan nummers
    amount_rounds = int(input("Voer een getal in a.u.b "))

  confirm_rounds = input(
    "Weet je het zeker? Druk op \'j\' voor JA en druk op \'n\' voor NEE. ")

  while confirm_rounds != 'j' and confirm_rounds != 'n':
    confirm_rounds = input(
      "Weet je het zeker? Druk op \'j\' voor JA en druk op \'n\' voor NEE. ")

  while confirm_rounds == 'n':
    try:
      amount_rounds = int(input('Hoeveel rondes wil je spelen? '))
    except ValueError:
      amount_rounds = int(input('Voer een getal in a.u.b. '))
    confirm_rounds = input(
      'Weet je het zeker? Druk op \'j\' voor JA en druk op \'n\' voor NEE. ')

  if confirm_rounds == 'j':
    print('Tijd voor BINGO!!!')
    ready = input('Druk op ENTER voor de eerste bal! ')

    if ready >= '':
        already_called = []  # <--storage getrokken nummers
        x = 0  # <--storage aantal rondes
        while x < amount_rounds:
            round_numbers = []
            while len(round_numbers) < 5:
                next_num = random.randint(1, 91)
                if next_num not in already_called:
                    already_called.append(next_num)
                    round_numbers.append(next_num)
            print(f"Ronde {x+1}: {', '.join(str(num) for num in round_numbers)}")
            time.sleep(2)  # <--tijd tussen de ballen
            x += 1
        print('Het gekozen aantal rondes is bereikt. ')
        time.sleep(2)
        print('Bedankt voor het spelen! ')


# command voor het starten van de game/ begin cyclus
begin()
# nog een keer spelen?
again = input(
  'Wil je nog een keer spelen? Druk op \'j\' voor JA en druk op \'n\' voor NEE. '
)
#loop tot juiste input
while again != 'j' and again != 'n':
  again = input(
    'Wil je nog een keer spelen? Druk op \'j\' voor JA en druk op \'n\' voor NEE. '
  )
# spel blijft zich herhalen tot user n invoert
while again == 'j':
  begin()
  again = input(
    'Wil je nog een keer spelen? Druk op \'j\' voor JA en druk op \'n\' voor NEE. '
  )

  while again != 'j' and again != 'n':
    again = input(
      'Dat is geen nummer.. Druk op \'j\' voor JA en druk op \'n\' voor NEE. ')
#einde loop/ spel
if again == 'n':
  print('Ook goed..')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print('.')
  time.sleep(1)
  print('De ballen! ')
  time.sleep(2)
