def calcular_promedio(numeros):
  """
  Calcula el promedio de una lista de números.

  Args:
    numeros: Una lista de números (enteros o flotantes).

  Returns:
    El promedio de los números en la lista.

  Raises:
    ValueError: Si la lista de entrada está vacía.
  """
  if not numeros:
    raise ValueError("La lista no puede estar vacía.")

  return sum(numeros) / len(numeros)
