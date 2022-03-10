import numpy as np

def ExamineNumpyEx1(result):
  jud = result == 46.265625
  if jud:
    return "SUCCESS!"
  return "WRONG ANSWER!"


def ExamineNumpyEx2(result):
  jud = list(result) == list(np.load('./NumpyResultEx2.npy'))
  if jud:
    return "SUCCESS!"
  return "WRONG ANSWER!"


def ExamineNumpyEx3(result):
  jud = (np.array(result).astype(np.float64) == np.load('./NumpyResultEx3.npy')).all()
  if jud:
    return "SUCCESS!"
  return "WRONG ANSWER!"