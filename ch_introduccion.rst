Introducción
============



Este libro surge por una sola razón: no existe mucho material sobre reStructuredText que digamos. Y, la verdad, no entiendo por qué (sí, lo que viene es un poco de mi historia).

Por azares del destino, mi trabajo me llevó a crear documentación/material de apoyo para la capacitación del nuevo personal, tanto como para los procesos típicos documentados paso por paso en largos mamotretos creados con Microsoft Word, hasta procesos que involucraban correr consultas de SQL bastante largas, mismas que copiabamos de un Wiki.

Por "razones de seguridad" el Wiki fue cerrado, toda la documentación que allí se encontraba tuvo que abandonar la nave que se hundía, y decidí darme a la tarea de encontrar alternativas (igual era mi responsabilidad capacitar a la gente, con o sin material de apoyo).

La decisión lógica, a la que todo programador termina llegando, fue Markdown. No obstante, tenía un problema para mí: todas las consultas en SQL tenían que ser copiadas dentro de cada documento donde se explicara el procedimiento, además de tener los archivos fuente aparte. Eso no va bien con esa idea de DRY (algo como "no dupliques información", del inglés "Don't Repeat Yourself").

Y, sí, claro, hay una variante de Markdown que podía hacer eso de enlazar los archivos... pero desde mi punto de vista, eso ya no era Markdown, y era otra cosa más que explicar a mis compañeros de trabajo.

Siendo responsable no solo de escribir la documentación, sino también de publicarla, distribuirla, y capacitar a mis compañeros en su uso... explicar las diferencias de los sabores de Markdown, además de tener que usar diversos procesadores para generar el HTML y el PDF, me parecía demasiado confuso.

Seguí buscando y me encontré con reST (por cierto, utilizaré tanto *reST* como *rst* para referirme a *reStructuredText* de ahora en adelante): una sintaxis diseñada por programadores para generar documentación.

Suficiente. Mi labor no es convencerte de las maravillas que reST puede hacer, solamente exponer. Sigamos.



¿Cómo leer este libro?
----------------------



Este libro está diseñado para ser una referencia de reStructuredText, al menos de los elementos más utilizados de este lenguaje. Si eres nuevo en el uso de reST, recomiendo leer este libro completo para darte una idea de qué puedes hacer con él. Posteriormente, si te agradan sus posibilidades, puedes aprender como usar sus elementos básicos y sus directivas.

En caso de ya estar familiarizado con el lenguaje, puedes utilizar este material como referencia, para recordar elmentos de la sintaxis.

.. note::

	En esta obra se muestra el texto fuente en reST y su salida a pantalla (bueno, a libro). Es decir, no se verá el código generado en HTML o LaTeX dado que esta obra está dirigida a personas sin conocimiento previo de lenguajes de marcado y considero que sería más confuso la inclusión de dicho código.



¿Cómo contribuir a esta obra?
-----------------------------



Este libro es de código abierto y se puede contribuir a él. El repositorio está alojado en GitHub_, y puedes consultar las instrucciónes para contribuir en el archivo CONTRIBUTING_.



Reportando un problema
----------------------



En caso de que encuentres algún problema en la obra, puedes `crear un problema`_ en GitHub y trabajaré en resolverlo.



.. _GitHub: https://github.com/ramoscarlos/guia-rst
.. _CONTRIBUTING: https://github.com/ramoscarlos/guia-rst/blob/master/CONTRIBUTING.md
.. _crear un problema: https://github.com/ramoscarlos/guia-rst/issues