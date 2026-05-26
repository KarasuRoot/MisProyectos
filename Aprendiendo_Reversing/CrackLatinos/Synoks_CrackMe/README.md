English:
# Versión en Inglés (English Version)

```markdown
# Basic Key Generator (Simulated Keygen)

This repository contains an educational Python script that illustrates the most fundamental mathematical logic behind a key generator (Keygen) tailored for elementary reverse engineering challenges or *crackmes*.

## 📋 Algorithm Description

The script showcases two programming approaches (`Version1` and `Version2`) to solve the exact same validation formula. The "serial number" logic relies strictly on a structural property (the length) of the string supplied by the user:

$$\text{Serial} = \text{Length of Name} \times 4$$

---

## 🔍 Code Walkthrough

### Version 1: Structured Approach (Step-by-Step)
```python
nombre = input('Indique el Usuario: ')
long = len(nombre)
serial = long * 4
print('La Clave para tu usuario', nombre, 'es:', serial)


Español:
Este repositorio contiene un script educativo de Python que ilustra la lógica matemática más básica detrás de un generador de claves (Keygen) para desafíos de ingeniería inversa o *crackmes* elementales.

## 📋 Descripción del Algoritmo

El script expone dos aproximaciones (`Version1` y `Version2`) para resolver la misma fórmula de validación. La lógica del "número de serie" se basa estrictamente en una propiedad geométrica o de longitud de la cadena de caracteres introducida por el usuario:

$$\text{Serial} = \text{Longitud del Nombre} \times 4$$

---

## 🔍 Análisis del Código

### Versión 1: Enfoque Estructurado (Paso a Paso)
```python
nombre = input('Indique el Usuario: ')
long = len(nombre)
serial = long * 4
print('La Clave para tu usuario', nombre, 'es:', serial)