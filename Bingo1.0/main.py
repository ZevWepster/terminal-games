import random
import time

print('Welkom bij Zevs Bere Gezellige BINGO! ')
print('Druk op ENTER om je antwoord te bevestigen. ')
time.sleep(1)


def begin():
  try:
    amount_rounds = int(input("Hoeveel rondes wil je spelen?: "))
  except ValueError:
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
    input('Druk op ENTER voor de eerste ronde! ')
    
    all_numbers = list(range(1, 91))
    random.shuffle(all_numbers)
    already_called = set()
    x = 0

    while x < amount_rounds and len(already_called) + 5 <= 90:
      print(f"\n--- Ronde {x + 1} ---")
      round_numbers = []

      while len(round_numbers) < 5:
        num = all_numbers.pop()
        if num not in already_called:
          already_called.add(num)
          round_numbers.append(num)

      for number in round_numbers:
        print(f"Nummer: {number}")
        time.sleep(5)

      x += 1

      if x < amount_rounds:
        input("\nDruk op ENTER voor de volgende ronde...")

    print('\nHet gekozen aantal rondes is bereikt.')
    time.sleep(2)
    print('Bedankt voor het spelen!')



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
