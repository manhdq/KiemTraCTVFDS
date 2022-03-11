from colorama import Fore

def GTExamineEx1(func):
  visual_all = False
  inputs = ['aadefxfedy', 'abbb', 'abcdef', 'abcdeata', 'fff', 'abaccadae']
  targets = [3, 2, 6, 6, 1, 4]

  preds = []
  for i, input in enumerate(inputs):
    try:
      pred = func(input)
      if visual_all:
        print(input + ':  ' + str(targets[i]) + '  -  ' + str(pred))
      preds.append(pred)
    except:
      if visual_all:
        print(input + ':  ' + str(targets[i]) + '  -  Wrong code')
      preds.append(-1)
  
  import numpy as np
  count = sum(np.array(targets) == np.array(preds))
  if count == len(targets):
    fore = Fore.GREEN + 'SUCCESS! '
  else:
    fore = Fore.RED
  
  print(fore + f'{count}/{len(targets)} testcase(s) are correct!')

def GTExamineEx2(func):
  visual_all = False
  inputs = ['efgttgfe', 'abbbb', 'abcdfe', 'aadefxfedy', 'abbb', 'abcdef', 'abcdeata', 'fff', 'abaccadae']
  targets = [4, 2, 6, 6, 2, 6, 6, 1, 5]

  preds = []
  for i, input in enumerate(inputs):
    try:
      pred = func(input)
      if visual_all:
        print(input + ':  ' + str(targets[i]) + '  -  ' + str(pred))
      preds.append(pred)
    except:
      if visual_all:
        print(input + ':  ' + str(targets[i]) + '  -  Wrong code')
      preds.append(-1)
  
  import numpy as np
  count = sum(np.array(targets) == np.array(preds))
  if count == len(targets):
    fore = Fore.GREEN + 'SUCCESS! '
  else:
    fore = Fore.RED
  
  print(fore + f'{count}/{len(targets)} testcase(s) are correct!')